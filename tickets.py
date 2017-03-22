# -*- coding:utf-8 -*-
"""Usage:
  tickets.py [-gdtkz] <from> <to> <date>
  tickets.py -h | --help | --version
Options:
  -g 	高铁
  -d 	动车
  -t 	特快
  -k 	快速
  -z 	直达
"""
from docopt import docopt
from stations import stations
import requests
import json
from collections import OrderedDict
import formatResult
_author_='lhw'
#docopt  格式化命令
#去除警告
requests.packages.urllib3.disable_warnings()
def cli():
	arguments = docopt(__doc__)
	#print(arguments)
	from_station=stations.get(arguments['<from>'])
	to_station=stations.get(arguments['<to>'])
	date=arguments['<date>']
	#print(from_station,to_station,date)
	#构建查询的URL
	url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,from_station,to_station)
	#url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+date+'&leftTicketDTO.from_station='+from_station+'&leftTicketDTO.to_station='+to_station+'&purpose_codes=ADULT'
	headers = {'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
				'Host':'kyfw.12306.cn',
				'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
	cookies = {'_jc_save_fromStation': '%u4E0A%u6D77%2C'+from_station, '_jc_save_toStation': '%u5317%u4EAC%2C'+to_station,
				'_jc_save_fromDate':date,'_jc_save_toDate':date,'_jc_save_wfdc_flag':'dc'}
	response=requests.get(url,verify=False,headers=headers,cookies=cookies)
	#print('请求头:',response.request.headers)
	#response.encoding = 'utf-8'
	#print('返回的json数据为:',response.text)
	rows = response.json()['data']
	#print(rows)
	#初始化
	trains=formatResult.TrainData(rows)
	trains.pretty_print()
if __name__ == '__main__':
	cli()
	