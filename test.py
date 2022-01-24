#!/usr/bin/python

import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def get_column_names(schema_name, table_name):
    """
    Returns a list of column names for a given table.
    """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = '%s' AND table_name = '%s' ORDER BY ordinal_position;" % (schema_name, table_name))
        rows = cur.fetchall()
        column_names = [row[0] for row in rows]
        cur.close()
        return column_names
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect()
    schema_name = 'public'
    table_name = 'demo_accounts'
    schema_name = 'public'
    column_names = get_column_names(schema_name, table_name)
    print(column_names)


