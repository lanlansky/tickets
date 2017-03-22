# -*- coding:utf-8 -*-
import re
import requests
from pprint import pprint
def run():
	url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
	#verify=False 表示不验证证书
	response=requests.get(url,verify=False)
	#print(response.text)
	#response.encoding = 'utf-8'
	stations=re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
	pprint(dict(stations),indent=4)
if __name__=='__main__':
	run()