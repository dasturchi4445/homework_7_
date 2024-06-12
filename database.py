import os
import psycopg2
from dotenv import load_dotenv

load_dotenv


class Database:
    @staticmethod
    def connect(query: str, query_type: str, psql=str) -> list or str:
        db = psql.connect(
            database=os.getenv('db_name'),
            user=os.getenv('db_user'),
            host=os.getenv('db_host'),
            password=os.getenv('db_password'),
            port=os.getenv('db_post')
        )
        cursor = db.cursor()
        data = ['insert', 'delete', 'alter']
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == 'insert':
                return "inserted data"

        else:
            return cursor.fetchall()
