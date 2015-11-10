'''
Author: Aditi Nair (asn264)
Date: November 10 2015

This module contains functions that are responsible for interactions with the user - prompting, validating prompts, and parsing them for program use.
'''

from Position import *
import sys

def prompt_for_list():

	'''Prompts the user for a list of positions. Accepts keyboard interrupts, etc.'''
	try:
		return raw_input("Enter a comma-separated, positive integer-valued list of positions to buy in parallel.")
	except (KeyboardInterrupt,EOFError):
		sys.exit()

def prompt_for_int():

	'''Prompts the user for a number of trials to run. Accepts keyboard interrupts, etc.'''
	try:
		return raw_input("Enter the number of trials you would like to run.")
	except (KeyboardInterrupt,EOFError):
		sys.exit()

def parse_for_list(str):

	'''Takes user input for a list of positions and tries to parse the string into a list of integers. Accepts all integers but complains for incorrect formatting.'''
    
	if str.strip().lower() == "quit":
		sys.exit()
        
	else:

	        positions = []
        
		#Find the open and close brackets
		try:
			left_bracket = str.index("[")
			right_bracket = str.index("]")

			#Assume the brackets are at the ends. If they are not, an error will be raised below because we will try and case them as ints.
			str = str[1:-1]

			#Continue while the string is nonempty
			while len(str):

		                #Do not accept strings like [10,100,]
            	    		if str[-1] == ",":
                    			print "Invalid list."
                    			positions[:] = []
                    			break
                
				#Remove extra white space if necessary
				str = str.strip()
					
				#Get the index of the first comma
       			 	try:
            				comma_index = str.index(",")
           	 	
            				#Parse the string from the first index up to the comma and see if the substring is a positive integer.
            				if str[0:comma_index].strip().isdigit():
               	 		
						#Add the new position integer to the list
	       		         		new_pos = int(str[0:comma_index].strip())
               					positions.append(new_pos)
               	 	
						#Delete the part of the string that relates to the new position
               					str = str[comma_index+1:]
               	 
					#Occurs if the value provided is not a positive integer
            				else:
               		 			print "Invalid list."
                				positions[:] = []
               					break
	
	       		     	#If there is no first comma, either the string is incorrectly formatted or there is only one element (and therefore no comma)
        			except ValueError:
		
       			     		#Parse the entire string and see if it is a positive integer
            				if str.strip().isdigit():
               		 			new_pos = int(str.strip())
                				positions.append(new_pos)
                				#Force the string to empty and end the while loop
                				str = str[-1:0]
            				else:
                				print "Invalid list."
                				positions[:] = []
                				break
		
		#Occurs if there is not one left bracket and one right bracket in the string
		except ValueError:		
			print "Invalid list."
			positions[:] = []
	
    		return positions

    
def parse_for_int(str):

	'''Takes user input for number of trials as a string and tries to parse it as an int. Accepts only positive integers.'''

	if str.lower() == "quit":
		sys.exit()
	else:
		#Remove extra whitespace and check if int
    		if str.strip().isdigit():
			if int(str.strip()) == 0:
				print "Invalid input."
				return None
			else:
				return int(str.strip())
    		else:
       		 	print "Invalid input."
        		return None


def get_list():

	'''Takes a list of positions from the user as a string and converts it to a list of Position objects. 
	Continues until an acceptable list is provided, or "quit" or keyboard interrupt.'''
    
	#Get a list of string in valid format
	usr_list = parse_for_list(prompt_for_list())

	#If a list of any non-negative integers was provided
	if len(usr_list) > 0:

		#Cast as Position objects
		try:	
			positions = [Position(i) for i in usr_list]
			return positions
		#Insist on a list
		except InvalidPositionError:
			print "Invalid input."
			return get_list()

	#Insist on a list
	else:
		return get_list()

def get_int():

	'''Asks the user for a number of trials to run. Continues until a positive integer is provided or quit or keyboard interrupt.'''
    
	usr_int = parse_for_int(prompt_for_int())
	if usr_int != None:
		return usr_int
	else:
		return get_int()

