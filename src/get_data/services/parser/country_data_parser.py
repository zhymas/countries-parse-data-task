from bs4 import BeautifulSoup
from typing import List, Dict, Any

from interfaces.parsers.parser_country_data_interface import CountriesParserDataInterface
from interfaces.request_service.request_service import RequestServiceInterface

class CountriesDataParser(CountriesParserDataInterface):
    def __init__(self, 
                 request_service: RequestServiceInterface,
                 countries_url: str):
        self.countries_url = countries_url
        self.request_service = request_service

    async def parse_country_data(self) -> List[Dict[str, Any]]:
        return await self._get_countries_data()
        
    async def _get_countries_data(self) -> List[Dict[str, Any]]:
        response = await self.request_service.get_request(self.countries_url)
        return self._parse_html_table(response.text)
    
    def _parse_html_table(self, html_content: str) -> List[Dict[str, Any]]:
        soup = BeautifulSoup(html_content, 'lxml')
        country_table = self._find_country_table(soup)
        return self._extract_countries_data(country_table)
    
    def _find_country_table(self, soup: BeautifulSoup):
        country_table = soup.find("table", {"class": "wikitable"})
        if not country_table:
            raise ValueError("Failed to find the table with country data on the page")
        return country_table
    
    def _extract_countries_data(self, table) -> List[Dict[str, Any]]:
        tbody = table.find("tbody") or table
        rows = tbody.find_all("tr")
        countries_data = []
        
        for row in rows[1:]:
            country_data = self._parse_country_row(row)
            if country_data:
                countries_data.append(country_data)
        
        return countries_data
    
    def _parse_country_row(self, row) -> Dict[str, Any]:
        cells = row.find_all(["td", "th"])
        if len(cells) < 6:
            return None
            
        try:
            return {
                "country": cells[0].get_text(strip=True),
                "population_2023": cells[1].get_text(strip=True),
                "location": cells[5].get_text(strip=True)
            }
        except (IndexError, AttributeError):
            return None


