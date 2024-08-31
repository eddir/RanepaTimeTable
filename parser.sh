#!/usr/bin/env bash

source ./venv/bin/activate
python3 parser.py
mkdir -p ./public/c
mv *.ics ./public/c