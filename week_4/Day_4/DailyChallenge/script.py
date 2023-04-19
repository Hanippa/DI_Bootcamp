# Instructions

#     Using this API, create the functionality which will write 10 random countries to your database.

#     These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

import requests
import json
import psycopg2
import random

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '2144'
DATABASE = 'countries'


connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )


def run_change_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

x = requests.get('https://restcountries.com/v3.1/all')
y = x.json()

for i in range(10):
    num = random.randint(0, 249)
    run_change_query(f"""INSERT INTO countries (name, capital, flag, subregion, population) VALUES  (
                                                                                                     '{y[num]["name"]["common"]}',
                                                                                                     '{y[num]["capital"][0]}',
                                                                                                     '{y[num]["flag"]}',
                                                                                                     '{y[num]["subregion"]}',
                                                                                                     {y[num]["population"]}
                                                                                                     )""")
