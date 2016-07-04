import time
import random

print (33 * '#')
print ('# Welcome to Russian Roulette!! #')
print (33 * '#')

time.sleep(3)

is_valid = 0
while not is_valid :
	try : 
		number = int( raw_input('Enter a number [1-6] : ') )
		is_valid = 1
	except ValueError, e :
		print ("'%s' is not a valid number." % e.args[0].split(": ")[1])

	#	print ('You entered %s !' % number)

q = raw_input('... ARE you ready  ?! Press y or n : ')
if q == 'y' :
	x = random.randrange(1,6)
	for i in range(5) :
		print ("BE READY ...")
	time.sleep(3)
	print ("My number is %x" % x)

	if x != int(number):
		print ("Wow, you are lucky!")
	else:
		print ("BANG BANG! MY BABY SHOT ME DOWN!")
