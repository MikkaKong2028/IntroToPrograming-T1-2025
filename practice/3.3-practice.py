"""# String functions1
# A group of like-functions that manipulate strings
# The modify strings
# SUPER easy and convenient to use
# Python would really not be fun without them

#   .lower()
# converts a string to all lowercase
# no matter what the input casing is, it is converted to lowercase
# and the answer is lowercase
input_answer = "Lord of The Rings"
input_answer = input_answer.lower() # Converts to "lord of the rings"
real_answer = "lord of the rings"
print(input_answer == real_answer)

# .upper()
# Converts a string to uppercase!
x = "hello world".upper()
print(x)    # prints "HELLO WOLRD"

# .capitalize()
# converts to lowercase, then capitalizes the first letter
y = "HeLlO wOrLd".capitalize()
print(y)    # print "Hello world"

# .title()
# converts a string to titlecase
#capital first letters of words
z = "HeLlO wOrLd".title()
print(z)    # print "Hello World"

# .swapcase()
# it inverts the casing of eac character
q = "Hello World!".swapcase()
print(q)    #prints "hELLO wORLD!"



# the if statement has two buddies
# the first little buddy is the the else statement

x = 10

if x > 0:   # not every if needs an else
    print("x is a postiive number")

# the second little buddy is the elif (else if)
elif x < 0:
    print("x is a negative number")

else:       # else always needs an if
    print("x is zero")



light = input("What color is the light?\n>")

if light.lower() == "green":
    print("GO")

elif light.lower() == "yellow":
    print("STOP IF SAFE")

elif light.lower() == "red":
    print("STOP")

else:
    print("YIELD")



x = 10

if x > 5:
    print("x is greater than 5")

if x > 8:
    print("x is greater than 8")

####################################
if x > 5:
    print("x is greater than 5")

elif x > 8:
    print("x is greater than 8")
# Example of string functions

text = " hello world "

# Uppercase
print(text.upper())  # Output: " HELLO WORLD "

# Lowercase
print(text.lower())  # Output: " hello world "

# Capitalize
print(text.capitalize())  # Output: " hello world "

# Title
print(text.title())  # Output: " Hello World "

# Strip whitespace
print(text.strip())  # Output: "hello world"

# Replace
new_text = text.replace("world", "Python")
print(new_text)  # Output: " hello Python "

# Split
words = "one,two,three".split(",")
print(words)  # Output: ['one', 'two', 'three']

# Join
joined_text = "-".join(["a", "b", "c"])
print(joined_text)  # Output: "a-b-c"

# Find
index = text.find("o")
print(index)  # Output: 4

# Endswith
is_txt_file = "filename.txt".endswith(".txt")
print(is_txt_file)  # Output: True
"""


sentence = input("write a a sentence\n>")
print(sentence.upper().strip().replace("bad", "good"))



if sentence.endswith("."):
    print("true")

else:
    print("false")



















