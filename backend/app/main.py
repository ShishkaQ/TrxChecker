from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tronpy import Tron
from tronpy.providers import HTTPProvider
import os
from pathlib import Path
from dotenv import load_dotenv

from backend.app.models import write_data, get_all_data
from backend.app.schemas import AddressRequest

# Загрузка .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = FastAPI()

# CORS настройки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TRONGRID_API_KEY = os.getenv("TRONGRID_API_KEY")

@app.post("/address-info/")
async def set_address(AddressRequest: AddressRequest) -> dict:
    provider = HTTPProvider(api_key=TRONGRID_API_KEY)
    client = Tron(provider)
    
    address = AddressRequest.address
    
    # Получение данных кошелька
    resource = client.get_account_resource(address)
    account = client.get_account(address)

    # Расчет показателей
    freeNetLimit = resource.get('freeNetLimit', 0)
    total_net_limit = resource.get('NetLimit', 0) + freeNetLimit
    total_net_used = resource.get('NetUsed', 0)
    bandwidth = total_net_limit - total_net_used

    energy_limit = resource.get('EnergyLimit', 0)
    energy_used = resource.get('EnergyUsed', 0)
    energy = energy_limit - energy_used

    balance = client.get_account_balance(address)

    # Сохранение в БД
    await write_data(address, bandwidth, energy, balance)

    return {
        "bandwidth": bandwidth,
        "energy": energy,
        "balance": balance
    }

@app.get("/users-info/")
async def get_users() -> list:

    users = await get_all_data()

    users.reverse()

    return users