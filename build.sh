#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt_tab'); nltk.download('stopwords')"
