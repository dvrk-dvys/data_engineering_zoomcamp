FROM python:3.9

RUN apt-get update && apt-get install -y wget
RUN pip install pandas
RUN pip install sqlalchemy
RUN pip install psycopg2


WORKDIR /app
# destination working directory path
COPY ingest_data.py ingest_data.py
# name of file on host machine and then the name of file on the destination

#ENTRYPOINT [ "bash" ]
ENTRYPOINT [ "python", "ingest_data.py" ]