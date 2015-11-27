#!/usr/bin/python

#**************************
#IMPORTS
import sys

#VARIABLES
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

#MULTI ASSIGNMENT
multi1 = multi2 = multi3 = 1
multi4, multi5, multi6 = 1, 2, "john"

#PRINT
print("")
print("PYTHON: VARIABLES")
print("")

#**************************
#PRINT
print (counter)
print (miles)
print (name)
print("")

#CONCATENATE FROM INT TO STRING
multiAll_1 = '{} {} {}'.format(multi1, multi2, multi3)

#CONCATENATE FROM (INT AND STRING) TO STRING
multiAll_2 = '{} {} '.format(multi4, multi5) + multi6

print (multiAll_1)
print (multiAll_2)

#**************************
#DELETE VARIABLE
print ( 'Deleting the varible ' + '{}'.format(counter) )
print("")
del counter

#**************************
#MANIPULATE SUBSTRINGS
str = 'IT WORLD!!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

#**************************
#SUCCESS
print ("SUCCESS!!")

