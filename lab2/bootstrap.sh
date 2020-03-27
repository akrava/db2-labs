#!/bin/bash

cd "$(dirname "$0")"

if ! pgrep -x "redis-server" >/dev/null; then
    echo "please, install redis-server"
    exit 1
fi

if [[ ! -f .env ]]; then
    cp  .env.example .env
fi

pipenv install --dev

if [[ $# -eq 1 ]] && ([[ $1 = "--cui" ]] || [[ $1 = "--worker" ]]); then
     pipenv run python src/main.py $1
elif [[ $# -eq 3 ]] && [[ $1 = "--simulate" ]]; then
     pipenv run python src/simulation.py $2 $3
else
    echo "No arguments supplied. Need --cui or --worker"
    exit 1
fi
