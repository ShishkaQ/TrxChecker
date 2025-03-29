from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class AddressRequest(BaseModel):
    address: str


class UserResponse(BaseModel):
    id: int
    address: str
    bandwidth: int
    energy: int
    balance: float


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    balance = Column(Float)
    
    # Метод для преобразования в словарь
    def to_dict(self):
        return {
            "id": self.id,
            "address": self.address,
            "bandwidth": self.bandwidth,
            "energy": self.energy,
            "balance": self.balance
        }