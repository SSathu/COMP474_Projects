#!/bin/bash
exec fastapi run app/main.py --port 80
EXPOSE 80
