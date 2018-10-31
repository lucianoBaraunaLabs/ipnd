# coding: utf-8

# Quiz 4 Dias do mês
# Given the variable,

# days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# # define a procedure, how_many_days,
# # that takes as input a number
# # representing a month, and returns
# # the number of days in that month.

# def how_many_days(month_number):
#  return days_in_month[month_number - 1]

# print how_many_days(1)
# #>>> 31

# print how_many_days(9)
# #>>> 30

# Quiz 5 - Treinando Listas
# Every entry in the following list is itself a list
# nested_list = [['HTML', 'Hypertext Markup Language forms the structure of webpages'],
#                ['CSS' , 'Cascading Style Sheets give pages style'],
#                ['Python', 'Python is a programming language'],
#                ['Lists', 'Lists are a data structure that let you organize information']]

# first_concept = nested_list[0]

# print "What do you think this will print?"
# print first_concept 

# print "Since first_concept was itself a list, we can access its elements"
# first_title = first_concept[0]
# first_description = first_concept[1]


# print "What will this print?"
# print first_title
# print first_description

#Quiz 07 - Países
# Given the variable countries defined as:

# #             Name    Capital  Populations (millions)
# countries = [['China','Beijing',1350],
#              ['India','Delhi',1210],
#              ['Romania','Bucharest',21],
#              ['United States','Washington',307]]

# # Write code to print out the capital of India
# # by accessing the list

# print countries[1][1]

#Quiz 26
# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.



# def sum_list(listNumber):
#     result = 0
#     for n in listNumber:
#         result += n
#     return result
        
 
# print sum_list([1, 7, 4])
# #>>> 12

# print sum_list([9, 4, 10])
# #>>> 23

# print sum_list([44, 14, 76])
# #>>> 134

#Quiz 27
# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

# def measure_udacity(list):
#     count = 0
#     for e in list:
#         if e[0] == 'U':
#             count = count + 1
#     return count



# print measure_udacity(['Dave','Sebastian','Katy'])
# #>>> 0

# print measure_udacity(['Umika','Umberto'])
# #>>> 2

#Quiz 28
# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

# Opção com while
# def find_element(p, t):
#     i = 0
#     while i < len(p):
#         if p[i] == t:
#             return i
#         i= i + 1
#     return -1

# def find_element(p, t):
#     for e in p:
#         if e == t:
#             return i
#         i = i + 1
#     return -1



# print find_element([1,2,3],3)
# #>>> 2

# print find_element(['alpha','beta'],'gamma')
# #>>> -1

# Quiz 29
# # Define a procedure, find_element,
# # using index that takes as its
# # inputs a list and a value of any
# # type, and returns the index of
# # the first element in the input
# # list that matches the value.

# # If there is no matching element,
# # return -1.

# def find_element(p, t):
#    if t in p:
#        return p.index(t)
#    return -1



# print find_element([1,2,3],3)
# #>>> 2

# print find_element(['alpha','beta'],'gamma')
# #>>> -1


# Quiz 22 Criando função nextDay
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

# def nextDay(year, month, day):
#     # YOUR CODE HERE
#     y = year
#     m = month
#     d = day + 1
   
#     if d > 30:
#         d = 1
#         m += 1
    
#     if m > 12:
#         m = 1
#         y += 1

#     return y, m, d

# print nextDay(1999, 12, 30) #=> (2000, 1, 1)
# print nextDay(2013, 1, 30) #=> (2013, 2, 1)
# print nextDay(2012, 12, 30) #=> (2013, 1, 1


# Processo de solução de problema
# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    # Em todos os casos a primeira data vem antes da primeira
    # Retrun True if year1-month1-day1 is before year2-moth2-day2.
    # Otherwise, return False.
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


print daysBetweenDates(2018, 1, 1, 2018, 12, 28)