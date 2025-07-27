from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.database.db_object_factory import DbObjectFactory
from services.countries.countries_service import CountriesService
from interfaces.countries.countries_aggregator import CountriesAggregatorInterface
from logs import logger

class CountriesRepository:
    def __init__(self, countries_factory: DbObjectFactory,
                countries_service: CountriesService,
                countries_aggregator: CountriesAggregatorInterface):
        self.countries_factory = countries_factory
        self.countries_service = countries_service
        self.countries_aggregator = countries_aggregator

    async def insert_countries(self, countries_data: list[dict], session: AsyncSession):
        try:
            countries = self.countries_factory.create(countries_data)
            logger.info(f"Created {len(countries)} Country objects")
            
            result = await self.countries_service.insert_countries(countries, session)
            logger.info("Countries inserted successfully")
            return result
            
        except Exception as e:
            logger.error(f"Failed to insert countries: {e}")
            raise
    
    async def get_countries(self, session: AsyncSession):
        return await self.countries_aggregator.aggregate_countries(session)