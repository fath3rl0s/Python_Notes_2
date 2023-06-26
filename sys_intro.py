#Introduction to Sys Module
#Carlos Enamorado 



'''
SYS Module
	The sys module provides a bunch of functions and variables 
	related to the python run-time environment

	For example, sys gives access to data sent as part of the 
	command-line argment when executing a python script

	This can be useful when entering variable data as part of the
	command-line when executing the script

	Sys module is a standard library and comes packaged with your python
	installed so you dont need to download and install pip but you 
	may need to download it with other modules

	To use it, we first need to import it to interact with it

'''

import sys

print("SYS Module")



print("\n")



#Version Information
print("Version Information")


print(sys.version)
#We can also see this output when starting python as an interpreter



print("\n")



#Access other information with sys
print("Access Other Information")


print("\n")


#Current executable binary
print(sys.executable)

#OS we are running
print(sys.platform)


print("\n")


'''
	Sys can also be used to interact with stdin,stdout, and stderr
	We leverage the sys module to read from stdin to write to stdout directly


	So far we have used the input and print functions to input and 
	display data from the terminal

	The sys module can also allow this fucntionality as so:

'''


print("Sys w/ STDIN and STDOUT")

#This will hang and wait for user input in the CLI
for line in sys.stdin:
	#This was after to avoid exiting out later on
	break
	#This will exit the for loop if user enters 'exit'
	if line.strip() == 'exit':
		break
	#This will print the user input
	sys.stdout.write(">> {}".format(line))


'''
	Accessing lower level functions with sys taht can be more difficult
	to use from existing python functions

	For example, we can use sys to flush out buffers. Python will write everything
	currently in the buffer directly to the terminal.

	Rather than waiting for certain amount of data or a specific character
'''

for i in range(1,5):
	sys.stdout.write(str(i))
	sys.stdout.flush()

for i in range(1,5):
	print(i)


print("\n")

#Call status bar to show the progress of a running job

import time

for i in range(0,51):
	time.sleep(0)
	sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, "."*(50 - i)))
	sys.stdout.flush()
sys.stdout.write("\n")


print("\n")

#First element will always be the name of the script
print(sys.argv)

#Pass any arguments after


#Helpful if you wanted to pass a username and password to the script
#Verify and file with an error if script has been called without the required args

if len(sys.argv) != 3:
	print("[X] To run {} enter an username and password".format(sys.argv[0]))
	sys.exit(5)

#You can assign these values 

username = sys.argv[1]
password = sys.argv[2]

print("{} {}".format(username,password))


print("\n")


#We can also use sys to access the PATH where python will search for modules
#Useful if using a virtual env
print("Access Path and Modules")
print("\n")


print(sys.path)


print("\n")


#Access all modules
print(sys.modules)


print("\n")

'''
	Once you are done with a script or based on some error, you can exit with a specific code
	This code can be usded to indicate a fail or success
	If calling a number of tools or scripts, such as enumeration, and we wanted to know if successful
	of failed, we can use the exit code to know the outcome of execution
'''


sys.exit(0)


'''
	To view error codes, use 'echo $?'

	┌──(f4th3rl0s㉿kali)-[~]
	└─$ echo $?
	5
'''




'''
	docs.python.org - For more information
	Always rely on the official documentation for torubleshooting
'''