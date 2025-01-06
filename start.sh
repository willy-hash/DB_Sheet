#!/bin/bash
gunicorn app:App --bind=0.0.0.0:$PORT