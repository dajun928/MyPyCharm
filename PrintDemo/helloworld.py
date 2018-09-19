#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
    工具脚本 201809月份日记格式
'''
def get_week_day(i):
  week_day_dict = {
    0 : u'星期一',
    1 : u'星期二',
    2 : u'星期三',
    3 : u'星期四',
    4 : u'星期五',
    5 : u'星期六',
    6 : u'星期天',
  }
  return week_day_dict[i]

for i in range(1,31):
    d=(i+4)%7
    print '-------------------------------------------------------------->'
    print u"2018年9月"+str(i)+u"日"+"  "+get_week_day(d)
    print '  '










