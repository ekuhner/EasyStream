import datetime
import os
import streamlit as st
import sqlite3 
from psycopg2 import sql
from connect import pconnect
 
class scoload_config:
    sqlite_file = None
    cliente = None
    sqlite_filename = None
    def __init__(self):
        
        st.title("Easy Ativos")
        st.write(
            "Aguarde enquanto montamos o ambiente..."
        )
        st.progress(1)

    def post_connect(self):
        """Post connection to the database"""

        st.header("Conectando ao banco de dados...")
        config = pconnect().load_config()
        pconn = pconnect().connect(config)

    def file_selector(self):
        filenames = []
        filepath= os.path.join(os.getcwd(), "sqlite")
        filenames = os.listdir(filepath)
        selected_filename = st.selectbox('Select a SQLITE database', filenames)
        self.sqlite_filename =  os.path.join(filepath, selected_filename)
    
    def load_sqlite(self):
        
        conn = sqlite3.connect(self.sqlite_filename)
        cursor = conn.cursor()
        rows = cursor.execute("SELECT count(*) conta FROM ativo")
        st.subheader(f"Quantidade de ativos {rows.fetchone()[0]}")
        conn.close()

    def main(self):
        self.file_selector()
        
        self.cliente = self.sqlite_filename.split("_")[1]
        self.load_sqlite()
        self.post_connect()
        
        
        #self.load_config()
        st.progress(100)
        st.success(f"Conectado ao banco de dados de {self.cliente} ")
        
if __name__ == "__main__":
    scoload_config().main()


