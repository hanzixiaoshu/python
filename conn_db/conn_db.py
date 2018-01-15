#!/usr/bin/env python
import MySQLdb

conn = MySQLdb.connect(host='', port=3306, user='', passwd='', db='')
cur = conn.cursor() #获取游标
ss =cur.execute("select * from")
info = cur.fetchmany(ss)
for i in info:
    print i
    
cur.close()
conn.commit()
conn.close()
