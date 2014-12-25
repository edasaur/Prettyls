Prettyls
====
Lightweight tool to pretty print the directory names recursively

Directories/files will be printed out in the following fashion:

|-base_directory/
|
|----base.txt
|
|----outer_directory/
|
|--------outer_directory_file.txt
|
|----outer_directory2/



Implementation of flags have not been completed yet:

- d[num] should be used as '-d5', in which case, the tool will perform a depth limited search of 5 levels
- h should be used as '-h', in which case, teh tool will not ignore hidden files that begin with '.'



More flags will possibly follow after the implementation of these two flags
