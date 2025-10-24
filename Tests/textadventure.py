global_var = input("\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nA Cold Wind Blows on a Dark Cloudy Morning... You are born again, you rise from your deep slumber to face the world's challenges. What is your name lost one...\n>")


def start_adventure():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nhello "  + global_var +  ". What do you decide to do, type the number:")
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









#outcome 1

def exit_door():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you exit your room, you get ready to go to the place they call school. Pick what you want to eat:")
    print("1. Cereal.")
    print("2. Toast.")
    print("3. Eat nothing.")
    print("4. Eggs.")

    choice = input("> ")

    if choice == "1":
        cereal_sick()
    elif choice == "2":
        eat()
    elif choice == "3":
        hunger()
    elif choice == "4":
        eat()
    else:
        print("invalid input, Put only the number of the choice")
        exit_door()



#outcome 1 1st option

def cereal_sick():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAfter you finish eating your breakfast, you leave to school and wait at the bus stop. As you enter the bus you cant help but feel uneasy, something is wrong... you suddenly remember that your lactose intolerant... You arive at the school parking lot, what do you do:")
    print("1. Enter the school building.")
    print("2. Dont enter the school building")
    
    choice = input("> ")

    if choice == "1":
        sick_enter_school()
    elif choice == "2":
        sick_trouble()
    else:
        print("invalid input, Put only the number of the choice")
        cereal_sick()




#outcome 1 option 4 and 2
def eat():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you finish your meal, you feel energized and leave to the bus stop. When the bus arrives, you feel a sense of peace wash over yourself and say to your self, (today is gonna be a great day). You arrive at the schools parking lot, What do you decide to do:")
    print("1. Enter the school building.")
    print("2. Dont enter the school building")
    
    choice = input("> ")

    if choice == "1":
        enter_school()
    elif choice == "2":
        trouble()
    else:
        print("invalid input, Put only the number of the choice")
        eat()




#outcome 1 option 3
def hunger():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou walk to the bus stop and wait. When you enter the bus your stomach grumbles, you are hungry... You arrive at the school parking lot, what will you do:")
    print("1. Enter the school building.")
    print("2. Dont enter the school building")
    
    choice = input("> ")

    if choice == "1":
        hun_enter_school()
    elif choice == "2":
        hun_trouble()
    else:
        print("invalid input, Put only the number of the choice")
        hunger()






#outcome 1 enter school
def enter_school():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you enter the school, the sound of laughter fills the air. People are moving through the hallways so you hurry and go to your locker, but a group of kids who seem to be your age are surround around locker. What do you want to do:")
    print("1. kindly ask them to move ask for them to move.")
    print("2. start SCREAMING.")
    print("3. Shove your way through the people.")

    choice = input("> ")

    if choice == "1":
        locker()
    elif choice == "2":
        creep_locker()
    elif choice == "3":
        watch_locker()
    else:
        print("invalid input, Put only the number of the choice")
        enter_school()

def locker():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Class mate:" + "\x1B[0m" "\nOh sorry I didnt realize we were blocking your locker, (classmate speaking to the others): lets go somewhere else guys.\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\n\nWhat do you want to do next:")
    print("1. Go to class.")
    print("2. Walk around and talk to people")
    choice = input("> ")

    if choice == "1":
        go_class()
    elif choice == "2":
        socialize()
    else:
        print("invalid input, Put only the number of the choice")
        locker()

def creep_locker():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Class mate:" + "\x1B[0m" "\nThis guy is a creep... Lets leave before they do something worse.\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\n\nWhat do you want to do next:")
    print("1. Go to class.")
    print("2. Walk around and talk to people.")
    choice = input("> ")

    if choice == "1":
        go_class()
    elif choice == "2":
        socialize()
    else:
        print("invalid input, Put only the number of the choice")
        creep_locker

def watch_locker():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Class mate:" + "\x1B[0m" "\nHey, Watch were your going punk! Lets leave this kid and do something else.\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\n\nWhat do you want to do next:")
    print("1. Go to class.")
    print("2. Walk around and talk to people.")
    choice = input("> ")

    if choice == "1":
        go_class()
    elif choice == "2":
        socialize()
    else:
        print("invalid input, Put only the number of the choice")
        watch_locker()

def socialize():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou see a freindly looking person, how should you aproach them?:")
    print("1. Hello guys, how are you guys enjoying the weather")
    print("2. start SCREAMING.")
    print("3. Hello guys how is the first doay of school going?")

    choice = input("> ")

    if choice == "1":
        weather()
    elif choice == "2":
        scream_person()
    elif choice == "3":
        first_day()
    else:
        print("invalid input, Put only the number of the choice")
        go_class()


def weather():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Jim:" + "\x1B[0m" "\nOh the weather, isn't it raining right now... Well thanks for asking, Whats your name?(you respond with your name) Oh cool nice to meet you "+global_var+". we better head to class before the bell rings, by the way my name is Jim.\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhat do you want to do next:")
    print("1. Go to class.")
    choice = input("> ")

    if choice == "1":
        go_class()
    else:
        print("invalid input, Put only the number of the choice")
        weather()

def scream_person():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Jim:" + "\x1B[0m" "\nWoah a crazy fellow you are whats your name(you tell him your name).Well " + global_var+  " What brings you here screaming like that?:")
    print("1. I dont know, I guess something urged me to scream.")
    print("2. I wanted be diffrent.")
    print("3. SCREAM")

    choice = input("> ")

    if choice == "1":
        response()
    elif choice == "2":
        response()
    elif choice == "3":
        response()
    else:
        print("invalid input, Put only the number of the choice")
        scream_person()

def response():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Jim:" + "\x1B[0m" "\nIntresting... Well we better go to class, cya.\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhat do you want to do next:")
    print("1. Go to class.")
    choice = input("> ")

    if choice == "1":
        go_class()
    else:
        print("invalid input, Put only the number of the choice")
        response()



def go_class():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\n When you enter the class the teacher starts calling out names for attendance\n\n\x1B[4m" + "Ms. Cornealius:" + "\x1B[0m" "\nIS James HERE!\n\n\x1B[4m" + "James:" + "\x1B[0m" "\nPresent!\n\n\x1B[4m" + "Ms. Cornealius:" + "\x1B[0m" "\nIS " + global_var+" HERE!\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nHow do you respond:")
    print("1. Present!")
    print("2. start SCREAMING.")
    print("3. Say nothing in embarresment.")

    choice = input("> ")

    if choice == "1":
        present()
    elif choice == "2":
        scream_attendance()
    elif choice == "3":
        shy()
    else:
        print("invalid input, Put only the number of the choice")
        go_class()







start_adventure()


















