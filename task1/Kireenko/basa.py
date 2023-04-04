import psycopg2
import t1

connection = psycopg2.connect(host='localhost', dbname='data', user='postgres', password='Q1w2e3r4')
cursor = connection.cursor()
data = t1.main()

for book in data:
    place, name, author, format = book.split("|")
    inser_qwery = f"""INSERT INTO public.user_table
              (id, name, author, format)
              VALUES ('{place}', '{name}','{author}', '{format}');"""
    cursor.execute(inser_qwery)
    connection.commit()