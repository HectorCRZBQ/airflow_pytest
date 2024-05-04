# Imagen que vamos a usar
FROM apache/airflow:2.2.0

# Usuario que vamos a usar
USER root

# Instalar la imagen
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

# Usuario que vamos a usar
USER airflow