from sqlmodel import SQLModel,Field, Column, Relationship
import sqlalchemy.dialects.postgresql as pg
import uuid
from sqlalchemy import Text
from datetime import datetime



class User(SQLModel, table=True):
    __tablename__ = "users"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    username: str
    password: str = Field(exclude=True)
    email: str
    first_name: str
    last_name: str
    created_on: datetime = Field(default_factory=datetime.now, sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    modify_on : datetime = Field(default_factory=datetime.now, sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    def __repr__(self):
        return f"<User {self.username}>"


class Shoes(SQLModel, table=True):
    __tablename__="shoes"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    title: str
    brand: str
    category: str
    price: float
    image_url: str
    sizes: str

    def __repr__(self):
        return f"<Shoes {self.title}>"
    
class Orders(SQLModel, table=True):
    __tablename__="orders"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    customer_name: str
    customer_email: str
    address: str
    items: str = Field(sa_column=Column(Text, nullable=False))

