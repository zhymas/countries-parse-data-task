from abc import ABC, abstractmethod

import httpx

class RequestServiceInterface(ABC):
    @abstractmethod
    async def get_request(self, url: str, user_agent: bool = True) -> httpx.Response:
        pass