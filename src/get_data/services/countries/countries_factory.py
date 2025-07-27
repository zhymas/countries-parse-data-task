from models.countries import Country
from interfaces.database.db_object_factory import DbObjectFactory
from services.countries.countries_exceptions import CountriesDBException

class CountriesFactory(DbObjectFactory[Country]):
    def create(self, countries_data: list[dict]) -> list[Country]:
        try:
            return [Country(country=data['country'], population=data['population'], region=data['region']) for data in countries_data]
        except CountriesDBException as e:
            raise e
        except Exception as e:
            raise Exception(f"Unknown error: {e}")