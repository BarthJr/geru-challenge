from http import HTTPStatus


def test_get_sessions(app):
    response = app.get('/api/v1/sessions', status=HTTPStatus.OK)
    assert response.status_code == HTTPStatus.OK


def test_get_session_by_uid(app):
    response = app.get('/api/v1/sessions/14a27b92-3ddb-44aa-acbf-379518853b69', status=HTTPStatus.OK)
    assert response.status_code == HTTPStatus.OK
