import MySQLdb
import sys

db=MySQLdb.connect(host="localhost",user="root",passwd="password", db="salesi")

cur=db.cursor()

cur.execute("SELECT info.name,info.tele FROM transaction JOIN info ON transaction.name=info.name WHERE status='"+sys.argv[1]+"'")

print sys.argv[1]+" Cases:"
print "Customer Name | Customer Tele"
for row in cur.fetchall():
	print row[0]+"  |  "+row[1]

db.close
