import psycopg2

conn = psycopg2.connect(
    database='persondb',
    user='postgres',
    password='Nikhil#1008',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

sql_query = ("SELECT dept, COUNT(emp_id) FROM employees GROUP BY dept ORDER BY dept ASC")
cur.execute(sql_query)
result = cur.fetchall()

for i in result:
    print(i)

cur.close()
conn.close()

