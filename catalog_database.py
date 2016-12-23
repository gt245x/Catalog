import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Comments(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    user_comments = Column(String(250), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    item_id = Column(Integer,ForeignKey('category_items.user_id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Categories(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Items(Base):
    __tablename__ = 'category_items'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(300))
    picture = Column(String(250))
    price = Column(String(8))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Categories)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'picture': self.picture,
            'price': self.price,
            'created_date': self.created_date,
        }


engine = create_engine('sqlite:///catalogproject.db')


Base.metadata.create_all(engine)