
# This Python file uses the following encoding: utf-8
import os, sys

# Quiz - 4
# speed_of_light = 299792458.0 
# cycles_per_second = 2700000000.0

# print speed_of_light / cycles_per_second

# Quiz 10
# Escreva um código em Python que define a variável age (idade) e atribui a ela sua idade em anos inteiros, depois usa esse valor para imprimir o número de dias correspondente.

# age = 30
# days_in_year = 365.25
# print age * days_in_year

# This code shows some basic variable assignment and string printing. 
# name = "Luciano"
# print "Hello " + name
# print name * 4


# This code shows the difference between the string "4" and the number 4.
# Remove the four comment characters (#) on the lines below to see what happens.
#print 4
#print "4"
#print 4 + 4
#print "4" + "4"

# This code shows some of the different mistakes that are easy to make while 
# working with strings. Remove one comment at a time and press Test Run to 
# see what happens. Be sure to re-comment before moving on or the program
# will keep showing you an error.
#print 'hello"
#print hello
#print "hello

# This code will give you a peek at what you are about to learn! Uncomment 
# all of the lines below to get a glimpse of "string indexing"
# name = "Andy"
# print name[0]
# print name[1]
# print name[2]
# print name[3 + 1]

# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.
# s = 'audacity'
# print 'U' + s[2:] 

# s = "any string"
# print s[:]
# print s + s[0:-1 + 1]
# print s[0:]
# print s[:-1]
# print s[:3] + s[3:]

# usandoFind = "Um texto qualquer lorem"
# print usandoFind.find('texto') #3
# print usandoFind[3:] #texto qualquer lorem
# print usandoFind.find('U') #0
# print usandoFind.find('Xuxa') #-1

# s = 'any string'
# print s.find('')
# print s.find(s + '!!!') + 1
# print 's'.find('s')


# print "Example 3: Printing out everything after a certain substring"
# my_string = "My favorite color: blue"
# color_start_location = my_string.find("color:")
# favorite_color = my_string[color_start_location:]
# print favorite_color # oops, this line prints out 'color: ' as well...
# print favorite_color[7:] # this fixes it!

#exemplos de find trocando valores
print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string