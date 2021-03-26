# configuration
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from slqalchemy.orm import relationship
from sqlalchemy import create engine

Base = declarative_base()
# first part end of configuration








# at the end - part of configuration
engine = create_engine('sqlite:///databasename.db')
Base.metadata.create_all(engine)
