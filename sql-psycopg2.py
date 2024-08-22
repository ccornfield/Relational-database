import psycopg2


connection = psycopg2.connect(database="chinook", host="localhost",port=5432,user="postgres",password="1234")

cursor = connection.cursor()

cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Nando Reis"])

results = cursor.fetchall()

connection.close()

for result in results:
    print(result)