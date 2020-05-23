import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

#import nlp_model
from nlp_model import PublicationKeyPhrase

bp = Blueprint('keyphrases', __name__, url_prefix='/keyphrases')


@bp.route('/paste', methods=('GET', 'POST'))
def paste():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        db = get_db()
        error = None

        if not title:
            error = 'Title is required.'
        elif not text:
            error = 'Text is required.'

        publication = PublicationKeyPhrase(text)
        kp_list = publication.get_key_phrases()
        keyphrases = '\n'.join(kp_list)

        if error is None:
            db.execute(
                'INSERT INTO documents (title, text, keyphrases) VALUES (?, ?, ?)',
                (title, text, keyphrases) )
            db.commit()
            return redirect(url_for('index'))

        flash(error)

    return render_template('keyphrases/paste.html')
