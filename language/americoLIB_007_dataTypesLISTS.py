#!/usr/bin/python

#**************************
#IMPORTS
import sys

#**************************
#LISTS (their elements and size can be changed)
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

#PRINTS
print ("")
print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists

#**************************
#TUPLES (cannot be updated. Tuples can be thought of as read-only lists)
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

#PRINTS
print ("")
print (tuple)           # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists

#**************************
#DICTIONARY(kind of HASHTABLE type)
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

#PRINTS
print ("")
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

#**************************
#UPDATE LISTS vs TUPLES
#tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list

#**************************
#SUCCESS
print ("\nSUCCESS!!")