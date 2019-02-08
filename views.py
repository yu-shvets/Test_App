import asyncio
from db.db import process_mysql
from aiohttp import web
import json


async def index(request):
    await asyncio.sleep(10)
    client_data = json.loads(open('db/sample_data.json').read())
    process_mysql(client_data)
    return web.Response(text='Your data was successfully saved and processed!')
