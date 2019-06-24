from http import HTTPStatus


def test_home(app):
    response = app.get('/', status=HTTPStatus.OK)
    assert response.status_code == HTTPStatus.OK


def test_get_quote(app):
    response = app.get('/quotes/1', status=HTTPStatus.OK)
    assert response.status_code == HTTPStatus.OK


def test_get_nonexistent_quote(app):
    response = app.get('/quotes/42', status=HTTPStatus.NOT_FOUND)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_all_quotes(app):
    response = app.get('/quotes', status=HTTPStatus.OK)
    assert response.status_code == HTTPStatus.OK


def test_get_random_quote(app):
    response = app.get('/quotes/random/', status=HTTPStatus.OK)
    assert response.status_code == HTTPStatus.OK
