import re
import os
import MySQLdb
import binascii

print("Connecting ...")
conn = MySQLdb.connect(host='localhost', user='ben', passwd='password1!', db='ben')
cur = conn.cursor()

cur.execute("SELECT data FROM ben.modbus_frames")

rows = cur.fetchall()

for row in rows:
    # print(bytearray(row).hex())
    print (binascii.hexlify(row[0]))


cur.close()
