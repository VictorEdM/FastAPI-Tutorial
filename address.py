from pydantic import BaseModel


class Address(BaseModel):
    name: str
    number: int