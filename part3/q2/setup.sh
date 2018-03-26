#!/usr/bin/env bash

if [ ! -d .env ]; then
    virtualenv .env -p python2
fi

source .env/bin/activate
pip install -r requirements.txt
