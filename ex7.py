# Prints a text string
print "Mary had a little lamb."

# Prints a string containing a formatter which is declared at the end of the line as a string
print "Its fleece was white as %s." % 'snow'

# Prints a text string
print "And everywhere that Mary went."

# Prints a text string multiplied out by 10
print "." * 10

# Creates a bunch of variables named end1-12 each which a single character text string declared
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Prints the variables as a single output by use of the + character joining the variables / strings. 
# The comma ensures line continuity through 'print' functions
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# Couldn’t you just not use the comma , and turn the last two lines into one single-line print?
# Yes, you could very easily, but then it’d be longer than 80 characters, which in Python is bad style.