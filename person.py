from pydantic import BaseModel
from address import Address


class Person(BaseModel):
    name: str
    age: int
    addresses: list[Address]
