#!/bin/bash
gunicorn App:app --bind=0.0.0.0:$PORT