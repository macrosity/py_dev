# Start off by showing the menu
print (30 * '-')
print ("	M A I N - M E N U")
print (30 * '-')
print ("1. Backup")
print ("2. User Management")
print ("3. Reboot Server")

# Add some more robust error handling by only accepting int input
is_valid = 0

while not is_valid :
	try :
		choice = int ( raw_input('Enter your choice [1-3] : ') )
		is_valid = 1 # Set it to 1 to validate input and terminate the while not loop
	except ValueError, e :
		print ("'%s' is not a valid integer." % e.args[0].split(": ") [1])

# Get the input
#choice = raw_input('Enter your choice [1-3] : ')

# Convert the string to integer type
#choice  = int(choice)

# Take action as per selected menu option
if choice == 1:
	print ("Starting backup ...")
elif choice == 2:
	print ("Starting user management module ...")
elif choice == 3:
	print ("Rebooting server ...")
else :
	print ("WTF are you doing? Invalid number, try again ...")

