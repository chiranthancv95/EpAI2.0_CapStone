'''
This script contains all the decorators used in other programs.
'''


import time
import urllib.request
from functools import wraps
from datetime import datetime, timezone

def timeit(f):
	'''
	This decorator prints the time that the code too execute a certain task.
	'''

	def timed(*args, **kw):

		ts = time.time()
		result = f(*args, **kw)
		te = time.time()

		print('took: %2.4f sec' % \
		  (te-ts))
		return result

	return timed

def func_name(f):
	'''
	This decorator prints out the function name and other parameters
	'''
	
	def func_n(*args, **kw):
		result = f(*args, **kw)
		print('func:%r args:[%r, %r] '% \
		  (f.__name__, args, kw,))
		return result
	return func_n


def logged(fn):
	'''
	This is a logger decorator which logs all the function parameters with time duration.
	'''

	
	@wraps(fn)
	def inner(*args, **kwargs):
		run_dt = datetime.now(timezone.utc)
		result = fn(*args, **kwargs)
		print('{0}: called {1}'.format(fn.__name__, run_dt))
		return result
		
	return inner



def is_connected(fn):
	'''
	This decorator checkcs whether the internet connection is present or not.
	'''

	@wraps(fn)
	def connected(*args, **kwargs):
		result = fn(*args, **kwargs)
		if urllib.request.urlopen('http://google.com'):
			# connect to the host -- tells us if the host is actually
			# reachable
			print ("Connected to internet")
		else:
			print ("Not connected to internet")
	return connected


def authenticatedOrNot(auth):
	'''
	This decorator ensures that the function or user is authenticated to run the program.
	'''
	def dec(fn):
		def inner(*args, **kwargs):
			return fn(*args, **kwargs)
		return inner
	if (auth):
		return dec
	else:
		print("You are not authenticated")

