#!/bin/bash


cd "$(dirname "$0")"
cd ./application
awhile=3
sleep $awhile && open http://localhost:8000/ &
python manage.py runserver
