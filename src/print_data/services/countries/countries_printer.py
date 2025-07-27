from typing import List, Dict, Any
from logs import logger

class CountriesPrinter:
    def print_region_statistics(self, aggregated_data: List[Dict[str, Any]]) -> None:
        try:
            for region_data in aggregated_data:
                print(f"Region: {region_data['region']}")
                print(f"Total population: {region_data['total_population']:,}")
                print(f"Largest country: {region_data['largest_country']['name']}")
                print(f"Largest country population: {region_data['largest_country']['population']:,}")
                print(f"Smallest country: {region_data['smallest_country']['name']}")
                print(f"Smallest country population: {region_data['smallest_country']['population']:,}")
                print("-" * 80)
                
            logger.info(f"Printed statistics for {len(aggregated_data)} regions")
            
        except Exception as e:
            logger.error(f"Failed to print region statistics: {e}")
            raise 