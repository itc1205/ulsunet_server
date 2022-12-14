from datetime import datetime as dt

import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Group(SqlAlchemyBase):
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    
    group_name = sqlalchemy.Column(sqlalchemy.String)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    course = sqlalchemy.Column(sqlalchemy.Integer)

    users = orm.releation("Users", back_populates="group")
    schedule = orm.releation("Group")