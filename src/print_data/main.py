import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from database.database import async_session
from di.container import Container
from logs import logger

async def main():
    try:
        container = Container()
        
        aggregator = container.countries_aggregator()
        printer = container.countries_printer()
        
        async with async_session() as session:
            logger.info("Starting data aggregation and printing...")
            
            aggregated_data = await aggregator.aggregate_countries_by_region(session)
            
            printer.print_region_statistics(aggregated_data)
            
            logger.info("Data printing completed successfully")
            
    except Exception as e:
        logger.error(f"Failed to print data: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())