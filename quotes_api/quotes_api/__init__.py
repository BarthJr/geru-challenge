from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import engine_from_config

from quotes_api.models.models import DBSession, Base


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    session_factory = SignedCookieSessionFactory('$2y$12$jBjDCKJ1lU8pLjJyzSnI5uDkul26WHyGvDiODF7xw0/5d4hQJLdn2')
    with Configurator(settings=settings, session_factory=session_factory) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
