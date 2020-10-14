import random
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


NAMES = ["Oliver", "Charlotte", "Theodore"]


async def index(request):
    name = random.choice(NAMES)
    return JSONResponse({"name": name})


app = Starlette(routes=[Route("/", index)])
