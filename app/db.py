# app/db.py
import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="compliance_search",
        user="taelaptop",
        password=""  # leave empty if no password
    )
    return conn
