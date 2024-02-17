FROM python:3.12-slim

WORKDIR /src

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y postgresql-client

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /src

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT "/entrypoint.sh"