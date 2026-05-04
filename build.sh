#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt
python -m nltk.downloader -d ./nltk_data punkt punkt_tab stopwords
