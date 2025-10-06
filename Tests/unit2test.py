#Question 1

first_word = input("what is your first word\n>")
second_word = input("what is your second word\n>")
third_word = input("what is your third word\n>")

print(first_word )
print(second_word )
print(third_word )






#Question 2

def add_three(x, y, z):
    print(x + y + z)

x = int(input("First number\n>"))
y = int(input("Second number\n>"))
z = int(input("Third number\n>"))

add_three(x, y, z)





#3 (3 points) Create a function called data_three that takes zero parameters. Inside of the function create three input statements that ask for a word, an integer, and a float. 
# Add the integer and the float and then concatenate that sum with the word, then print.

def data_three():
    word = input("Give me a word\n>")
    integer = input("give me a integer\n>")
    float_ = input("give me a float\n>")
    print(integer + float_ + word) 
    
data_three()





