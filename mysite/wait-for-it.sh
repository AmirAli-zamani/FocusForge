import time
import psycopg2
from django.db import connections
from django.db.utils import OperationalError

def check():
    db_conn = None
    print("Waiting for database...")

    while not db_conn:
        try:
            db_conn = connections['default']
            c = db_conn.cursor()
        except OperationalError:
            print("Database unavailable, waiting 1 second...")
            time.sleep(1)

    print("Database is ready!" )
