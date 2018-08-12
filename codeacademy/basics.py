print "Python 2 print"
print("Python 3 print")
"""Triple quotes for
multi-line comments"""

a_true = True # 1
a_false = False # 0

an_int = 5
a_float = float(an_int)
a_string = str(a_float)
# Print cannot concatenate different types (TypeError)
print("To print the float with a string: " + str(a_float))

# STRINGS
single_quote = 'Still a string'
apostrophe = "This isn\'t a broken string."
index = "PYTHON"[0] # P!
len("length of string")
print "MAKE LOWERCASE".lower()
print "make uppercase".upper()
# len() & str() can be called on other datatypes
# .lower() & .upper() only apply to strings
print "03 - %02d - 2019" % (6) # pad with zeros, 2 characters wide
print "Appending two strings: %s and %s" % ("one", "two")
console_input = raw_input("Give me any string input:")
print "Thanks for giving me " + console_input

# DATETIME LIBRARY