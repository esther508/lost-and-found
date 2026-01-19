from sqlalchemy import Column, Integer, String
from database import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(256))
    description = Column(String(300))
    location = Column(String(200))
    date = Column(String(50))
    contact_information = Column(String(20))
    status = Column(String(20))
