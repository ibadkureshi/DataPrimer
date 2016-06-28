import sys



personName=sys.argv[1]

print "Hello " + personName

tTab = int(sys.argv[2])

for i in range(1,11):
	print str(tTab) + " x " + str(i) + " = " + str(tTab*i)
