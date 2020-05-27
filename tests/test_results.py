import pytest
from keyphrases.db import get_db


def test_index(client, input_test):
    input_test.input()
    response = client.get('/')
    assert b'test title' in response.data
    assert b'Upload New' in response.data
    assert b'View' in response.data
    assert b'1 keyphrases' in response.data



@pytest.mark.parametrize('path', (
    '/1/view',
    '/1/delete',
))

def test_view(client, input_test, path):
    input_test.input()
    assert client.get('/1/view').status_code == 200


def test_delete(client, input_test, app):
    input_test.input()
    response = client.post('/1/delete')
    assert response.headers['Location'] == 'http://localhost/'

    with app.app_context():
        db = get_db()
        documents = db.execute('SELECT * FROM documents WHERE id = 1').fetchone()
        assert documents is None
