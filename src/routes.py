from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from models import User, Device, user_device
from datetime import datetime
from base_functions import aggregate_data, model_to_dict

router = APIRouter()


@router.get('/devices/{id}')
async def get_device_statistics(
        id: int,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        result = await session.execute(select(Device).filter_by(device_id=id))
        return result.scalars().all()
    except Exception as e:
        raise e
        return {"message": "Something went wrong :("}


@router.get('/devices/{id}/analysis')
async def get_device_analysis(
        id: int,
        date_from: datetime = None,
        date_to: datetime = None,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        filters = [Device.device_id == id]
        if date_from:
            filters.append(Device.created_at >= date_from)
        if date_to:
            filters.append(Device.created_at <= date_to)
        data = await session.execute(select(Device).
                                     filter(*filters))
        scalars_data = data.scalars().all()
        result = aggregate_data(model_to_dict(scalars_data))
        return result
    except Exception as e:
        print(e)
        return {"message": "Something went wrong :("}


@router.post('/users/{user_id}/add')
async def add_user_device(
        user_id: int,
        device_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        await session.execute(user_device.insert().values(user_id=user_id, device_id=device_id))
        await session.commit()
        return {"message": "User and device added to each other successfully"}
    except Exception as e:
        return {"message": "Something went wrong :("}


@router.get('/users/{user_id}/devices')
async def get_device_analysis_by_user(
        user_id: int,
        device_id: int = None,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        all_user_device = await session.execute(select(user_device).
                                                order_by(user_device.c.device_id, user_device.c.user_id).
                                                where(user_device.c.user_id == user_id))
        ans_devices = []
        if device_id:
            for elem in all_user_device:
                if elem[1] == device_id:
                    device = await session.execute(select(Device).filter(Device.device_id == elem[1]))
                    ans_devices.append(device.scalar())
                    break
        else:
            for elem in all_user_device:
                device = await session.execute(select(Device).filter(Device.device_id == elem[1]))
                ans_devices.append(device.scalar())
        device_analysis = aggregate_data(model_to_dict(ans_devices))
        return device_analysis
    except Exception as e:
        return {"message": "Something went wrong :("}
