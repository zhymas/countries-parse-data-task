from dependency_injector import containers, providers

from services.countries.countries_aggregator import CountriesAggregator
from services.countries.countries_printer import CountriesPrinter

class Container(containers.DeclarativeContainer):
    countries_aggregator = providers.Singleton(CountriesAggregator)
    countries_printer = providers.Singleton(CountriesPrinter)