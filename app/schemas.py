from pydantic import BaseModel


class ClientBase(BaseModel):
    email: str


class ClientCreate(ClientBase):
    password: str


class Client(ClientBase):
    id: int
    userName = str
    address = str
    contact = str
    name = str
    birthday = str
    email = str

    class Config:
        orm_mode = True
