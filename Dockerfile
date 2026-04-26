FROM python:3.12-slim

WORKDIR /app

COPY tcp /app/tcp

CMD ["python", "-u", "tcp/tcp_server.py"]
