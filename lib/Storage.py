from datetime import *  
import MySQLdb
import time  
import os

DBHOST = 'dbhost'
DBUSER = 'user'
DBPASSWD = 'passwd'
DBNAME = 'name'

def todb(fname):
	errormsg = 'everything ok'
	try:
		f = open(fname,"r")
		conn = MySQLdb.connect(host=DBHOST,user=DBUSER,passwd=DBPASSWD,db=DBNAME,charset="utf8")
		cur = conn.cursor()
		sql = """CREATE TABLE `%s` (city VARCHAR(255),weather VARCHAR(45),aqi VARCHAR(255),humidity VARCHAR(45),temperature VARCHAR(255),wind_direction VARCHAR(255),wind_scale VARCHAR(255))""" % (date0s)
		cur.execute(sql)
		i = 0
		weather = f.readline()
		while weather:
			i = i + 1
			weather_list = weather.split(' ')
			del weather_list[1]
			sql = "insert into `%s`(`city`,`weather`,`aqi`,`humidity`,`temperature`,`wind_direction`,`wind_scale`)values('%s','%s','%s','%s','%s','%s','%s')"%(date0s,weather_list[0],weather_list[1],weather_list[2],weather_list[3],weather_list[4],weather_list[5],weather_list[6])
			cur.execute(sql)
			weather = f.readline()
		conn.commit()
		cur.close()
		conn.close()
		f.close()
		errormsg = 'success!'

	except Exception as e:
		errormsg = 'ouch!'
		raise e
	finally:
		return errormsg



def main():
	pass

if __name__ == '__main__':
	main()