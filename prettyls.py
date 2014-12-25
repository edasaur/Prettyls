import os, sys, string

flags_dict = {'d':False} #-d means depth-limited
def strip(path):
	path = string.split(path, '/')
		

def is_directory(directory): #probably not the best way to figure out whether a directory or not
	try:
		os.listdir(directory)
	except OSError as e:
		return False
	return True
	
def pretty_print(input_dir):
	stack = [(input_dir, 1),]
	while stack:
		directory, level = stack[-1]
		if directory[-1] != "/":
			directory += "/"
		stack = stack[0:-1]
		print "-"*2*(level-1)+str(directory)
		print "|"
		for filename in os.listdir(directory):
			if filename[0] == '.': #skip hidden directories
				pass
			elif is_directory(directory+filename):
				stack.append((directory+filename, level+1))
			else:
				print "-"*2*level + str(filename)	
				print "|"	
		
if __name__ == "__main__":
	print "This is the first argument: "+str(sys.argv[0])
	if sys.argv[1] == 'help':
		print "This will be the help section, sort of like a man page!"		
	elif sys.argv[1][0] == '-':
		for flag in sys.argv[1][1::]:
			if flag not in flags_dict:
				raise SyntaxError('Flag not set')
			elif type(flag) == int:
				if flags_dict['d'] == True:
					flags_dict['d'] = flag
				else:
					raise SyntaxError('Unknown letter identifier')
			else:
				flags_dict[flag] = True
		pretty_print(sys.argv[2])
	else:
		pretty_print(sys.argv[1])

