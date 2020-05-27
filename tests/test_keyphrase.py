import pytest
from flask import g, session
from keyphrases.db import get_db


def test_input(client, app):
    assert client.get('/keyphrase/input').status_code == 200
    response = client.post(
        '/keyphrase/input', data={'title': 'a', 'text': 'a'}
    )
    assert 'http://localhost/' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM documents WHERE title = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('title', 'text', 'message'), (
    ('', '', b'Title is required.'),
    ('a', '', b'Text is required.'),
    #('test', 'test', b'Title "test" is already used'),
))
def test_input_validate_input(client, title, text, message, input_test):
    input_test.input()
    response = client.post(
        '/keyphrase/input',
        data={'title': title, 'text': text}
    )
    assert message in response.data


#def test_uploaded_texts(client, path):
#    response = client.post(path)
#    assert response.headers['Location'] == 'http://localhost/'