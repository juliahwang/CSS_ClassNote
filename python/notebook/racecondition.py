import threading

g_result = 0
lock = threading.Lock()

def thread_main(*args):
	global g_result
	global lock

	lock.acquire()
	for arg in args:
		g_result += arg
	lock.release

n = 100000
offset = n//4

li = {e for e in range(n + 1)}

threads = []

 for i in range(4):
	 th = threading.Thread(target = thread_main.args = \
             li[offset * i + 1 : offset * (i + 1) + 1)
