import sys
import MySQLdb

# This is the line to connect to our MYSQL
db=MySQLdb.connect(host="localhost",user="root",passwd="password",db="salesi")

#you must create a Cursor object. It will let
# you execute all the queries you need
cur=db.cursor()

f=open("data.csv","r")

for line in f:
	if line.startswith('date'):
		pass
	else:
		line=line.strip('\n').strip('\r')
		entry=line.split(',')
		print entry
		
		query="INSERT INTO transaction(date,name,cost,paid,balance,status) VALUES ('"+entry[0]+"','"+entry[1]+"','"+entry[2]+"','"+entry[3]+"','"+entry[4]+"','"+entry[5]+"')"
		
		print query

		cur.execute(query)
		db.commit()

