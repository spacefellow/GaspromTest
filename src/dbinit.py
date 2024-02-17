import random
from models import User, Device
import time
from fastapi import Depends
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
import datetime


devices = [{'device_id': i,
            'x': float(random.randint(1, 10)),
            'y': float(random.randint(1, 10)),
            'z': float(random.randint(1, 10))} for i in range(5)]

devices.extend(devices)

users = [{'id': i} for i in range(4)]


async def add_user(user: User, current_session: AsyncSession = Depends(get_async_session)):
    for i in users:
        try:
            stmt = insert(user).values(
                id=i['id']
            ).on_conflict_do_nothing()
            await current_session.execute(stmt)
            await current_session.commit()
        except Exception as e:
            continue
    print('users added')


async def add_device(device: Device, current_session: AsyncSession = Depends(get_async_session)):
    for i in devices:
        time.sleep(1)
        try:
            stmt = insert(device).values(
                device_id=i['device_id'],
                x=i['x'],
                y=i['y'],
                z=i['z'],
                created_at=datetime.datetime.now()
            ).on_conflict_do_nothing()
            await current_session.execute(stmt)
            await current_session.commit()
        except Exception as e:
            continue
    print('devices added')





async def fill():
    func_list = [
        (add_user, User),
        (add_device, Device),
    ]
    for func in func_list:
        async for session in get_async_session():
            try:
                await func[0](func[1], session)
            except Exception as e:
                print(e)


def main():
    import asyncio
    asyncio.run(fill())


main()
