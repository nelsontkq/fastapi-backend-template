FROM tiangolo/uvicorn-gunicorn:python3.11 as backend

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
WORKDIR /

COPY ./api /api

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]