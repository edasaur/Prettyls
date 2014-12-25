import os, sys, string

flags_dict = {'d':False} #-d means depth-limited
def join(list_str,join_char):
	result = ""
	for item in list_str:
		result += item + "/"
	return 	result[0:-1]

def strip(path):
	path_dirs = string.split(path, '/')
	parent_path, fold_name = join(path_dirs[0:-2],'/'), join(path_dirs[-2::],'/')
	return [parent_path, fold_name]

def is_directory(directory): #probably not the best way to figure out whether a directory or not
	try:
		os.listdir(directory)
	except OSError as e:
		return False
	return True
	
def pretty_print(input_dir):
	stack = [(strip(input_dir), 1),]
	while stack:
		directory, level = stack[-1]
		if directory[1][-1] != "/":
			directory[1] += "/"
		stack = stack[0:-1]
		print "|"+"-"*2*(level-1)+str(directory[1])
		print "|"
		for filename in os.listdir(directory[0]+'/'+directory[1]):
			if filename[0] == '.': #skip hidden directories
				pass
			elif is_directory(directory[0]+"/"+directory[1]+filename):
				stack.append((strip(directory[0]+"/"+directory[1]+filename+"/"), level+1))
			else:
				print "|"+"-"*2*level + str(filename)	
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
		if sys.argv[2][-1] != '/':
			pretty_print(sys.argv[2]+'/')
		else:
			pretty_print(sys.argv[2])
	else:
		if sys.argv[1][-1] != '/':
			pretty_print(sys.argv[1]+'/')
		else:
			prett_print(sys.argv[1])

