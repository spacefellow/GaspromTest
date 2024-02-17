#!/bin/bash

PGPASSWORD=$POSTGRES_PASSWORD psql --host ${POSTGRES_HOST} -U ${POSTGRES_USER} -W -c "CREATE DATABASE gasprom_test;"
alembic upgrade head
python dbinit.py
uvicorn run:app --host 0.0.0.0 --port 8000