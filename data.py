from BeautifulSoup import BeautifulSoup  
import json
import requests
import os

import time
#
class CA:
	a='2'
	b='3'

A = CA()
B = CA()
C = CA()
dict={11:A,22:B,33:C}


f = open('test.txt','w')
for i in dict:
	item =  dict.get(i)
	f.write(str(item))



now = time.localtime(time.time())
print time.asctime(now)
print type(time.strftime("%Y-%m-%d",now))


def asdf():
	return 3

x= asdf() 