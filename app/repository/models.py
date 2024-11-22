from sqlalchemy import Column, Integer, String, ForeignKey, TEXT, Table
from sqlalchemy.dialects.postgresql import BIT
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.testing import db

Base = declarative_base()

supplier_land_crop = Table(
    'supplier_land_crop',
    Base.metadata,
    Column('supplier_id', ForeignKey('suppliers.id'), primary_key=True),
    Column('land_crop_id', ForeignKey('land_crops.id'), primary_key=True),
)


class Supplier(db.Model):
    __tablename__ = 'supplier'
    name = Column(TEXT(None, 'Cyrillic_General_CI_AS'), nullable=True)
    contact_person = Column(TEXT(None, 'Cyrillic_General_CI_AS'), nullable=True)
    inn = Column(String(15, 'Cyrillic_General_CI_AS'), nullable=True)
    storage_address = Column(TEXT(None, 'Cyrillic_General_CI_AS'))
    phone = Column(String(255, 'Cyrillic_General_CI_AS'))
    id = Column(Integer, primary_key=True)
    subscription_cancelled = Column(BIT, nullable=True, comment="Отписан ли от рассылки")
    subscription_admin = Column(BIT, nullable=True, comment="Отписан ли от рассылки админом")
    district_id = Column(ForeignKey('district.id'), nullable=True, comment="id области")
    district = relationship('District')
    area_id = Column(ForeignKey('area.id'), nullable=True, comment="id района")
    area = relationship('Area')
    manager_id = Column(ForeignKey('user.id'), nullable=True)
    manager = relationship('User')
    land_crop = relationship('LandCrop', secondary=supplier_land_crop, backref=backref('suppliers'))
    landuser = Column(String(255, 'Cyrillic_General_CI_AS'), nullable=True)


class District(Base):
    __tablename__ = 'district'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, comment="Название области")
    utc_offset = Column(Integer, nullable=False, comment="Смещение от UTC")
