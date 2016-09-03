# coding: utf-8

from datetime import *  
import MySQLdb
import time  
import os

DBHOST = 'dbhost'
DBUSER = 'user'
DBPASSWD = 'passwd'
DBNAME = 'name'

# 请修改起始和截至日期
date0 = date(2016,3,22)
date3 = date(2016,5,22)


date1 = date(2010,04,06)  
date2 = date1.replace(day = 07)
delta = date2 - date1

while date0 != date3:
	date0s = date0.strftime('%Y-%m-%d') 
	fname = 'weather'+ date0s + '.txt'    

	conn = MySQLdb.connect(host=DBHOST,user=DBUSER,passwd=DBPASSWD,db=DBNAME,charset="utf8")
	cur = conn.cursor()
	sql = """CREATE TABLE `%s` (city VARCHAR(255),weather VARCHAR(45),aqi VARCHAR(255),humidity VARCHAR(45),temperature VARCHAR(255),wind_direction VARCHAR(255),wind_scale VARCHAR(255))""" % (date0s)
	cur.execute(sql)

	if os.path.exists(fname):
		f = open(fname,"r")
		e = f.read(1)
		if e != 'e':
			f = open(fname,"r")
			i = 0
			weather = f.readline()
			while weather:
				i+=1
				print(date0,i)
				weather_list = weather.split(' ')
				del weather_list[1]
				sql = "insert into `%s`(`city`,`weather`,`aqi`,`humidity`,`temperature`,`wind_direction`,`wind_scale`)values('%s','%s','%s','%s','%s','%s','%s')"%(date0s,weather_list[0],weather_list[1],weather_list[2],weather_list[3],weather_list[4],weather_list[5],weather_list[6])
				cur.execute(sql)
				weather = f.readline()
			conn.commit()
			cur.close()
			conn.close()

			f.close()
			date0 += delta
		else:
			date0 += delta
	else:
		date0 += delta

