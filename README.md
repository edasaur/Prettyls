Prettyls
====
Lightweight tool to pretty print the directory names recursively

Directories/files will be printed out in the following fashion:
```
|-base_directory/
|
|----base.txt
|
|----outer_directory/
|
|--------outer_directory_file.txt
|
|----outer_directory2/
```


Current implemented flags:

- d[num] should be used as '-d5', in which case, the tool will perform a depth limited search of 5 levels
- h should be used as '-h', in which case, the tool will not ignore hidden files that begin with '.'
- s should be used as '-s', in which case, the tool will accept arguments to specify a different path than the current working directory
