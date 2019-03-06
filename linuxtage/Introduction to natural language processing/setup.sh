#!/usr/bin/env bash
# Setup Python environment
set -e
set -x

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

pip install -r requirements.txt
python -m spacy download en_core_web_sm

set +x
set +e