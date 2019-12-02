from datetime import datetime
import sqlalchemy
from data.modelbase import SqlAlchemyBase


class License(SqlAlchemyBase):
    __tablename__ = 'licenses'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, index=True)
    description = sqlalchemy.Column(sqlalchemy.String)