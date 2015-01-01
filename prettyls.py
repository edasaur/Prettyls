import os, sys, string

flags_dict = {'d':False, 'h':False, 's':False} #-d means depth-limited
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
		print "|"+"-"*4*(level-1)+str(directory[1])
		print "|"
		for filename in os.listdir(directory[0]+'/'+directory[1]):
			if level == flags_dict['d']:
				continue
			if not flags_dict['h'] and filename[0] == '.': #skip hidden directories
				continue
			elif is_directory(directory[0]+"/"+directory[1]+filename):
				stack.append((strip(directory[0]+"/"+directory[1]+filename+"/"), level+1))
			else:
				print "|"+"-"*4*level + str(filename)	
				print "|"	
		
if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == 'help':
		print "This will be the help section, sort of like a man page!"		
	elif len(sys.argv) > 1 and sys.argv[1][0] == '-': #read through specified tags
		for flag in sys.argv[1][1::]:
			try:
				int_flag = int(flag)
				if flags_dict['d']:
					flags_dict['d'] = int_flag
				else:
					raise SyntaxError('Unknown letter identifier')
				continue
			except ValueError:
				pass
			if flag not in flags_dict:
				raise SyntaxError('Flag not set')
			else:
				flags_dict[flag] = True
		#print flags_dict['s']
		if flags_dict['s']:
			if sys.argv[2][-1] != '/':
				pretty_print(sys.argv[2]+'/')
			else:
				pretty_print(sys.argv[2])
		else:
			pretty_print(os.getcwd())
	else:
		pretty_print(os.getcwd())
