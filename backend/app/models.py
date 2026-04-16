from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Float
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Zone(Base):
    __tablename__ = 'zones'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('urban', 'rural', 'suburban', name='zone_type_enum'), nullable=False)
    parent_id = Column(Integer, ForeignKey('zones.id'))
    geometry = Column(Geometry('GEOMETRY'))
    
    parent = relationship('Zone', remote_side=[id], backref='children')

class Dealer(Base):
    __tablename__ = 'dealers'
    id = Column(Integer, primary_key=True)
    zone_id = Column(Integer, ForeignKey('zones.id'), nullable=False)
    category = Column(Enum('category1', 'category2', 'category3', name='dealer_category_enum'), nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    
    zone = relationship('Zone')

class UploadedSession(Base):
    __tablename__ = 'uploaded_sessions'
    id = Column(Integer, primary_key=True)
    file_metadata = Column(String, nullable=False)
    column_mappings = Column(String, nullable=False)
    data_storage = Column(String, nullable=False)

class AppConfig(Base):
    __tablename__ = 'app_config'
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, nullable=False)
    value = Column(String, nullable=False)