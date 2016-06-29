import sys
import MySQLdb

# This is the line to connect to our MYSQL
db=MySQLdb.connect(host="localhost",user="root",passwd="password",db="salesi")

#you must create a Cursor object. It will let
# you execute all the queries you need
cur=db.cursor()

cur.execute("SELECT * FROM info")

for row in cur.fetchall():
	print row

f=open("data.csv","r")

for line in f:
	line=line.strip('\n').strip('\r')
	entry=line.split(',')
	print entry