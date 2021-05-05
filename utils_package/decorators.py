import time
import urllib.request
from functools import wraps
from datetime import datetime, timezone

def timeit(f):

	def timed(*args, **kw):

		ts = time.time()
		result = f(*args, **kw)
		te = time.time()

		print('took: %2.4f sec' % \
		  (te-ts))
		return result

	return timed

def func_name(f):
	
	def func_n(*args, **kw):
		result = f(*args, **kw)
		print('func:%r args:[%r, %r] '% \
		  (f.__name__, args, kw,))
		return result
	return func_n


def logged(fn):

	
	@wraps(fn)
	def inner(*args, **kwargs):
		run_dt = datetime.now(timezone.utc)
		result = fn(*args, **kwargs)
		print('{0}: called {1}'.format(fn.__name__, run_dt))
		return result
		
	return inner



def is_connected(fn):

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
	def dec(fn):
		def inner(*args, **kwargs):
			return fn(*args, **kwargs)
		return inner
	if (auth):
		return dec
	else:
		print("You are not authenticated")

