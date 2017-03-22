# -*- coding:utf-8 -*-
from prettytable import PrettyTable
from colorama import init, Fore
#colorama 控制台输出彩色文字
#PrettyTable  像MySQL数据库那样格式化显示数据

class TrainData(object):
	# 显示车次、出发/到达站、 出发/到达时间、历时、一等坐、二等坐、软卧、硬卧、硬座
	header = '车次 出发/到达站 出发/到达时间 历时 一等坐 二等坐 软卧 硬卧 硬座'.split()
	def __init__(self,rows):
		self.rows=rows
	def _get_duration(self,row):
		#获取车次的运行时间
		duration=row.get('lishi').replace(':','小时')+'分钟'
		#print(duration)
		if duration.startswith('00'):
			return duration[4:]
		if duration.startswith('0'):
			return duration[1:]
		return duration
	#Python内置的@property装饰器就是负责把一个方法变成属性
	@property
	def trains(self):
		#这句必须有，否则颜色设置不起作用
		#Fore.GREEN+'Hello' 对这个字符串设置颜色
		#Fore.GREEN+'Hello'+ Fore.RESET   输出之后颜色恢复默认
		init(autoreset=True)
		for row in self.rows:
			data= row.get('queryLeftNewDTO')
			#print(data)
			train=[ 
				# 车次
				data['station_train_code'],
				# 出发、到达站
				Fore.GREEN+'-'.join([data['start_station_name'], data['end_station_name']])+ Fore.RESET,
				# 出发、到达时间
				Fore.RED+'-'.join([data['start_time'], data['arrive_time']])+ Fore.RESET,
				# 历时
				self._get_duration(data),
				# 一等坐
				data['zy_num'],
				# 二等坐
				data['ze_num'],
				# 软卧
				data['rw_num'],
				# 软坐
				data['yw_num'],
				# 硬坐
				data['yz_num']
				]
			#相当于暂存，下次循环数据依然存在
			yield train
	def pretty_print(self):
		#格式化打印
		pretty=PrettyTable()
		#设置标题行
		pretty._set_field_names(self.header)
		#将每一行的数据加入到  pretty
		for train in self.trains:
			pretty.add_row(train)
		print(pretty) 
		

