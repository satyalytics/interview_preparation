# configuration
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from slqalchemy.orm import relationship
from sqlalchemy import create engine

Base = declarative_base()
# first part end of configuration


# class started

class Restaurants(Base):
  __tablename__ = 'restaurant'
  
  # mapper
  id_ = Column(Integer, primary_key=True)
  name = Column(String(250), nullable=False)
    
  
class MenuItems(Base):
  __tablename__ = 'menuitem'
  
  # mapper
  name = Column(String(80), nullable=False)
  course = Column(String(250))
  desc = Column(String(250))
  price = Column(String(8))
  restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
  restaurant = relationship(Restaurant)
  
  
# at the end - part of configuration
engine = create_engine('sqlite:///databasename.db')
Base.metadata.create_all(engine)
