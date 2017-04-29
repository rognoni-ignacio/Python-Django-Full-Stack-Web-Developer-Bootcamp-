#### PART 6: EXERCISE REVIEW  #######

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

## Problem 1 ##
print("---Problem 1---")
# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print("Print 'd'")
print(s[0])

# 'o'
print("Print '0' - Part 1")
print(s[-1])
print("Print '0' - Part 2")
print(s[len(s)-1])

# 'djan'
print("Print 'djan'")
print(s[:4])

# 'jan'
print("Print 'jan'")
print(s[1:4])

# 'go'
print("Print 'go'")
print(s[4:])

# Bonus: Use indexing to reverse the string
print("Reverse string")
print(s[::-1])

###############
## Problem 2 ##
###############
print("---Problem 2---")
# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
print("Befor reassign")
print(l)
l[2][2] = "goodbye"
print("After reassign")
print(l)

###############
## Problem 3 ##
###############
print("---Problem 3---")
# Using keys and indexing, grab the 'hello' from the following dictionaries:

print("Dictionary 1")
d1 = {'simple_key':'hello'}
print(d1['simple_key'])

print("Dictionary 2")
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

print("Dictionary 3")
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
print("---Problem 4---")
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))


###############
## Problem 5 ##
###############

print("---Problem 5---")
# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
# "Hello my dog's name is Sammy and he is 4 years old"
print("Hello my dog's name is {var_name} and he is {var_age} years old".format(var_name = name, var_age = age))
