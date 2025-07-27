from sqlalchemy.ext.asyncio import AsyncSession
from models.countries import Country
from services.countries.countries_exceptions import CountriesInsertionException
from logs import logger

class CountriesService:
    async def insert_countries(self, 
                               countries: list[Country], 
                               session: AsyncSession):
        if not countries:
            logger.warning("No countries to insert")
            return
            
        try:
            async with session.begin():
                session.add_all(countries)
                await session.commit()
                logger.info(f"Successfully inserted {len(countries)} countries")
                
        except Exception as e:
            logger.error(f"Failed to insert countries: {e}")
            await session.rollback()
            raise CountriesInsertionException(f"Database insertion failed: {e}")