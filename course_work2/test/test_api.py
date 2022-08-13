from run import app


def test_app():
    response = app.test_client().get('/', follow_redirects=True)
    assert response.status_code == 200


def test_api():
    response = app.test_client().get('/api/posts', follow_redirects=True)
    assert type(response.json) == list, 'not list'


def test_api_id():
    params = [1, 2, 3, 5, 6, 100]
    for i in params:
        response = app.test_client().get(f'/api/posts/{i}')
        assert response.status_code == 200, 'error'
