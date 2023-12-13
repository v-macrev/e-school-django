# Using the full Python 3.10 image
FROM python:3.10-slim

EXPOSE 8000

# Install necessary packages and generate locale
RUN apt-get update && apt-get install -y git\
    gcc \
    default-libmysqlclient-dev \
    libpq-dev \
    pkg-config \


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /apps

COPY . /apps

# Run Django management commands
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /apps
USER appuser

# During debugging, this entry point will be overridden. 
# For more information, please refer to https://aka.ms/vscode-docker-python-debug
# The gunicorn worker is set to 'threads' and the number of threads per worker is set to 4 for multithreading.
CMD ["/start.sh", "gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "3600", "--workers", "9", "--worker-class", "gevent", "--keep-alive", "5",  "--log-level", "info", "--access-logfile", "-", "core.wsgi"]
