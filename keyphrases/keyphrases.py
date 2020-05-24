import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db
from nlp_model import PublicationKeyPhrase

bp = Blueprint('keyphrases', __name__, url_prefix='/keyphrases')

@bp.route('/paste', methods=('GET', 'POST'))
def paste():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        db = get_db()
        error = None
        if not text:
            error = 'Text is required.'
        elif db.execute(
            'SELECT id FROM documents WHERE title = ?', (title,)
        ).fetchone() is not None:
            error = f'Title "{title}" is already used'

        if error is None:
            publication = PublicationKeyPhrase(text)
            kp_list = publication.get_key_phrases()
            number_of_kp = len(kp_list)
            keyphrases = '\n'.join(set(kp_list))

            db.execute(
                'INSERT INTO documents (title, text, keyphrases, kp_count) VALUES (?, ?, ?, ?)',
                (title, text, keyphrases, number_of_kp) )
            db.commit()
            return redirect(url_for('index'))

        flash(error)

    return render_template('keyphrases/paste.html')
