FROM python:3.9-slim

ENV DAGSTER_HOME=/opt/dagster/dagster_home

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
COPY dagster_home /opt/dagster/dagster_home
COPY ecommerce_dema /opt/dagster/app/ecommerce_dema
COPY dbt /opt/dagster/app/dbt

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

WORKDIR /opt/dagster/app