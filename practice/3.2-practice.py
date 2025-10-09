"""
if condition:
    # Code to execute if the condition is true





#if statement independent prints whatver vaulue is lower or higher

number = 5

if number > 0:
    print("The number is positive")




#else needs a if before the else, dependent. Like a fork in the road only one or the other can happen. If the if statement is false then the else statement comes into play.

number = -3

if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")




anwser_one = input("what is 2 plus 2?\n>")
print(answer_one == "4")

"""

a = 0
b = 11
c = 52

#can only run one false is plum true is kiwi.






if a < 0:
    print("kiwi")

else:
    print("plum")





#simple password checks if your input is the same as the key. 



def check_password():
    password_given = input("what is the password\n>")
    password = "Hello100"

    if  password_given == password:
        print("password correct")
    else:
        print("password incorrect")
        check_password()





check_password()

















