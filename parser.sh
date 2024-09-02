#!/usr/bin/env bash

source ./venv/bin/activate
python3 parser.py https://netospace.ru/drive/d/s/zr6nlE5FI9aNM96YG7v9C0BBJ2cSnYdf/U7yj3Po4cSeCqJYmwrzuQkI1WHwMsqV7-Pb4gmWwEnws sh_2 timetable.ics
mkdir -p ./public/c
mv *.ics ./public/c