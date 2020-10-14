import aiohttp
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


HELLO_ADDR = "hello:8000"


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def index(request):
    async with aiohttp.ClientSession() as session:
        msg = await fetch(session, f"http://{HELLO_ADDR}")
    return PlainTextResponse(msg["message"])


app = Starlette(routes=[Route("/", index)])
