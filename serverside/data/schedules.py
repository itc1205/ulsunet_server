import sqlalchemy

from sqlalchemy import orm

from .db_session import SqlAlchemyBase

class Schedule(SqlAlchemyBase):
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    lections = sqlalchemy.Column(sqlalchemy.String)
    places = sqlalchemy.Column(sqlalchemy.String)

    group = orm.relation()