from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

class CountriesAggregatorInterface(ABC):
    @abstractmethod
    async def aggregate_countries(self, session: AsyncSession):
        pass
