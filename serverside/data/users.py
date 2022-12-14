from datetime import datetime as dt

import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    profile_image = sqlalchemy.Column(sqlalchemy.String)

    group = sqlalchemy.Column(sqlalchemy.Integer, 
                                sqlalchemy.ForeignKey("group.id"))
    
