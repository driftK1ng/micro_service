#!/bin/bash

sleep 20
alembic upgrade head
uvicorn app.main:app --host 0.0.0.0 --port 80
