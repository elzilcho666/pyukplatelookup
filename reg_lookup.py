#/usr/bin/python
import sys
import sqlite3
regDB = sqlite3.connect('UK_prefixes.db')
reg = sys.argv[1]
region = (reg[:2],)
cur = regDB.cursor()
cur.execute("select * from Reg_current where prefix =?", region)
row = cur.fetchone()
print "Car registered at %s, %s" % (row[1], row[2])
if int(reg[-2:]) > 50:
	year = str(int(reg[-2:]) - 49)
	prevyear = str(int(year) - 1)
	if len(year) == 1:
		year = "0" + year
		prevyear = "0" + prevyear
	print "The car was registered between 1st September 20%s and 28th/29th Febuary 20%s" % (prevyear, year)
else:
	year = reg[-2:]
	print "The car was registered between 1st March and 31st August 20%s" % (year)
#for row in rows:
#	print "Car registered in %s, %s" % (row['city'], row['region'])

