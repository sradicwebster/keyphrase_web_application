import os
import tempfile

import pytest
from keyphrases import create_app
from keyphrases.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class InputActions(object):
    def __init__(self, client):
        self._client = client

    def input(self, title='test', text='test'):
        return self._client.post(
            '/keyphrase/input',
            data={'title': title, 'text': text}
        )

@pytest.fixture
def input_test(client):
    return InputActions(client)