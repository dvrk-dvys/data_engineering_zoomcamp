import sys

import pandas as pd

print(sys.argv)
day = sys.argv[1]

#some fancy pandas stuff like loading a csv file

print(f'job finished successfully for day = {day}!')





# How to set up a docker:
# open -a Docker   ## or open the application manually

# to view all recently made images:
#  docker images

# you can rebuild it. the name is test:
# docker build -t test:pandas .

# this code takes in a sys argument:
#docker run -it test:pandas 2025-04-18

# notebook convert the data upload from csv to pg to a python script not just a jupyter notebook
#❯ jupyter nbconvert --to=script upload-data.ipynb                            ─╯