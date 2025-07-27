from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from logs import logger
from typing import List, Dict, Any

class CountriesAggregator:
    async def aggregate_countries_by_region(self, session: AsyncSession) -> List[Dict[str, Any]]:
        try:
            query = text("""
                WITH region_stats AS (
                    SELECT 
                        region,
                        SUM(population) as total_population,
                        COUNT(*) as country_count
                    FROM countries 
                    WHERE region != ''
                    GROUP BY region
                ),
                largest_countries AS (
                    SELECT 
                        region,
                        country as largest_country_name,
                        population as largest_country_population,
                        ROW_NUMBER() OVER (PARTITION BY region ORDER BY population DESC) as rn_largest
                    FROM countries 
                    WHERE region != ''
                ),
                smallest_countries AS (
                    SELECT 
                        region,
                        country as smallest_country_name,
                        population as smallest_country_population,
                        ROW_NUMBER() OVER (PARTITION BY region ORDER BY population ASC) as rn_smallest
                    FROM countries 
                    WHERE region != ''
                )
                SELECT 
                    rs.region,
                    rs.total_population,
                    lc.largest_country_name,
                    lc.largest_country_population,
                    sc.smallest_country_name,
                    sc.smallest_country_population
                FROM region_stats rs
                LEFT JOIN largest_countries lc ON rs.region = lc.region AND lc.rn_largest = 1
                LEFT JOIN smallest_countries sc ON rs.region = sc.region AND sc.rn_smallest = 1
                ORDER BY rs.region
            """)
            
            result = await session.execute(query)
            rows = result.fetchall()
            
            aggregated_data = []
            for row in rows:
                aggregated_data.append({
                    'region': row.region,
                    'total_population': row.total_population,
                    'largest_country': {
                        'name': row.largest_country_name,
                        'population': row.largest_country_population
                    },
                    'smallest_country': {
                        'name': row.smallest_country_name,
                        'population': row.smallest_country_population
                    }
                })
            
            logger.info(f"Aggregated data for {len(aggregated_data)} regions using single SQL query")
            return aggregated_data
            
        except Exception as e:
            logger.error(f"Failed to aggregate countries by region: {e}")
            raise 