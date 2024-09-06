from pydantic import BaseModel


class CallSchema(BaseModel):
    phone: int
    address: str
