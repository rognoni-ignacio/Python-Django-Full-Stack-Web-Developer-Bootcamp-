# -*- coding: utf-8 -*-
#### PART 9: FUNCTION EXERCISES #####

## -- PROBLEM 1 -- ##
print "Problem 1"
# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def array_check(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

print "Check if [1, 2, 3] in [1, 1, 2, 3, 1]"
print array_check([1, 1, 2, 3, 1])

print "Check if [1, 2, 3] in [1, 1, 2, 4, 1]"
print array_check([1, 1, 2, 4, 1])

print "Check if [1, 2, 3] in [1, 1, 2, 1, 2, 3]"
print array_check([1, 1, 2, 1, 2, 3])


## -- PROBLEM 2 -- ##
print "Problem 2"
# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def string_bits(str):
    result = ""
    for i in range(len(str)):
        if i%2 == 0:
            result += str[i]
    return result

print string_bits("Hello")
print string_bits("Hi")
print string_bits("Heeololeo")

print "Problem 2 - Alternative"

def string_bits_2(str):
    return str[::2]

print string_bits_2("Hello")
print string_bits_2("Hi")
print string_bits_2("Heeololeo")

## -- PROBLEM 3 -- ##
print "Problem 3"
# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    end_a = a[-len(b):]
    end_b = b[-len(a):]
    return b in end_a or a in end_b

print end_other('Hiabc', 'abc')
print end_other('AbC', 'HiaBc')
print end_other('abc', 'abXabc')
print end_other('xyz', 'wtgrs')


## -- PROBLEM 4 -- ##
print "Problem 4"
# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    result = ""
    for letter in str:
        result += letter + letter
    return result

print double_char('The')
print double_char('AAbb')
print double_char('Hi-There')


## -- PROBLEM 5 -- ##
print "Problem 5"
# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

# def fix_teen(n):
#   if(n in list(range(13,20))):
#       if(n != 15 and n!= 16):
#           return 0
#   return n
def fix_teen(n):
  if n in [13, 14, 17, 18, 19]:
          return 0
  return n

print no_teen_sum(1, 2, 3)
print no_teen_sum(2, 13, 1)
print no_teen_sum(2, 1, 14)


## -- PROBLEM 6 -- ##
print "Problem 6"
# Return the number of even integers in the given array.

# Examples:

# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    counter = 0
    for i in nums:
        if i % 2 == 0:
            counter = counter + 1
    return counter

print count_evens([2, 1, 2, 3, 4])
print count_evens([2, 2, 0])
print count_evens([1, 3, 5])
