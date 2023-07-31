from idlelib import query

import psycopg2

# connect to db
conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='******')
try:
    with conn:
        with conn.cursor() as cur:
            # execute query
            cur.execute("INSERT INTO user_account VALUES (%s, %s)", (7, 'Gill'))
            cur.execute("SELECT * FROM user_account")

            rows = cur.fetchall()
            print(rows)
            for row in rows:
                print(row)

finally:
    conn.close()
