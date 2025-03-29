from sqlalchemy import Column, Integer, String, Float, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.app.schemas import UserResponse, User

# Настройка подключения к БД
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:mysecretpassword@localhost:5432/trondb"
Base = declarative_base()


# Инициализация движка и сессии
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session = sessionmaker(
    engine, 
    expire_on_commit=False, 
    class_=AsyncSession
)

# Функция записи данных (исправлены типы параметров)
async def write_data(address: str, bandwidth: int, energy: int, balance: float):
    async with async_session() as session:
        async with session.begin():
            new_user = User(
                address=address,
                bandwidth=bandwidth,
                energy=energy,
                balance=balance
            )
            session.add(new_user)
        await session.commit()

# Функция получения данных с сериализацией
async def get_all_data():
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        
        # Используем метод to_dict() или фильтрацию __dict__
        return [user.to_dict() for user in users]
        
