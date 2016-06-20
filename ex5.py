# This script includes variables within the string, rather than outside of it.

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Try to write some variables that convert the inches to centimetres and lbs to kilos.
kilo = weight / 2.2
cm = height * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "If you're counting in centimetres that's %d." % cm
print "He's %d pounds heavy." % weight
print "In kilos that is %d." % kilo
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, cm, kilo, age + cm + kilo)

# Here I will round a floating point number.
my_num = 5.2

rounded = round(my_num)

# Need to work out why this formatter does not print the floating point (sorted, needed %r instead of %d)
print "My floating point number is %r." % my_num
print "My rounded number is %r." % rounded
