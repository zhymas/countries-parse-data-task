import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from di.container import Container
from database.database import async_session
from logs import logger

async def main():
    container = Container()
    
    countries_data_parser = container.countries_data_parser()
    countries_repository = container.countries_repository()
    
    try:
        countries_data = await countries_data_parser.parse_country_data()
        logger.info(f"Parsed {len(countries_data)} countries")
        
        async with async_session() as session:
            await countries_repository.insert_countries(countries_data, session)
        
        logger.info("Countries processed successfully!")
        
    except Exception as e:
        logger.error(f"Failed to process countries: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())