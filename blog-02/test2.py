#!/usr/bin/python

import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="12345")
    return conn

def get_column_names(connection,schema_name, table_name):
    """
    Returns a list of column names for a given table.
    """
    cur = connection.cursor()
    try:
    
        cur.execute("SELECT column_name,data_type FROM information_schema.columns WHERE table_schema = '%s' AND table_name = '%s';" % (schema_name, table_name))
        rows = cur.fetchall()
        cur.close()
        return rows

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    connection = connect()
    schema_name = 'public'
    table_name = 'demo_accounts'
    schema_name = 'public'
    column_names = get_column_names(connection,schema_name, table_name)
    print(column_names)


