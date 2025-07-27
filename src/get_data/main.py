import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from services.request_service.request_service import RequestService
from services.parser.country_data_parser import CountriesDataParser
from config.config import config
from logs import logger

async def main():
    request_service = RequestService()
    countries_data_parser = CountriesDataParser(request_service, config.countries.wikipedia_url)
    countries_data = await countries_data_parser.parse_country_data()
    logger.info(f"Countries data parsed: {countries_data}")

if __name__ == "__main__":
    asyncio.run(main())