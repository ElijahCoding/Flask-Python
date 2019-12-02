from datetime import datetime
import sqlalchemy
from data.modelbase import SqlAlchemyBase

class User(SqlAlchemyBase):
    __tablename__ = 'users'

    