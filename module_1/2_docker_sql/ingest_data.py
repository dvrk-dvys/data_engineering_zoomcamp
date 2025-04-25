#!/usr/bin/env python
# coding: utf-8

import argparse
import os
from time import time

import pandas as pd
from sqlalchemy import create_engine



def main(params):
    user = params.username
    password = params.password
    host = params.host
    port = params.port
    database = params.db
    table_name = params.table_name
    csv_url = params.csv_url

    csv_name = 'output.csv.gz'

    os.system(f'wget {csv_url} -O {csv_name}')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    engine.connect()

    df_iter = pd.read_csv(csv_name, compression='gzip', iterator=True, chunksize=100000)
    df = next(df_iter)
    print(pd.io.sql.get_schema(df, name=table_name, con=engine))

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    for df in df_iter:
        t_start = time()

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists='append')

        t_end = time()
        print('inserted another chunk..., it took %.3f seconds' % (t_end - t_start))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest csv data to postgres')

    parser.add_argument('--username', help='username for Postgres')
    parser.add_argument('--password', help='password for Postgres')
    parser.add_argument('--host', help='hostname or IP address of the Postgres server')
    parser.add_argument('--port', help='port number of the Postgres server')
    parser.add_argument('--db', help='name of the Postgres database')
    parser.add_argument('--table_name', help='name of the target table in the database')
    parser.add_argument('--csv_url', help='URL to the CSV file')

    args = parser.parse_args()
    #print(args.accumulate(args.integers))
    main(args)


# How to set up a docker:
# open -a Docker   ## or open the application manually

# to view all recently made images:
#  docker images

# you can rebuild it. the name is test:
# docker build -t test:pandas .

# this code takes in a sys argument:
#docker run -it test:pandas 2025-04-18

# notebook convert the data upload from csv to pg to a python script not just a jupyter notebook
#❯ jupyter nbconvert --to=script upload-data.ipynb


#docker build -t texi:ingest_v001 .