import psycopg2
import pandas as pd
conn = psycopg2.connect(
    host="localhost",
    dbname="persondb",
    user="postgres",
    password="Nikhil#1008",
    port="5432"
)

# to execute the postgresql commands
cur = conn.cursor()

sql_query = """SELECT dept, COUNT(dept) FROM employees 
               GROUP BY dept;
            """

cur.execute(sql_query)

result = cur.fetchall()
for item in result:
    print(item)

conn.commit()
cur.close()
conn.close()



df = pd.Series(result, name='Departments')
print(df)