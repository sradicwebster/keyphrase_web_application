import pytest
from keyphrases.db import get_db


def test_input(client, app):
    assert client.get('/keyphrase/input').status_code == 200
    response = client.post(
        '/keyphrase/input', data={'title': 'entry', 'text': 'some words'}
    )
    assert 'http://localhost/' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM documents WHERE title = 'entry'",
        ).fetchone() is not None


@pytest.mark.parametrize(('title', 'text', 'message'), (
    ('', '', b'Title is required'),
    ('test', '', b'Text is required'),
    ('test', 'some words', b'Title "test" is already used'),
))
def test_input_validate_input(client, title, text, message):
    response = client.post(
        '/keyphrase/input',
        data={'title': title, 'text': text}
    )
    assert message in response.data

