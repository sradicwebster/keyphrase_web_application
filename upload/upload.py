from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from nlp_model import PublicationKeyPhrase

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/key_phrase', methods=['GET','POST'])
def get_key_phrase():

    text = request.files['file']
    text.save(secure_filename('/input.txt'))

    with open('input.txt', "r") as f:
        text = f.read().splitlines()[0]

    publication = PublicationKeyPhrase(text)
    key_phrases = publication.get_key_phrases()
    output = {i + 1: key_phrases[i] for i in range(len(key_phrases))}

    return render_template("result.html",result = output)




'''
    return redirect(url_for('predict'))

@app.route('/predict', methods=['POST'])
def prediction():
    with open('amber.txt', "r") as f:
        text = f.read().splitlines()[0]

    publication = PublicationKeyPhrase(text)
    key_phrases = publication.get_key_phrases()
    output = {i+1: key_phrases[i] for i in range(len(key_phrases))}

    return output
'''

if __name__ == '__main__':
    app.run(debug=True)