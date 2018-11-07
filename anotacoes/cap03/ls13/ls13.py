# -*- coding: utf-8 -*-
# Quiz 1 Loop
# import random

# random_list = [0, 1, 2, 20]
# list_length = 20

# # Minha resposta
# def random_list_number():
#     i = 0
#     while i < 20:
#         random_list.append(random.randrange(10))
#         i += 1 

# # Resposta do curso
# def random_list_number():
#     while len(random_list) < list_length:
#         random_list.append(random.randint(0, 10))

# random_list_number()
# print random_list

#-----------------------------
# Quiz 2 Loop
# import random

# random_list = []
# list_length = 20

# def random_list_number():
#     while len(random_list) < list_length:
#         random_list.append(random.randint(0, 10))

# random_list_number()

# Minha resposta
# index = 0
# count = 0

# while index < len(random_list):
#     if random_list[index] == 9:
#         count += 1
#     index += 1

# print random_list
# print count

#-----------------------------


# # Quiz 3 loop
# # Great! We now want to create a new list that contains the counts
# # of all occurrances of every number seen in the randomly generated 
# # list. That means we want counts of all occurrences of all numbers
# # from 0 through 10 in our randomly generated list.

# # Let's store our counts in a list of length 11 
# # with zeros filled in.

# # We can multiply a list construct to create a list with the same
# # elements n number of times.
# count_list = [0] * 11

# # Check that we have a list of length 11 with all 0 elements
# print count_list

# # We use this list to store our count of numbers 0 to 10 - take note 
# # that total numbers 0 to 10 is 11. We can use the index number of
# # each element to refer to the count of our target
# # number. Our target number is actually the index of the list.
# # For example, assume count_list looks like this:

# count_list = [1,2,3,2,2,1,1,2,3,1,2]

# # Let's print out the occurrences for the numbers 0, 4, 5, and 6
# print count_list[0]
# print count_list[4]
# print count_list[5]
# print count_list[6]

# # Therefore, for our output, we want a count_list that looks like:
# # [1,2,3,2,2,1,1,2,3,1,2]

# # Here's our code that we coded before

# import random

# # Create random list of integers using while loop --------------------
# random_list = []
# list_length = 20

# while len(random_list) < list_length:
#   random_list.append(random.randint(0,10))

# print "lista gerada  ", random_list
# # --------------------------------------------------------------------

# # Initialize count_list for every integer between 0 and 10. 
# # A number will correspond to an index of this count_list
# # Therefore if we see that there are 3 occurrences of the number 4, 
# # we assign count_list[4] = 3, if there are 5 occurrences of the 
# # number 6, we assign count_list[6] = 5

# count_list = [0] * 11
# index = 0
# count = 0

# # Write code here to loop through every number in random_list and
# # update count_list appropriately

# while index < len(random_list):
#     number = random_list[index]
#     count_list[number] = count_list[number] + 1
#     index += 1


# # Check the list we created
# print count_list
# # If we coded everything correctly, the sum of all of the numbers 
# # in count_list should be 20
# print sum(count_list)

#Quiz 4 loop while

# We now would like to summarize this data and make it more visually appealing
# We want to go through count_list and print a table that shows the number and its 
# corresponding count.

# The output should look like this neatly formatted table:
"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""
# Here is our code we have written so far:

import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

# Aggregate the data -------------------------------------------------
count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1

# Minha resposta
# print 'random_list  ', random_list
# def showTable():
#     index = 0
#     print 'number | ocorrência '
#     for target_list in count_list:
#         # print index, ' | ', target_list # mostrando normal
#          # * vai aparecer de acordo com a multiplicação em relação a quantidade
#          # que aparece
#         print index, ' | ', '*' * target_list
#         index += 1

# showTable()

# Resposta do curso

def print_table():
    print "number | occurrence"
    index = 0
    num_len = len("number")

    while index < len(count_list):
        num_spaces = num_len - len(str(index))
        print " " * num_spaces + str(index) + " | " + str(count_list[index])
        index = index + 1

print_table()