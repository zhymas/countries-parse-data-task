import httpx

from interfaces.parsers.parser_country_data_interface import CountriesParserDataInterface
from config.config import config

class CountriesDataParser(CountriesParserDataInterface):
    def __init__(self):
        self.countries_url = config.countries.countries_url

    async def parse_country_data(self) -> dict:
        return await self._get_countries_data()
        
    async def _get_countries_data(self) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.countries_url)
            return response.json()