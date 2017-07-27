name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# num of centimeters per inch
cm_per_inch = 2.54

# num kg per lb
kg_per_lb = .453592

height_in_centimeters = height * cm_per_inch
weight_in_kg = weight * kg_per_lb

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %d centimeters." % height_in_centimeters
print "He's %d pounds heavy." % weight
print "That's %d kilograms." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s deending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

print "I can print %d in hex as %x !" % (weight, weight)
