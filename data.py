import sys

f=open("data.csv","r")
runningTotal=0
runningPaid=0
runningBalance=0


for line in f:
	line=line.strip('\n').strip('\r')
	entry=line.split(',')
	try:
		runningTotal += int(entry[2])
		runningPaid += int(entry[3])
		runningBalance += int(entry[4])
	except:
		pass
	
print "Total Cost = " + str(runningTotal) 
print "Total Paid = " + str(runningPaid)
print "Total Balance = " + str(runningBalance)

f.seek(0)
for line in f:
	line=line.strip('\n').strip('\r')
	entry=line.split(',')
	if entry[5]=="pending":
		print "Clients " + entry[1] + " are pending"

f.close

