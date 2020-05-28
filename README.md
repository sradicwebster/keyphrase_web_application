# Key phrase extractor web application
University of Bristol Interactive AI CDT first year individual project to construct a web application around an NLP model, applying good software engineering practices.

The Python web framework Flask was used to construct an application around an NLP model that was developed to extract key phrases from scientific publications.

# To run on Linux or Mac
Download: keyphrases-1.0.0-py3-none-any.whl and in the directory create a virtual environment and install using pip
```sh
$ python3 -m venv venv
$ pip install keyphrases-1.0.0-py3-none-any.whl
$ export FLASK_APP=keyphrases
$ flask init-db
$ flask run
```





