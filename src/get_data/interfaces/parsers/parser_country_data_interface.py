from abc import ABC, abstractmethod

class CountriesParserDataInterface(ABC):
    @abstractmethod
    async def parse_country_data(self) -> dict:
        pass