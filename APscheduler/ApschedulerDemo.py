# coding=utf-8

# 定时调度工具   APScheduler是一个Python定时任务框架

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from OtherClass import *



#本类的方法
def my_job01():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    other=OtherClass()
    # scheduler.add_job(my_job01, 'cron', hour ='16',minute ='44')
    scheduler.add_job(other.my_job02, 'cron', hour ='17',minute ='15')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


