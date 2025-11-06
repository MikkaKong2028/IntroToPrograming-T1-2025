"""import random 


def rps(rock, paper, scissors):
    


    action= ["rock", "paper", "scissors"]
    p1 = random.choice(action)

    print(p1)
    



    action= ["rock", "paper", "scissors"]
    p2 = random.choice(action)

    print(p2)
    
    if p1 == "rock" and p2 == "scissors":
        print("Player 1 won!")
    elif p1 == "scissors" and p2 == "rock":
        print("Player 2 won!")
    elif p1 == "paper" and p2 == "rock":
        print("Player 1 won!")
    elif p1 == "rock" and p2 == "paper":
        print("Player 2 won!")
    elif p1 == "scissors" and p2 == "paper":
        print("Player 1 won!")
    elif p1 == "paper" and p2 == "scissors":
        print("Player 2 won!")
    elif p1 == "scissors" and p2 == "paper":
        print("Player 2 won!")
    elif p1 == "scissors" and p2 == "rock":
        print("Player 2 won!")
    elif p1 == "paper" and p2 == "rock":
        print("Player 1 won!")
    elif p1 == "rock" and p2 == "paper":
        print("Player 2 won!")
    else:
        print("Draw!")
rps("rock", "paper", "scissors")    

"""

"""
def start_adventure():
    print("You stand at the entrance of a dark forest. Do you:")
    print("1. Enter the forest")
    print("2. Turn back and go home")

    choice = input("> ")

    if choice == "1":
        enter_forest()
    elif choice == "2":
        go_home()
    else:
        print("Invalid choice. Try again.")
        start_adventure()

def enter_forest():
    print("You bravely step into the forest and hear strange noises...")
    # More encounters and choices follow

def go_home():
    print("You decide it's safer at home, but your adventure ends here.")
    # End of the game or new encounters

"""
"""
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")

#    \n\n\n\n---------------------------------------------------------------------------------------------------------------\n line spacing between questions

name = global_var = input("A Cold Wind Blows on a Dark Cloudy Morning... You are born again, you rise from your deep slumber to face the world's challenges. What is your name lost one...\n>")


def start_adventure(name):
    print("\n-\n-\n-\n-\n-\n-\n-\nhello " + name +". What do you decide to do, type the number:")
    print("1. Exit your room through a door and the only place you know to be home.")
    print("2. go back to into your den for a deep slumber.")
    print("3. Exit your room through a window an the only place you know to be home")
    print("4. Complain and scream.")

    choice = input("> ")

    if choice == "1":
        exit_door()
    elif choice == "2":
        sleep()
    elif choice == "3":
         exit_window()
    elif choice == "4":
         scream()
    else:
        print("invalid input, Put only the number of the choice")
        start_adventure()
"""

"""
def school_adventure():
    global_var = input("Inner voice...  A Cold Wind Blows on a Dark Cloudy Morning... You are born again, you rise from your deep slumber to face the world's challenges. What is your name lost one...\n>")
    if global_var != "":
        start_adventure()
    else:
        print("invalid input, Please type a username.")
        school_adventure()

    def start_adventure():
        print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\nhello " + global_var +". What do you decide to do, type the number:")
        print("1. Exit your room through a door and leave the only place you know to be home.")
        print("2. go back to into your den for a deep slumber.")
        print("3. Exit your room through a window and leave the only place you know to be home")
        print("4. Complain and scream.")

        choice = input("> ")

        if choice == "1":
            exit_door()         #outcome 1
        elif choice == "2":
            sleep()             #outcome 2
        elif choice == "3":
            exit_window()       #outcome 3
        elif choice == "4":
            scream()            #outcome 4
        else:
            print("invalid input, Put only the number of the choice")
            start_adventure()

school_adventure()"""





num = [10,9,8,7,6,5,4,3,2,1]

for count in num: #for each individual game in the games variable print all the games in a loop. game = each of these but goes around in a loop 
    print(count)


games = [10,9,8,7,6,5,4,3,2,1]

for game in games: #for each individual game in the games variable print all the games in a loop. game = each of these but goes around in a loop 
    print(game)



