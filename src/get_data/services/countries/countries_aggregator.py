from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from interfaces.countries.countries_aggregator import CountriesAggregatorInterface
from models.countries import Country

class CountriesAggregator(CountriesAggregatorInterface):
    async def aggregate_countries(self, session: AsyncSession):
        return await self._get_aggregated_countries(session)

    async def _get_aggregated_countries(self, session: AsyncSession):
        return await session.execute(select(Country).order_by(Country.population.desc()))