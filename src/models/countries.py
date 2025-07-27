from sqlalchemy import Column, BigInteger, String, Integer
from database.database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(255), nullable=False, unique=True)
    population = Column(BigInteger, nullable=False)
    region = Column(String(255), nullable=False)