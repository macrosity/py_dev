# Declare x as a string containing a formatter
x = "There are %d types of people." % 10

# Declare binary as a text string
binary = "binary"

# Declare do_not as a text string containing a single quote character
do_not = "don't"

# Declare y as a string containing two formatters
y = "Those who know %s and those who know %s." % (binary, do_not) # String inside a string

# Print the strings containing formatters and variables
print x
print y

# Print two new strings containing formatters that incorporate the original strings that contained the variables
print "I said: %r" % x				# String inside a string
print "I also said: '%s'" % y		# String inside a string

# Declare hilarious as False (a Boolean value)
hilarious = False

# Declare joke_evaluation as a string containing a formatter
joke_evaluation = "Isn't this joke so funny?! %r"

# Print the variable string joke_evaluation and define the formatter as the variable hilarious which has a value of False
print joke_evaluation % hilarious

# Declare two more variables as text strings
w = "This is the left side of..."
e = "a string with a right side."

# Print the two variable strings with a + character to "join" then together
print w + e # String inside a string