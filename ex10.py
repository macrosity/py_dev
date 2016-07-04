# "I am 6'2\" tall."	# escape double-quote inside a string
# 'I am 6\'2" tall."	# escape single-quote inside a string

# Here are some escape sequences

#	\\	Backslash (\)
#	\'	Single-quote (')
#	\"	Double-quote (")
#	\n	ASCII linefeed (LF)
#	\t	Horizontal tab (TAB)



tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Here's a tiny piece of fun code to try out

#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,

# Here I am using triple single-quote instead of double-quote
steveo = '''
Here's some stuff.
That I wrote.
As you can see.
It is real interesting.
'''

print steveo

# Writing my own escape sequences and format strings for testing ...

basic = 'basic\n\t formatter'

my_tab = "\t This text is indented with a tab."
non_tab = "This one is not."
formatter_0 = "Here I use a %s." % basic

print my_tab
print non_tab


print formatter_0
