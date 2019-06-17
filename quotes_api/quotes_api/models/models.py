from zope.sqlalchemy import ZopeTransactionExtension
from .meta import Base

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)


from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)


Index('my_index', MyModel.name, unique=True, mysql_length=255)
