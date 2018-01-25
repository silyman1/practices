#返回函数，闭包
i = 0
def a():
	global i
	def b():
		global i
		s = i +1
		i = i+1
		print s
	return b
c=a()
c()
c= a()
c()
c= a()
c()
c= a()
c()
c= a()
c()

#匿名函数
def is_odd(n):
	return n % 2 == 1

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print L
def log(action,text):
	def decorator(func):
		def wrapper(*arg,**kwrgs):
			print '%s---%s'%(action,text)
			print 'begin'
			func(*arg,**kwrgs)
			print 'end'
			return
		return wrapper
	return decorator
#装饰器
@log('execute','abcdefg')
def now():
	print('2015-3-25')

now()
print now.__name__

