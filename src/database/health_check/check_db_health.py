import time
import psycopg2
from psycopg2 import OperationalError
from pathlib import Path
import sys

src_path = str(Path(__file__).parent.parent.parent)
if src_path not in sys.path:
    sys.path.append(src_path)

from config.config import config
from logs import logger

def wait_for_postgres():
    max_retries = 30
    retry_interval = 2
    
    db_params = {
        'dbname': config.database.db_name,
        'user': config.database.db_username,
        'password': config.database.db_password,
        'host': config.database.db_host,
        'port': config.database.db_port
    }
    
    for i in range(max_retries):
        try:
            conn = psycopg2.connect(**db_params)
            conn.close()
            logger.info("PostgreSQL is ready!")
            return True
        except OperationalError as e:
            if i == max_retries - 1:
                logger.error(f"Could not connect to PostgreSQL after {max_retries} attempts")
                raise e
            logger.info(f"PostgreSQL is not ready yet. Waiting {retry_interval} seconds... (Attempt {i+1}/{max_retries})")
            time.sleep(retry_interval)
    
    return False

if __name__ == "__main__":
    wait_for_postgres() 