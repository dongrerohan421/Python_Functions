import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program started on on " + time.ctime())
while(break_count < total_break):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=8JJrz_VDbx0")
	break_count = break_count + 1

