from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field

ROOT_DIR = Path(__file__).parent.parent.parent
load_dotenv(ROOT_DIR / ".env")

class DatabaseConfig(BaseSettings):
    db_username: str = Field(default="postgres", env="DB_USERNAME")
    db_password: str = Field(default="postgres", env="DB_PASSWORD")
    db_host: str = Field(default="postgres", env="DB_HOST")
    db_port: int = Field(default=5432, env="DB_PORT")
    db_name: str = Field(default="postgres", env="DB_NAME")

    @property
    def asyncpg_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    @property
    def syncpg_url(self) -> str:
        return f"postgresql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
class CountriesConfig(BaseSettings):
    wikipedia_url: str = Field(default="https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959", env="WIKIPEDIA_URL")

class Config(BaseSettings):
    database: DatabaseConfig = DatabaseConfig()
    countries: CountriesConfig = CountriesConfig()

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "extra": "ignore"
    }

config = Config()