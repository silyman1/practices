#coding=utf-8

#多线程

import threading
import time 
def mytime():
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 


data = 0
lock = threading.Lock()
def func():
	global data
	print '%s acquire lock %s\n'%(threading.currentThread().getName(),mytime())
	if lock.acquire():
		print '%s get lock %s\n'%(threading.currentThread().getName(),mytime())
		data +=1
		time.sleep(2)
		print '%s release lock %s\n'%(threading.currentThread().getName(),mytime())
		lock.release()
t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()
#t = threading.Thread(target=func)
#t.start()
#class MyThread(threading.Thread):
#	def run(self):
#		print 'MyThread ==================='
#t =MyThread(target=func)
#t.start()
