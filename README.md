# tickets
Python3    实现12306余票查询
# 教程
网址 http://www.jianshu.com/p/fc85b094949e
# 备注
12306余票查询接口已改，新的接口为  https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-03-22&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=BJP&purpose_codes=ADULT 而且Json数据的格式有变化以及一些key值有变动
# 注意
在获取车站的拼音和大写字母的代号信息时， 将结果格式化重定向到 stations.py 时出现中文乱码，暂时不知如何解决。可以先将结果重定向到一个txt文档，然后复制到stations.py就可以。
