import pytest
from keyphrases.db import get_db


def test_index(client):
    response = client.get('/')
    assert b'test' in response.data
    assert b'1 keyphrases' in response.data
    assert b'Upload New' in response.data
    assert b'View' in response.data


@pytest.mark.parametrize('path', (
    '/1/view',
    '/1/delete',
))

def test_view(client, path):
    assert client.get('/1/view').status_code == 200


def test_delete(client, app):
    response = client.post('/1/delete')
    assert response.headers['Location'] == 'http://localhost/'

    with app.app_context():
        db = get_db()
        documents = db.execute('SELECT * FROM documents WHERE id = 1').fetchone()
        assert documents is None
