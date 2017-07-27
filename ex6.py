#setup string x
x = "There are %d types of people." % 10
#set variable binary
binary = "binary"
#set variable do_not
do_not = "don't"
#set string y
y= "Those who know %s and those who %s." % (binary, do_not) #string in a string

#printing the joke
print x
#still printing the joke
print y

# printing the joke again
print "I said: %r." % x #string in a string
print "I also said: '%s'." % y #string in a string

#set strings for evaluating the joke
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #string in a string

#print joke evaluation
print joke_evaluation % hilarious

#set up strings for concatenation
w = "This is the left side of..."
e= 'a string with a right side.'

#print concatenated strings
print w + e
