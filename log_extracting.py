import re
import os
import MySQLdb
import binascii

print("Connecting ...")
conn = MySQLdb.connect(host='localhost', user='ben', passwd='password1!', db='ben') # User setup for SQL database
cur = conn.cursor()

regex = re.compile(r"^\w{3} (\d{2})\/(\d{2})\/(\d{2}) ([^\s]+) \[[^\[]+\[(\d+):[^:]+:([^\]]+)]: (.*) \(0x8([^\)]+)\) ([^\]]+)")     #Regex expression, finding the Strings

count = 0

print("Searching for files ...")

for file in os.listdir('./log_files'):                  #Searching for file: log_files in the directory
	with open(file, 'r') as f:                          #opens the file
		for line in f:
			match = regex.match(line)                   #matching the regex 
			if match:

				time = '20' + match.group(3) + '-' + match.group(2) + '-' + match.group(1) + ' ' + match.group(4) 

				args = (time, match.group(5),match.group(6), match.group(7), int(match.group(8), 16), binascii.unhexlify(match.group(9)))
				cur.execute("INSERT INTO ben.modbus_frames (TIMESTAMP, IMEI, ASSET_NAME, FRAME_TYPE, POLL_CMD_ID, DATA) VALUES (%s, %s, %s, %s, %s, %s)", args) # insert format and data types for SQL database.
				count += 1

conn.commit()            #saves changes

print("Saving Changes ...")

conn.close()             #closes database.db

print('Inserted ', count, ' rows') # displays the number of rows extracted
