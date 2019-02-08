import asyncio
import sqlalchemy as sa
from aiomysql.sa import create_engine
import json

client_data = json.loads(open('sample_data.json').read())

metadata = sa.MetaData()

tbl = sa.Table('tbl', metadata,
               sa.Column('id', sa.Integer, primary_key=True),
               sa.Column('name', sa.String(255)),
               sa.Column('age', sa.Integer),
               sa.Column('city', sa.String(255))
               )


async def go(loop, client_data):
    engine = await create_engine(user='test_app_user',
                                 db='test_app',
                                 host='127.0.0.1',
                                 password='********',
                                 loop=loop
                                 )
    async with engine.acquire() as conn:
        await conn.execute(tbl.insert().values({'name': client_data['name'],
                                                'age': client_data['age'],
                                                'city': client_data['city']
                                                }))
    engine.close()
    await engine.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(go(loop, client_data))
