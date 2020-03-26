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

if [[ $# -eq 1 ]] && ([[ $1 = "--cui" ]] || [[ $1 = "--worker" ]]); then
    python src/main.py $1
elif [[ $# -eq 3 ]] && [[ $1 = "--simulate" ]]; then
    python src/simulation.py $2 $3
else
    echo "No arguments supplied. Need --cui or --worker"
    exit 1
fi
