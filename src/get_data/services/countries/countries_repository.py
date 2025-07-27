from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.countries import Country
from interfaces.database.db_object_factory import DbObjectFactory
from logs import logger

class CountriesRepository:
    def __init__(self, countries_factory: DbObjectFactory[Country]):
        self.countries_factory = countries_factory

    async def insert_countries(self, countries_data: list[dict], session: AsyncSession) -> list[Country]:
        try:
            countries = self.countries_factory.create(countries_data)
            logger.info(f"Created {len(countries)} Country objects")
            
            existing_countries = await self.get_all_countries(session)
            existing_names = {country.country for country in existing_countries}
            
            new_countries = [country for country in countries if country.country not in existing_names]
            
            if not new_countries:
                logger.info("All countries already exist in database")
                return existing_countries
            
            session.add_all(new_countries)
            await session.commit()
            logger.info(f"Successfully inserted {len(new_countries)} new countries")
            return new_countries
                
        except Exception as e:
            logger.error(f"Failed to insert countries: {e}")
            await session.rollback()
            raise

    async def get_all_countries(self, session: AsyncSession) -> list[Country]:
        try:
            result = await session.execute(select(Country))
            return result.scalars().all()
        except Exception as e:
            logger.error(f"Failed to get countries: {e}")
            raise

    async def get_country_by_name(self, name: str, session: AsyncSession) -> Country | None:
        try:
            result = await session.execute(
                select(Country).where(Country.country == name)
            )
            return result.scalar_one_or_none()
        except Exception as e:
            logger.error(f"Failed to get country {name}: {e}")
            raise

    async def delete_countries(self, session: AsyncSession) -> None:
        try:
            async with session.begin():
                await session.execute(select(Country).delete())
                await session.commit()
                logger.info("All countries deleted successfully")
        except Exception as e:
            logger.error(f"Failed to delete countries: {e}")
            await session.rollback()
            raise