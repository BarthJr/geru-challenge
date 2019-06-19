from cornice import Service
from pyramid.httpexceptions import HTTPOk, HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from quotes_api.models.models import DBSession, SessionLogs
from quotes_api.views.api.schema import SessionLogsSchema, session_schema

session = Service(name='session', path='api/v1/sessions')
session_by_uid = Service(name='session_by_uid', path='api/v1/sessions/{uid}')


@session.get(schema=SessionLogsSchema, content_type='application/json')
def get_sessions(request):
    try:
        sessions = DBSession().query(SessionLogs).all()
        return HTTPOk(json=session_schema.dump(sessions).data)
    except NoResultFound:
        return HTTPNotFound()


@session_by_uid.get(schema=SessionLogsSchema, content_type='application/json')
def get_session_by_uid(request):
    try:
        uid = request.matchdict.get('uid')
        session_uid = DBSession().query(SessionLogs).filter_by(uid=uid)
        return HTTPOk(json=session_schema.dump(session_uid).data)
    except NoResultFound:
        return HTTPNotFound()
