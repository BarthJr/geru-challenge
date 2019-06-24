from os.path import join, dirname

import pytest
from pyramid import paster
from webtest import TestApp

from quotes_api import main


@pytest.fixture(scope='session')
def app(request):
    settings = paster.get_appsettings(join(dirname(__file__), '../../../testing.ini'))

    app = main(settings.global_conf, **settings)
    test_app = TestApp(app)

    return test_app
