import mysql.connector
import streamlit as st
from langchain_helper import get_few_shot_db_chain
import pandas as pd
# import sqlite3
import mysql

def get_table():
    db_user = "root"
    db_password = "root"
    db_host = "localhost"
    db_name = "atliq_tshirts"
    conn = mysql.connector.connect(host=db_host,
            user=db_user,
            passwd=db_password,
            database=db_name)
    # conn = sqlite3.connect(database='database/conver')
    # c = conn.cursor()
    # with open('database/db_creation_atliq_t_shirts.sql', 'r') as f:
    #     sqlfile = f.read()
    # sqlCommands = sqlfile.split(';')

    # for command in sqlCommands:
    #     try:
    #         c.execute(command)
    #     except OperationalError as e:
    #         print("Command skipped: ", e)
    # print(conn.execute("SELECT * FROM t_shirts;"))
    return pd.read_sql("SELECT * FROM t_shirts LIMIT 10;", con=conn)

st.title("Chat with Database Using Langchain")

st.dataframe(get_table(), width=1200, height=210)

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)






