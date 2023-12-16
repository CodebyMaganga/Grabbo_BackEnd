from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

#create base_model
Base = declarative_base()

#defining events model
class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(String())
    rating = Column(String())
    category = Column(String())
 