from sys import argv
from os.path import exists

script, from_file, to_file = argv
out_file = open(to_file, 'w')
out_file.close()
