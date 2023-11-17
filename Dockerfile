FROM python:3.8
RUN apt update && apt install -y && python -m pip install --upgrade pip
RUN pip install fastapi uvicorn pymongo requests
