#!/usr/bin/env bash
# Setup Python environment
set -e
set -x

python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip

pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m spacy download de_core_news_sm
python -m spacy download de_core_news_md

set +x
set +e