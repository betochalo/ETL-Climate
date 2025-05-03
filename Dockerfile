FROM apache/airflow:slim-3.0.0-python3.9

COPY requirements.txt /opt/airflow/requirements.txt

USER root

RUN apt-get update \
    && apt-get install -y default-jdk \
    && mkdir -p /opt/airflow/scripts \
    && chown -R airflow: /opt/airflow/scripts

USER airflow

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

WORKDIR /opt/airflow

COPY --chown=airflow:airflow dags/ ./dags/
COPY --chown=airflow:airflow scripts/ ./scripts/

EXPOSE 8080