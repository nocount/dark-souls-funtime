import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',passwd='Fr0ntranger')

cursor = conn.cursor()
#cursor.execute('CREATE DATABASE IF NOT EXISTS dark_souls')
cursor.execute('USE dark_souls')

#Creating weapon stats table in mysql
create_statement = ('CREATE TABLE IF NOT EXISTS weapon_stats ('
				'name VARCHAR(64),'
				'phys INT,'
				'magic INT,'
				'fire INT,'
				'lightning INT,'
				'total INT,'
				'weapon_category VARCHAR(64))')
# cursor.execute(create_statement)


cursor.execute('SELECT * FROM weapon_stats')
print(cursor.fetchall())
