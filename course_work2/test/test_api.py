from run import app


def test_app():
    response = app.test_client().get('/', follow_redirects=True)
    assert response.status_code == 200


def test_api():
    response = app.test_client().get('/api/posts', follow_redirects=True)
    assert type(response.json) == list, 'not list'


def test_api_id():
    params = {"pk": 1}
    response = app.test_client().get('/api/posts/', query_string=params)
    assert type(response.json) == dict, 'not dict'
