from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

#create base_model
Base = declarative_base()

#defining events model
class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    price = Column(String(), nullable=False)
    rating = Column(String(), nullable=False)
    category = Column(String(), nullable=False)
 