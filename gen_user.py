# -*- coding: utf-8 -*-
import random
import time

ipaddr = "223.152.112."
ip_count = 101  #1-100 ip地址范围
sep = "\t"  #定义分隔符

#年，月，日，时，分，秒，*，*，*
starttime_tp = (2015,8,16,19,18,50,2,317,0)     #修改开始时间
starttime_sm = time.mktime(starttime_tp)
endtime_tp = (2015,8,17,19,18,50,2,317,0)   #修改结束时间
endtime_sm = time.mktime(endtime_tp)

datafile = open("data_100u.txt",'a+')

for i in range(int(starttime_sm),int(endtime_sm),300): # 每隔5分钟300秒
    time_str = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i))
    for ip in range(1,ip_count):
        score1 = str(random.randint(10,19))
        score2 = str(random.randint(800,899))
        score = score1+score2   #随机数：前2位10-19，后3位800-899之间
        line_data = ipaddr+str(ip)+sep+time_str+sep+score+"\n"
        datafile.write(line_data)
    test_data = "100.100.100.100"+sep+time_str+sep+"10000"+"\n"
    datafile.write(test_data)
