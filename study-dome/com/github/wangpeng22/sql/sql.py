import pymysql

db = pymysql.connect(host='47.110.39.144', user='root', passwd='db.W.104756~', db='mysql')

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print("Database version : %s " % data)

db.close()


