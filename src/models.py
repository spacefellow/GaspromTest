from sqlalchemy import Column, Integer, Double, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import datetime


user_device = Table('user_device', Base.metadata,
                    Column('user_id', ForeignKey('users.id'), primary_key=True),
                    Column('device_id', ForeignKey('devices.id'), primary_key=True)
                    )


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    devices = relationship("Device", secondary="user_device", back_populates='users')


class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, nullable=False)
    x = Column(Double, nullable=True)
    y = Column(Double, nullable=True)
    z = Column(Double, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    users = relationship("User", secondary="user_device", back_populates='devices')
