# ERRORS AND EXCEPTIONS

# SYNTAX ERROR --> THIS TYPE OF ERROR IS DISPLAYED IN THE IDE
# print('hello)

# NAME ERROR --> THIS TYPE OF ERROR IS DISPLAYED IN THE IDE
# mylist = [1,2,3]
# print(thisnewlist)

# WRITE IN A TEXT FILE
print("-------- Write in a text file - Success case --------")
try:
    textfile = open('14_errors_exceptions_text.txt', 'w')
    textfile.write("Write a new line in the text file")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA")
else:
    print("SUCCESS!")
    textfile.close()
print("The code reached this line")

# WRITE IN A TEXT FILE THAT IS OPEN WITH THE 'read' PARAMETER --> ERROR
print("-------- Write in a text file - Error case --------")
try:
    textfile = open('14_errors_exceptions_text.txt', 'r')
    textfile.write("Write a new line in the text file")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA")
else:
    print("SUCCESS!")
    textfile.close()
print("The code reached this line")


# textfile = open('14_errors_exceptions_text.txt', 'r')
# textfile.write("Write a new line in the text file")
# print("The code doesn't reach this line")

# USING GENERIC EXCEPTIONS
print("-------- Write in a text file - Generic exception --------")
try:
    textfile = open('14_errors_exceptions_text.txt', 'r')
    textfile.write("Write a new line in the text file")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA")
finally:
    print("EXECUTE THIS LINE OF CODE ALWAYS")