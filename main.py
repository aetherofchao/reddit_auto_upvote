#!/usr/bin/python3
from Reddit import Reddit
import sys


def usage():
	print (
"""upvote [flag] [option] 

	-d --debug             |	enable debug mode

	l list    [file]       |	lists averige upvode/downvote/none count
	p print   [file] [n]   |	prints last n collected posts 
	c collect [sub] [file] |	starts collecting posts to file
	    controls:  q       |	save and exit
	               w       |	save
	               e       |	exit without saving (saves each minute)
	               s       |	skip one post
	               l       |	clear display
	               d       |	enable debug mode
	""")	

def main():
	argc = len(sys.argv)

	r = Reddit()

	shift = 0

	if (argc > shift + 1 and (sys.argv[shift + 1] == "--debug" or sys.argv[shift + 1] == "-d" )):
		r.set_debug_flag()
		shift += 1

	# r.set_choise(["[up]","[dw]","[no]"])
	r.set_choise(["[no]"])
	r.set_bot("bot4")
	r.set_sub("all")

	if (argc > shift + 1 and (sys.argv[shift + 1] == "list" or sys.argv[shift + 1] == "l" )):
		if (argc > shift + 2):
			r.read(sys.argv[shift + 2])
		else:
			r.read()
		r.list()  # to see results

	elif (argc > shift + 1 and (sys.argv[shift + 1] == "print" or sys.argv[shift + 1] == "p" )):
		if (argc > shift + 2):
			r.read(sys.argv[shift + 2])
		else:
			r.read()

		if (argc > shift + 3):
			r.print(int(sys.argv[shift + 3]))
		else:
			r.print()  # to see results
	
	elif (argc > shift + 1 and (sys.argv[shift + 1] == "collect" or sys.argv[shift + 1] == "c" )):
		if (argc > shift + 2):
			r.set_sub (sys.argv[shift + 2])
		if (argc > shift + 3): # file
			r.set_file(sys.argv[shift + 3])
		else:
			r.set_file(sys.argv[shift + 2]+".bin")
		r.collect()  # endless loop


	else: usage()


if (__name__ == '__main__'):
	main()
