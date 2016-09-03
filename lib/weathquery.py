# -*- coding:utf-8 -*-
# basic datas structure of city's weather
# basic operation of weather
# 03/12/2015




import json
import requests
import time

class CityWeather(object):
	""" 
	Describe the basic CityWeather

	"""
	def __init__(self):
		name = ' '
		date = ' '
		weather = ' '
		longitude = 0
		latitude = 0
		low_tmp = 0
		high_tmp = 0
		wd = ' '
		ws = ' '
	def __str__(self):
		repinfo =  'name: '+str(self.name)+'\n'+'date: '+str(self.date)+'\n'+str(self.weather)+'\n'+str(self.longitude)+':'+str(self.latitude)+'\n'+str(self.low_tmp)+' -> '+str(self.high_tmp)+'\n'+str(self.wd)+'\n'+str(self.ws)
		return repinfo

	def __repr__(self):
		return str(self)




def queryweather(cityid):   # the type of cityid 
	cw = CityWeather()

	url = "http://a.apix.cn/apistore/weatherservice/cityid"
	querystring = {"cityid":cityid}  # string
	headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apix-key': "806b1cf735614df172466e273d33089f"
    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	res = json.loads(response.text)


	info = res['retData']
	cw.name = info['city'].encode('utf-8')
	cw.date = info['date'].encode('utf-8')
	#print cw.name
	cw.longitude = info['longitude']
	cw.latitude = info['latitude']
	#print '经度:' + str(cw.longitude) + ' 纬度:' + str(cw.latitude)
	cw.weather = info['weather'].encode('utf-8')  #unicode 
	#print '天气:' + cw.weather
	cw.low_tmp = info['l_tmp'].encode('utf-8')
	cw.high_tmp = info['h_tmp'].encode('utf-8')
	cw.wd = info['WD'].encode('utf-8')
	cw.ws =  info['WS'].encode('utf-8')
	#print ((response.text).encode('utf-8'))
	return cw

def getWeather(cityid):
	try:
		cw = queryweather(cityid)
		return cw
	except :
		print 'Sorry but error happend'
		cw = CityWeather()
		cw.name = 'error'
		cw.date = 'error'
		cw.weather = 'error'
		cw.longitude = 1000
		cw.latitude = 1000
		cw.low_tmp = 1000
		cw.high_tmp = 1000
		cw.wd = 'errpr'
		cw.ws = 'error'
		return cw
	finally:
		print 'Done...'

if __name__ == '__main__':
	wangjiang = "101021300"
	#susong =  "88980809"
	t0 = time.time()
	#x2 = queryweather(wangjiang)
	x1 = getWeather(wangjiang)
	t1 = time.time()
	print 'Time we used: ' + str(t1-t0) + ' Seconds'
	print x1
	#queryweather(wangjiang)









