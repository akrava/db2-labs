#!/bin/bash

cd "$(dirname "$0")"

if ! pgrep -x "redis-server" >/dev/null; then
    echo "please, install redis-server"
    exit 1
fi

if [[ ! -d venv ]]; then
    virtualenv venv --python=python3.6
    source venv/bin/activate
    pipenv install --dev
else
    source venv/bin/activate
fi

python src/main.py
