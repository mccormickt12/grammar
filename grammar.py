import sys
import re

#get file and put it into input
arg = sys.argv[1]
f = open(arg, 'r')
new_file = arg[:-3] + "_grammar.py"
new = open(new_file, 'w')
current_indent = 0
next_indent = 0
openers = ['def', 'class', 'for', 'while', 'if', 'else', 'elif', 'try', 'except']
closers = ['return', ' break']
end = 'end'
tab = "\t"
new_line = "\n"
for next in f:
	done = False
	current_indent = next_indent
	#next = f.readline()  #next line of file
	next = next.strip()  #next line of file w/o leading or trailing whitespace
	has_end = re.match(end, next)
	if has_end and not done:
		next_indent = current_indent - 1
		done = True
		continue
	for item in closers:
		has_end = re.match(item, next)
		if has_end and not done:
			next_indent = current_indent - 1
			done = True
	for item in openers:
		has_begin = re.match(item, next)
		if has_begin and not done:
			next_indent = current_indent + 1
			done = True
	start = tab*current_indent
	line = start + next + new_line
	new.write(line)
