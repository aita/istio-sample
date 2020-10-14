from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def hello(request):
    return JSONResponse({"message": "hello world"})


app = Starlette(routes=[Route("/", hello)])
