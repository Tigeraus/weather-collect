# -*- coding:utf-8 -*-
# 03/12/2015


import lib.weathquery as wq
import os
from BeautifulSoup import BeautifulSoup  
import json
import requests
import time 


html = open('cityid.html','r')
#cityfile = open('cityid.txt','w')
soup = BeautifulSoup(''.join(html))
#print soup.prettify()

CityList = []


CitySum = soup.findAll('p',style="text-align:left;")

for city in CitySum:
	if city.string:
		#print city.string
		print city.string[:9].encode('utf-8')
		print city.string[10:].encode('utf-8')
		e = city.string[:9].encode('utf-8')
		CityList.append(e)
	else:
		pass

print CityList




print len(CityList)


def SearchWeather():
	CityDict = {}
	for i in range(len(CityList)):
		cityw = wq.CityWeather()
		CityId = CityList[i]
		print type(CityId)
		cityw = wq.getWeather(CityId)
		print cityw
		e = {cityw.name: cityw}
		CityDict.update(e)
	return CityDict

def StorageWeather(CityDict):
	now = time.localtime(time.time())
	rightnow = time.strftime("%Y-%m-%d",now)
	f = open('weather'+rightnow+'.txt','w')
	for city in CityDict:
		cityinfo = CityDict.get(city)
		f.write(cityinfo.name+' '+cityinfo.date+' '+cityinfo.weather+' '+str(cityinfo.longitude)+'; '+str(cityinfo.latitude)+' '+str(cityinfo.low_tmp)+'&deg;C' + str(cityinfo.high_tmp)+'&deg;C'+' '+cityinfo.wd+' '+cityinfo.ws+'\n')
	f.close()



if __name__ == '__main__':
        BASE_DIR = os.path.dirname(__file__)
        print BASE_DIR
	t0 = time.time()
	dict = SearchWeather()
	t1 = time.time()
	print 'Time we used to search the weather: ' + str(t1-t0) + ' Seconds'
	StorageWeather(dict)
	t2 =time.time()
	print 'Time we used to search the weather: ' + str(t2-t1) + ' Seconds'