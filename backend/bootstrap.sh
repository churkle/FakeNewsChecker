#!/bin/sh
export FLASK_APP=./fakenewschecker/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0