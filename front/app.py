import aiohttp
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import grpc

import greeting_pb2
import greeting_pb2_grpc


HELLO_ADDR = "hello:8000"
GREETER_ADDR = "greeter:50051"


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


def greet(name):
    with grpc.insecure_channel(GREETER_ADDR) as channel:
        stub = greeting_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greeting_pb2.HelloRequest(name=name))
    return response.message


async def index(request):
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, f"http://{HELLO_ADDR}")
    message = greet(data["name"])
    return PlainTextResponse(message)


app = Starlette(routes=[Route("/", index)])
