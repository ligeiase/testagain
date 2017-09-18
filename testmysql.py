#!/usr/bin/python
#encoding=utf-8

import MySQLdb

db = MySQLdb.connect(host="dbhost",user="username",passwd="passwd",db="dbname",port=dbport)

cursor = db.cursor()
sqls = "SELECT user_id,from_ip,access_time from tl_smtp where to_days(access_time)=to_days(current_date())"

try:

        cursor.execute(sqls)
        results = cursor.fetchall()
        for row in results:
                userid = row[0]
                fromip = row[1]
                datetime = row[2]
                print "%s,%s,%s" % (userid,fromip,datetime)

except:
        print "ERROR"

cursor.close()
db.close()