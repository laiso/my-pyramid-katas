from sqlalchemy import (
    Column,
    Integer,
    Unicode,
)
from pyramid_sqlalchemy import (
    BaseObject,
    Session,
)


class User(BaseObject):
    __tablename__ = 'users'
    query = Session.query_property()
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255), unique=True)
