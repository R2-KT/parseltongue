#import arguments
from sys import argv

#save args
script, filename = argv

#open file
txt = open(filename)


#describe output with filename
print "Here's your file %r:" % filename
#output file contents
print txt.read()

#close the file
txt.close()

#prompt for filename input
print "Type the filename again:"
#save prompted filename input
file_again = raw_input("> ")

#open file again
txt_again = open(file_again)
#output file contents again
print txt_again.read()

#close the file again
txt_again.close()
