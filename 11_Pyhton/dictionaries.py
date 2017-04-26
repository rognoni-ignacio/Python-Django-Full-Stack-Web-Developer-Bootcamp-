### Dictionaries ###

# We've been learning about sequences in Python but now we're going to switch
# gears and learn about "mappings' in Python. If you're familiar with other
# languages you can think of these Dictionaries as hash tables (objects in Javascript).

# So what are mappings? Mappings are a collection of objects that are stored by
# a key, unlike a sequence that stored objects by their relative position.
# This is an important distinction, since mappings won't retain order since they
# have objects defined by a key.
#
# A Python dictionary consists of a key and then an associated value. That value
# can be almost any Python object.
#
# Constructing a Dictionary
# Let's see how we can construct dictionaries to get a better understanding of how they work!

# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}

# Call values by their key
print("Call Key2 of my dictionary")
print(my_dict['key2'])


# Its important to note that dictionaries are very flexible in the data types
# they can hold. For example:

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

#Lets call items from the dictionary
print("Call Key3 of my dictionary")
print(my_dict['key3'])

# Can call an index on that value
print("Call item 0 of key 3 in my dictionary")
print(my_dict['key3'][0])

#Can then even call methods on that value
print("Call item 0 of key 3 in my dictionary using upper()")
print(my_dict['key3'][0].upper())

# We can effect the values of a key as well. For instance:
print("Affecting a dictionary value is permanent")
print("Before the change")
print(my_dict['key1'])

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123

#Check
print("After the change")
print(my_dict['key1'])


# A quick note, Python has a built-in method of doing a self subtraction or
# addition (or multiplication or division). We could have also used += or -= for
# the above statement. For example:

# Set the object equal to itself minus 123
print("Affect the value itself")
my_dict['key1'] -= 123
print(my_dict['key1'])


# We can also create keys by assignment. For instance if we started off with an
# empty dictionary, we could continually add to it:

# Create a new dictionary
d = {}

# Create a new key through assignment
d['animal'] = 'Dog'

# Can do this with any object
d['answer'] = 42

#Show
print(d)


# Nesting with Dictionaries ###
print("Nesting dictionaries")

# Hopefully your starting to see how powerful Python is with its flexibility of
# nesting objects and calling methods on them. Let's see a dictionary nested
# inside a dictionary:

# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}


# Wow! Thats a quite the inception of dictionaries!
# Let's see how we can grab that value:

# Keep calling the keys
print("Nested dictionary")
print(d['key1']['nestkey']['subnestkey'])


#### A few Dictionary Methods ####
print("Dictionary Methods")
# There are a few methods we can call on a dictionary.
# Let's get a quick introduction to a few of them:

# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}

# Method to return a list of all keys
print("Return all keys")
print(d.keys())

# Method to grab all values
print("Return all values")
print(d.values())

# Method to return tuples of all items  (we'll learn about tuples soon)
print("Return all items")
print(d.items())
