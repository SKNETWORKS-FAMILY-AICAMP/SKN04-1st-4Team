# pip install psycopg2

import psycopg2
import streamlit as st
import pandas as pd
import numpy as np

import requests
from PIL import Image
from io import BytesIO
import IPython.display as display
import json

with psycopg2.connect(
    host='192.168.0.87',
    dbname='postgres',
    user='postgres',
    password='qksrkqek12',
    port=8874
    )as conn:
        with conn.cursor() as cur:
                cur.execute('SELECT * FROM project1.faq;')
                result_one = cur.fetchone() # READ
                result_many = cur.fetchmany() 
                result_all = cur.fetchall()


result_one = [result_one]
result_all = list(result_all)
result_one.extend(result_many)
result_one.extend(result_all)
result_all = result_one

st.title('FAQ')

tab1, tab2 = st.tabs(['Kia', 'En_coe'])
num1, num2 = 0, 0
for i in range(60):
    if result_all[i][0] == 'kia':
        num1 += 1
        with tab1:
            expander = st.expander(f"Q.{num1}\t" + result_all[i][1])
            expander.write(result_all[i][4])
            if result_all[i][3] != 'None':
                expander.image(result_all[i][3])
    else:
        num2 += 1
        with tab2:
            expander = st.expander(f"Q.{num2}\t" + result_all[i][1])
            expander.write(result_all[i][4])
            if result_all[i][3] != 'None':
                expander.image(result_all[i][3])