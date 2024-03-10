import mysql.connector
import os
import dotenv
import hashlib

dotenv.load_dotenv('.././app.env')

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

config = {
  'user': DB_USER,
  'password': DB_PASSWORD,
  'host': DB_HOST,
  'database': DB_NAME
}

def hash_password(password):
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  return hashed_password

def insDB(query, values): 
  db = mysql.connector.connect(**config)
  cursor = db.cursor(dictionary=True)
  cursor.execute(query, values)
  db.commit()
  last_inserted_id = cursor.lastrowid
  cursor.close()
  db.close()
  return last_inserted_id

def selDB(query, values=None):
  db = mysql.connector.connect(**config)
  cursor = db.cursor(dictionary=True)
  result = cursor.execute(query, values)
  rows = cursor.fetchall()
  db.close()
  return rows