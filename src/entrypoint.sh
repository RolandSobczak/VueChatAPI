#!/bin/sh

python -m uvicorn backend.main:app --reload --host 0.0.0.0
