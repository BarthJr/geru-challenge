from datetime import datetime
from .meta import Base

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime
)

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))


class SessionLogs(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    uid = Column(Text)
    url = Column(Text)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
