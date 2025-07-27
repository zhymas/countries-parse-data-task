from dependency_injector import containers, providers
from services.countries.countries_factory import CountriesFactory
from services.countries.countries_repository import CountriesRepository
from services.request_service.request_service import RequestService
from services.parser.country_data_parser import CountriesDataParser
from config.config import config

class Container(containers.DeclarativeContainer):
    request_service = providers.Singleton(RequestService)
    
    countries_data_parser = providers.Factory(
        CountriesDataParser,
        request_service=request_service,
        countries_url=config.countries.wikipedia_url
    )
    
    countries_factory = providers.Singleton(CountriesFactory)
    
    countries_repository = providers.Factory(
        CountriesRepository,
        countries_factory=countries_factory
    ) 