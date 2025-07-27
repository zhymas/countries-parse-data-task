import random

import httpx
from requests_random_user_agent import USER_AGENTS

from interfaces.request_service.request_service import RequestServiceInterface

class RequestService(RequestServiceInterface):
    _timeout = 30.0
    
    async def get_request(self,
                           url: str,
                           user_agent: bool = True) -> httpx.Response:
        try:
            async with httpx.AsyncClient(timeout=self._timeout, follow_redirects=True) as client:
                if user_agent:
                    headers = {"User-Agent": self._get_user_agent()}
                response = await client.get(url=url, headers=headers)
                response.raise_for_status()
                return response
        except httpx.HTTPError as e:
            raise httpx.HTTPError(f"GET request failed: {str(e)}")
        
    def _get_user_agent(self) -> str:
        return random.choice(USER_AGENTS)