import httpx
from proxy.user_agent_pool import get_user_agent
from proxy.proxy_rotator import get_proxy

class RequestHandler:
    async def fetch(self, url):
        headers = {'User-Agent': get_user_agent()}
        proxy = get_proxy()
        async with httpx.AsyncClient(proxies=proxy, headers=headers, timeout=10) as client:
            try:
                r = await client.get(url)
                r.raise_for_status()
                return r.text
            except Exception as e:
                print(f"Error: {e}")
                return None