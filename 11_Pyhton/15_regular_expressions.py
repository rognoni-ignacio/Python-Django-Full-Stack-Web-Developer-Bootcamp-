# REGULAR EXPRESSIONS

# IMPORT MODULE
import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, not the other term'

for pattern in patterns:
    print("I'm searching for: " + pattern)

    if re.search(pattern, text):
        print("MATCH")
    else:
        print("NO MATCH!")

 # USING MATCH FUNCTION
print("--- USING MATCH FUNCTION ---")
text = 'term1'
match = re.search('term1', text)
print(match)
# OBJECT MATCH CONTAINS INFORMATION ABOUT THE MATCH
print(match.start())
print(match.end())

# USING SPLIT
split_term = '@'
email = 'user@email.com'
print(re.split(split_term, email))

# GET ALL MATCHES
print(re.findall('match','test phrase match is in middle'))
print(re.findall('match','test phrase match is in middle match'))

# USING FUNCTIONS
print("--- USING FUNCTION FOR FINDING MULTIPLE PATTERNS ---")
def multi_re_find(patterns, phrase):
    
    for pattern in patterns:
        print("Searching for pattern {}".format(pattern))
        print(re.findall(pattern, phrase))
        print('\n')

phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
#LOOK FOR S, FOLLOWED BY 0 OR MORE D's
# patterns = ['sd*']

#LOOK FOR S, FOLLOWED BY 1 OR MORE D's
# patterns = ['sd+']

#LOOK FOR S, FOLLOWED BY 0 OR 1 D
# patterns = ['sd?']

#LOOK FOR S, FOLLOWED BY N D's
# patterns = ['sd{3}']

#LOOK FOR S, FOLLOWED BY N OR M D's
# patterns = ['sd{1,3}']

# LOOK FOR S, FOLLOWED BY ONE OR MORE S's OR D's
# patterns = ['s[sd]+']

multi_re_find(patterns, phrase)

# EXCLUSIONS
phrase = 'This is a string! Buit it has punctuation. How can we remove it?'

# LOOK FOR ONE OR MORE INSTANCES OF !, ., ? 
# patterns = ['[^!.?]+']

# LOOK FOR LOWERCASE CHARACTERS
# patterns = ['[a-z]+']

# LOOK FOR UPPERCASE CHARACTERS
# patterns = ['[A-Z]+']

phrase = 'This is a string with numbers 12312 and a symbol #hastag'

# LOOK FOR DIGIT CHARACTERS
# patterns = [r'\d+']

# LOOK FOR NON DIGIT CHARACTERS
# patterns = [r'\D+']

# LOOK FOR WHITESPACES
# patterns = [r'\s+']

# LOOK FOR NON WHITESPACES
# patterns = [r'\S+']

# LOOK FOR ALPHANUMERIC
# patterns = [r'\w+']

# LOOK FOR NON ALPHANUMERIC
patterns = [r'\W+']

multi_re_find(patterns, phrase)