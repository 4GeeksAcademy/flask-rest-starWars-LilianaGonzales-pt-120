from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer,DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List

db = SQLAlchemy()

# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }




user_vehicle = db.Table('users_characters',
    db.Column('id', db.Integer, primary_key = True),
    db.Column('user_id', db.Integer,db.ForeignKey("users.id"), nullable=False),
    db.Column('character_id', db.Integer,db.ForeignKey("characters.id"), nullable=False),
    db.Column('favorite', db.Boolean(), default=False)
)

class User(db.Model):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(Integer, primary_key= True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)
    subscription: Mapped[datetime] = mapped_column(DateTime)

    characteres: Mapped[List["Character"]] = relationship(back_populates="users", secondary=user_vehicle)

class Character (db.Model):
    __table__= 'characters'

    id:Mapped[int] = mapped_column(Integer, primary_key= True)
    name: Mapped[str] = mapped_column(String(80),nullable=False)
    gender: Mapped[str] = mapped_column(String(20),nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    list_vehicle : Mapped [List["Vehicle"]] = relationship(back_populates="character")

    users: Mapped[List["User"]] = relationship(back_populates="characteres", secondary=user_vehicle )

class Planet (db.Model):
    __table__= 'planets'

    id:Mapped[int] = mapped_column(Integer, primary_key= True)
    name: Mapped[str] = mapped_column(String(50),nullable=False)
    climate: Mapped[str] = mapped_column(String(20),nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime)

class Vehicle (db.Model):
    __table__= 'vehicles'

    id:Mapped[int] = mapped_column(Integer, primary_key= True)
    name: Mapped[str] = mapped_column(String(50),nullable=False)
    model: Mapped[str] = mapped_column(String(20),nullable=False)
    passengers: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    character_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("characters.id"), nullable=False)

    character: Mapped["Character"] = relationship(back_populates="list_vehicle")



