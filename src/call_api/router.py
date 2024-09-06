from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update
from call_api.models import call
from call_api.schemas import CallSchema
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

router = APIRouter(
    prefix="/call_api",
    tags=["Operations"]
)


@router.get("/check_data")
async def check_data(phone: int, session: AsyncSession = Depends(get_async_session)):
    query = select(call).where(call.c.phone == phone)
    result = await session.execute(query)
    return result.all()


@router.post("/write_data")
async def write_data(new_phone: CallSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(call).values(**new_phone.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status_code": 201}


@router.put("/write_data")
async def update_data(new_phone: CallSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = update(call).values(**new_phone.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status_code": 201}
