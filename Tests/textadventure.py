
import random


global_var = input("\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nA Cold Wind Blows on a Dark Cloudy Morning... You are born again, you rise from your deep slumber to face the world's challenges. What is your name lost one...\n>")


def start_adventure():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nhello "  + global_var +  ". What do you decide to do, type the number:")
    print("1. Exit your room through a door and leave the only place you know to be home.")
    print("2. go back to into your den for a deep slumber.")
    print("3. Exit your room through a window and leave the only place you know to be home")
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
def sleep():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou decide to go back into a deep slumber. As you do you suddenly wake up hours later to the angry sound of your mother yelling at you to get up and get ready for school. What do you want do next:")
    print("1. Get ready for school.")
    print("2. Ignore your mom.")
    print("3. yell back at your mom.")
    print("4. Complain and scream.")

    choice = input("> ")

    if choice == "1":
        late()         
    elif choice == "2":
        sleep_again()             
    elif choice == "3":
        yell()       
    elif choice == "4":
        yell()           
    else:
        print("invalid input, Put only the number of the choice")
        sleep()

def yell(): 
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you begin to yell in frustration your mother walks in and yells back. After the tantrum you get in the car and head to school late. When you arrive at school you got to 2nd hour becuase of how late you showed up. Shortly after you arrive find yourself in second hour english class with the teacher beggining to talk.\n\n\n\x1B[4m" + "Ms, fiddle:" + "\x1B[0m" "\nAll right kids, settle down! Today we will be doing speeches! (The kids faces turn blue) yes, yes I know harsh for the firt day. But you know, if you dont challenge yourself you wont get better at things, so get ready to share something about this summer to your class.\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhat do you want to do next:")
    print("1. Talk about how you bed rot all summer")
    print("2. start SCREAMING.")
    print("3. Say nothing when you go up")

    choice = input("> ")

    if choice == "1":
        bed_rot()
    elif choice == "2":
        scream_speech()
    elif choice == "3":
        quiet()
    else:
        print("invalid input, Put only the number of the choice")
        late() 

def scream():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou decide to scream at the top of your lungs. This wakes up your mother and she scolds you for yelling early in the morning. After letting out that scream, you feel like you can take on the worlds challenges so you start getting ready. What do you want to eat for breakfast:")
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
        scream()
def late():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you get in the car your mom scolds you for trying to skip school. When you arrive at school you got to 2nd hour becuase of how late you showed up. Shortly after you arrive find yourself in second hour english class with the teacher beggining to talk.\n\n\n\x1B[4m" + "Ms, fiddle:" + "\x1B[0m" "\nAll right kids, settle down! Today we will be doing speeches! (The kids faces turn blue) yes, yes I know harsh for the firt day. But you know, if you dont challenge yourself you wont get better at things, so get ready to share something about this summer to your class.\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhat do you want to do next:")
    print("1. Talk about how you bed rot all summer")
    print("2. start SCREAMING.")
    print("3. Say nothing when you go up")

    choice = input("> ")

    if choice == "1":
        bed_rot()
    elif choice == "2":
        scream_speech()
    elif choice == "3":
        quiet()
    else:
        print("invalid input, Put only the number of the choice")
        late() 


def sleep_again():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nJust minutes before you try to fall asleep again your mom busts through the door and smacks you on the head and begins lecuturing you.\n\n\n\x1B[4m" + "Mom:" + "\x1B[0m" "\nYOU'VE GOT SOME NERVE IGNORING ME LIKE THAT! HURRY UP, NO TIME TO EAT.\n\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you get in the car your mom scolds you again for trying to skip school. When you arrive at school you got to 2nd hour becuase of how late you showed up. Shortly after you arrive find yourself in second hour english class with the teacher beggining to talk.\n\n\n\x1B[4m" + "Ms, fiddle:" + "\x1B[0m" "\nAll right kids, settle down! Today we will be doing speeches! (The kids faces turn blue) yes, yes I know harsh for the firt day. But you know, if you dont challenge yourself you wont get better at things, so get ready to share something about this summer to your class.\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhat do you want to do next:")
    print("1. Talk about how you bed rot all summer")
    print("2. start SCREAMING.")
    print("3. Say nothing when you go up")

    choice = input("> ")

    if choice == "1":
        bed_rot()
    elif choice == "2":
        scream_speech()
    elif choice == "3":
        quiet()
    else:
        print("invalid input, Put only the number of the choice")
        late() 




def exit_window():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you inch tomwards the window you are filled with the thought of confusion and wondering why or rather WHO would ever want to jump out a window? None the less you open the window and jump out... Thats when you remember that you sleep on the second floor and it faces your \nbackyard with a steep hill that leads to a lake. As you fall you start to regret you decision while you break your leg on impact. After landing you roll down the steep hill unable to stop and you start drowining in the supprisingly deep lake. What do you want to do now:")
    print("1. attempt to swim out")
    print("2. give up and drown.")
    
    choice = input("> ")

    if choice == "1":
        swim()
    elif choice == "2":
        die()
    else:
        print("invalid input, Put only the number of the choice")
        exit_window()











def die(): #bad ending
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you sink deeper and deeper in the lake you exept death as a option. Each passing second you feel the life being drained from your eyes and the air from your lungs depleat. after 2 minutes your body has no choice but to sucumb to the darkness... Congrats, you got the \x1B[4m" + "'Bad'" + "\x1B[0m" " ending")












def swim(): #1 in 3 chance to live
    random_int = random.randint(1, 3)
    if random_int == 1:#bad ending
        print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you thrash around in the water trying to escape you feel he air in your lungs get thinner and thinner until the light starts to fade from your eyes... Congrats, you got the \x1B[4m" + "'Bad'" + "\x1B[0m" " ending ")
    
    if random_int == 2:#bad ending
        print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you thrash around in the water trying to escape you feel he air in your lungs get thinner and thinner until the light starts to fade from your eyes... Congrats, you got the \x1B[4m" + "'Bad'" + "\x1B[0m" " ending ")

    if random_int == 3:#survivor ending 
        print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you try your hardest to swim out of the lake but you just cant each second you feel air leaving you lungs and you start to see darkness... Suddenly you are pulled out of the water by your neighbor and quikly brought to a hospital. You eventualy wake to the sound of medical \nbeeping and cheering. As you talk to the doctors, they imform you that you've been in a coma for a week. Congrats, you got the \x1B[4m" + "'Survivior'" + "\x1B[0m" " ending")




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



def sick_trouble():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you sit outside the school waiting for nothing the bell rings, you are now late and missing from class. As you sit outside the school wondering why you decided on not to enter, a teacher spots you and is about to bring you to class. Before he could talk to you, you suddenly feel stomach acids rise and you barf all over the side walk. The teacher brings you to the nurses office instead where you are told to rest. What do you want to do next:")
    print("1. Ask to go home")
    print("2. Go to class")
    print("3. Go to sleep")
    choice = input("> ")

    if choice == "1":
        go_home()
    elif choice == "2":
        english1()
    elif choice == "3":
        english1()
    else:
        print("invalid input, Put only the number of the choice")
        sick_trouble()





def sick_enter_school():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you enter the school, the sound of laughter fills the air. People are moving through the hallways so you hurry and go to your locker, but a group of kids who seem to be your age are surround around locker. What do you want to do:")
    print("1. kindly ask them to move ask for them to move.")
    print("2. start SCREAMING.")
    print("3. Shove your way through the people.")

    choice = input("> ")

    if choice == "1":
        sick_nurse()
    elif choice == "2":
        sick_nurse()
    elif choice == "3":
        sick_nurse()
    else:
        print("invalid input, Put only the number of the choice")
        sick_enter_school()

def sick_nurse():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you approach them you suddenly feel ill and feel the stomach acids rising. Before anyone could act you barf all over the floor in front of the kids. As soon as you do the kids flee and you can enter your locker, but before you could enter you are stoped by the nurse and brought to the office to rest. What do you want to do next:")
    print("1. Ask to go home")
    print("2. Go to class")
    print("3. Go to sleep")
    choice = input("> ")

    if choice == "1":
        go_home()
    elif choice == "2":
        english1()
    elif choice == "3":
        english1()
    else:
        print("invalid input, Put only the number of the choice")
        sick_nurse()







def go_home():#sick ending
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhen you as the nurse if you can go home she calls your mom to pick you up, after a couple minutes your mom arrives to take you home. When you open the car door your mom greets you with a concerned look, as you arrive at home you're overjoyed that you made it back home. Congrats you found the \x1B[4m" + "'sick'" + "\x1B[0m" " ending")













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

def trouble():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you sit outside the school waiting for nothing the bell rings, you are now late and missing from class. As you sit outside the school wondering why you decided on not to enter, a teacher spots you and brings you inside class. When you enter the class the teacher starts calling out names for attendance\n\n\x1B[4m" + "Ms. Cornealius:" + "\x1B[0m" "\nIS James HERE!\n\n\x1B[4m" + "James:" + "\x1B[0m" "\nPresent!\n\n\x1B[4m" + "Ms. Cornealius:" + "\x1B[0m" "\nIS " + global_var+" HERE!\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nHow do you respond:")
    print("1. Present!")
    print("2. start SCREAMING.")
    print("3. Say nothing in embarresment.")

    choice = input("> ")

    if choice == "1":
        present()
    elif choice == "2":
        scream_attendence()
    elif choice == "3":
        shy()
    else:
        print("invalid input, Put only the number of the choice")
        trouble()



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
def hun_trouble():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhen you enter the class the teacher starts calling out names for attendance\n\n\x1B[4m" + "Ms. Cornealius:" + "\x1B[0m" "\nIS James HERE!\n\n\x1B[4m" + "James:" + "\x1B[0m" "\nPresent!\n\n\x1B[4m" + "Ms. Cornealius:" + "\x1B[0m" "\nIS " + global_var+" HERE!\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nHow do you respond:")
    print("1. Present!")
    print("2. start SCREAMING.")
    print("3. Say nothing in embarresment.")

    choice = input("> ")

    if choice == "1":
        attendence_hun()
    elif choice == "2":
        attendence_hun()
    elif choice == "3":
        attendence_hun()
    else:
        print("invalid input, Put only the number of the choice")
        hun_trouble()


def hun_enter_school():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs you enter the school, the sound of laughter fills the air. People are moving through the hallways so you hurry and go to your locker, but a group of kids who seem to be your age are surround around locker. What do you want to do:")
    print("1. kindly ask them to move ask for them to move.")
    print("2. start SCREAMING.")
    print("3. Shove your way through the people.")

    choice = input("> ")

    if choice == "1":
        locker_hun()
    elif choice == "2":
        creep_locker_hun()
    elif choice == "3":
        watch_locker_hun()
    else:
        print("invalid input, Put only the number of the choice")
        hun_enter_school()

def locker_hun():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Class mate:" + "\x1B[0m" "\nOh sorry I didnt realize we were blocking your locker, (classmate speaking to the others): lets go somewhere else guys.\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\n\nWhat do you want to do next:")
    print("1. Go to class.")
    print("2. Walk around and talk to people")
    choice = input("> ")

    if choice == "1":
        go_class_hun()
    elif choice == "2":
        socialize_hun()
    else:
        print("invalid input, Put only the number of the choice")
        locker_hun()


def creep_locker_hun():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Class mate:" + "\x1B[0m" "\nThis guy is a creep... Lets leave before they do something worse.\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhat do you want to do next:")
    print("1. Go to class.")
    print("2. Walk around and talk to people.")
    choice = input("> ")

    if choice == "1":
        go_class_hun()
    elif choice == "2":
        socialize_hun()
    else:
        print("invalid input, Put only the number of the choice")
        creep_locker_hun()


def watch_locker_hun():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Class mate:" + "\x1B[0m" "\nHey, Watch were your going punk! Lets leave this kid and do something else.\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\n\nWhat do you want to do next:")
    print("1. Go to class.")
    print("2. Walk around and talk to people.")
    choice = input("> ")

    if choice == "1":
        go_class_hun()
    elif choice == "2":
        socialize_hun()
    else:
        print("invalid input, Put only the number of the choice")
        watch_locker_hun()


def socialize_hun():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou see a freindly looking person, how should you aproach them?:")
    print("1. Hello, how are you enjoying the weather today")
    print("2. start SCREAMING.")
    print("3. Hello how is the first day of school going?")

    choice = input("> ")

    if choice == "1":
        hun_conversation()
    elif choice == "2":
        hun_conversation()
    elif choice == "3":
        hun_conversation()
    else:
        print("invalid input, Put only the number of the choice")
        socialize_hun()


def hun_conversation():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou see a freindly looking person, how should you aproach them?:")
    print("1. Hello, how are you enjoying the weather today")
    print("2. start SCREAMING.")
    print("3. Hello how is the first day of school going?")

    choice = input("> ")

    if choice == "1":
        weather()
    elif choice == "2":
        scream_person()
    elif choice == "3":
        first_day()
    else:
        print("invalid input, Put only the number of the choice")
        hun_conversation()




def go_class_hun():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhen you enter the class the teacher starts calling out names for attendance\n\n\x1B[4m" + "Ms. Cornealius:" + "\x1B[0m" "\nIS James HERE!\n\n\x1B[4m" + "James:" + "\x1B[0m" "\nPresent!\n\n\x1B[4m" + "Ms. Cornealius:" + "\x1B[0m" "\nIS " + global_var+" HERE!\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nHow do you respond:")
    print("1. Present!")
    print("2. start SCREAMING.")
    print("3. Say nothing in embarresment.")

    choice = input("> ")

    if choice == "1":
        attendence_hun()
    elif choice == "2":
        attendence_hun()
    elif choice == "3":
        attendence_hun()
    else:
        print("invalid input, Put only the number of the choice")
        go_class_hun()

def attendence_hun():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nBefore you could say a word your stomach growls violently and the class erupts into laughter then you tell the teacher your present. homeroom eventualy ends and you find yourself in first hour math class. You are tasked with solving review problems for math class input only numbers.\n\n")
    question_1 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n2+2 = ")
    question_2 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n3+9 = ")
    question_3 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n4+1 = ")
    question_4 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n5-2 = ")
    question_5 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n4+8 = ") 
    question_6 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n40 / 4 = ")
    question_7 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n7^2 = ")
    question_8 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n9 x 0 = ")
    question_9 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n8 x 3 - 7 = ")
    question_10 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n2274 x 2223 = ")


    score = 0
    
    if  question_5.lower() == "12":
        score = score + 1
        

    if  question_4.lower() == "3":
        score = score + 1
   


    if  question_3.lower() == "5":
        score = score + 1

    

    if  question_2.lower() == "12":
        score = score + 1



    if  question_1.lower() == "4":#makes it lowercse can be used to fix spelling error for upper and lower case
        score = score + 1   



    if  question_6.lower() == "10":
        score = score + 1
        
    
    
    if  question_7.lower() == "49":
        score = score + 1



    if  question_8.lower() == "0":
        score = score + 1




    if  question_9.lower() == "17":
        score = score + 1




    if  question_10.lower() == "5,055,102" or "5055102":
        score = score + 1
    print("SCORE: " + str(score) + "/10")
    english()



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
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Class mate:" + "\x1B[0m" "\nThis guy is a creep... Lets leave before they do something worse.\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhat do you want to do next:")
    print("1. Go to class.")
    print("2. Walk around and talk to people.")
    choice = input("> ")

    if choice == "1":
        go_class()
    elif choice == "2":
        socialize()
    else:
        print("invalid input, Put only the number of the choice")
        creep_locker()

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
    print("1. Hello, how are you enjoying the weather today")
    print("2. start SCREAMING.")
    print("3. Hello how is the first day of school going?")

    choice = input("> ")

    if choice == "1":
        weather()
    elif choice == "2":
        scream_person()
    elif choice == "3":
        first_day()
    else:
        print("invalid input, Put only the number of the choice")
        socialize()

def first_day():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Jim:" + "\x1B[0m" "\nOh todays fine, thanks for asking. Whats your name? (You tell him your name)Oh cool, well then nice to meet you " + global_var +" Ill catch you later we better head yo class before its too late.")
    print("1. Go to class.")
    print("2. Walk around and talk to people.")
    choice = input("> ")

    if choice == "1":
        go_class()
    elif choice == "2":
        socialize()
    else:
        print("invalid input, Put only the number of the choice")
        first_day()

def weather():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Jim:" + "\x1B[0m" "\nOh the weather, isn't it raining right now... Well thanks for asking, Whats your name? (you respond with your name) Oh cool nice to meet you "+global_var+". We better head to class before the bell rings, by the way my name is Jim.\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhat do you want to do next:")
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
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhen you enter the class the teacher starts calling out names for attendance\n\n\x1B[4m" + "Ms. Cornealius:" + "\x1B[0m" "\nIS James HERE!\n\n\x1B[4m" + "James:" + "\x1B[0m" "\nPresent!\n\n\x1B[4m" + "Ms. Cornealius:" + "\x1B[0m" "\nIS " + global_var+" HERE!\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nHow do you respond:")
    print("1. Present!")
    print("2. start SCREAMING.")
    print("3. Say nothing in embarresment.")

    choice = input("> ")

    if choice == "1":
        present()
    elif choice == "2":
        scream_attendence()
    elif choice == "3":
        shy()
    else:
        print("invalid input, Put only the number of the choice")
        go_class()

def shy():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nUnsuprisingly the teacher marks you absent for homeroom. homeroom eventualy ends and you find yourself in first hour math class. You are tasked with solving review problems for math class input only numbers.\n\n")
    question_1 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n2+2 = ")
    question_2 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n3+9 = ")
    question_3 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n4+1 = ")
    question_4 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n5-2 = ")
    question_5 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n4+8 = ") 
    question_6 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n40 / 4 = ")
    question_7 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n7^2 = ")
    question_8 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n9 x 0 = ")
    question_9 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n8 x 3 - 7 = ")
    question_10 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n2274 x 2223 = ")


    score = 0
    
    if  question_5.lower() == "12":
        score = score + 1
        

    if  question_4.lower() == "3":
        score = score + 1
   


    if  question_3.lower() == "5":
        score = score + 1

    

    if  question_2.lower() == "12":
        score = score + 1



    if  question_1.lower() == "4":#makes it lowercse can be used to fix spelling error for upper and lower case
        score = score + 1   



    if  question_6.lower() == "10":
        score = score + 1
        
    
    
    if  question_7.lower() == "49":
        score = score + 1



    if  question_8.lower() == "0":
        score = score + 1




    if  question_9.lower() == "17":
        score = score + 1




    if  question_10.lower() == "5055102":
        score = score + 1
    print("SCORE: " + str(score) + "/10")
    english()






def scream_attendence():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nThe marks your name off but now all the other kids are looking at you with disgusted facial reactions. homeroom eventualy ends and you find yourself in first hour math class. You are tasked with solving review problems for math class input only numbers.\n\n ")
    question_1 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n2+2 = ")
    question_2 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n3+9 = ")
    question_3 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n4+1 = ")
    question_4 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n5-2 = ")
    question_5 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n4+8 = ") 
    question_6 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n40 / 4 = ")
    question_7 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n7^2 = ")
    question_8 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n9 x 0 = ")
    question_9 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n8 x 3 - 7 = ")
    question_10 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n2274 x 2223 = ")


    score = 0
    
    if  question_5.lower() == "12":
        score = score + 1
        

    if  question_4.lower() == "3":
        score = score + 1
   


    if  question_3.lower() == "5":
        score = score + 1

    

    if  question_2.lower() == "12":
        score = score + 1



    if  question_1.lower() == "4":#makes it lowercse can be used to fix spelling error for upper and lower case
        score = score + 1   



    if  question_6.lower() == "10":
        score = score + 1
        
    
    
    if  question_7.lower() == "49":
        score = score + 1



    if  question_8.lower() == "0":
        score = score + 1




    if  question_9.lower() == "17":
        score = score + 1




    if  question_10.lower() == "5055102":
        score = score + 1
    print("SCORE: " + str(score) + "/10")
    english()




def present():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs the teacher marks your name off, homeroom eventualy ends and you find yourself in first hour math class. You are tasked with solving review problems for math class input only numbers.\n\n ")
    question_1 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n2+2 = ")
    question_2 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n3+9 = ")
    question_3 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n4+1 = ")
    question_4 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n5-2 = ")
    question_5 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n4+8 = ") 
    question_6 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n40 / 4 = ")
    question_7 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n7^2 = ")
    question_8 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n9 x 0 = ")
    question_9 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n8 x 3 - 7 = ")
    question_10 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n2274 x 2223 = ")


    score = 0
    
    if  question_5.lower() == "12":
        score = score + 1
        

    if  question_4.lower() == "3":
        score = score + 1
   


    if  question_3.lower() == "5":
        score = score + 1

    

    if  question_2.lower() == "12":
        score = score + 1



    if  question_1.lower() == "4":#makes it lowercse can be used to fix spelling error for upper and lower case
        score = score + 1   



    if  question_6.lower() == "10":
        score = score + 1
        
    
    
    if  question_7.lower() == "49":
        score = score + 1



    if  question_8.lower() == "0":
        score = score + 1




    if  question_9.lower() == "17":
        score = score + 1




    if  question_10.lower() == "5055102":
        score = score + 1
    print("SCORE: " + str(score) + "/10")
    english()
  
def english():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nShortly after you finish your quiz the bell rings and you find yourself in second hour english class with the teacher beggining to talk.\n\n\n\x1B[4m" + "Ms, fiddle:" + "\x1B[0m" "\nAll right kids, settle down! Today we will be doing speeches (The kids faces around turn blue as their voices shut) yes, yes I know harsh for the firt day. But you know, if you dont challenge yourself you wont get better at things, so get ready to share something about this summer to your class.\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhat do you want to do next:")
    print("1. Talk about how you bed rot all summer")
    print("2. start SCREAMING.")
    print("3. Say nothing when you go up")

    choice = input("> ")

    if choice == "1":
        bed_rot()
    elif choice == "2":
        scream_speech()
    elif choice == "3":
        quiet()
    else:
        print("invalid input, Put only the number of the choice")
        english()
def quiet():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou step up to the front of the room and stand there with a blank expression. Unsuprisingly the class looks at you with a confused expression in respose to your silence until the teacher breaks the silence and tells you to sit back down. After you finished your speech you listened to a couple other speeches then the class ended. What do you want to do next:")
    print("1. Go to 3rd hour.")
    print("2. Skip 3rd hour.")

    choice = input("> ")

    if choice == "1":
        science()
    elif choice == "2":
        skip_class()

    else:
        print("invalid input, Put only the number of the choice")
        quiet()

def science():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou are now in science class and have to do a small lab, Anwser the questions only numbers given.\n>")
    question_1 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "What is gravity:" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_2 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "what is the water cycle:" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_3 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "What is friction" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_4 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "What does the do atmophere" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_5 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false the sun is solid:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_6 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false there are 3 types of rocks:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_7 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false Issac newton discoverd genetics and evolution:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_8 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false earth is the only habitable planet:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_9 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false earth is the largest planet:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_10 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false trees generate carbon dioxide:" + "\x1B[0m" "\n1. true\n2. False\n>") 


    score = 0
    
    if  question_5.lower() == "2":
        score = score + 1
        

    if  question_4.lower() == "3":
        score = score + 1
   


    if  question_3.lower() == "1":
        score = score + 1

    

    if  question_2.lower() == "4":
        score = score + 1



    if  question_1.lower() == "2":#makes it lowercse can be used to fix spelling error for upper and lower case
        score = score + 1   



    if  question_6.lower() == "1":
        score = score + 1
        
    
    
    if  question_7.lower() == "2":
        score = score + 1



    if  question_8.lower() == "1":
        score = score + 1




    if  question_9.lower() == "2":
        score = score + 1




    if  question_10.lower() == "2":
        score = score + 1
    print("SCORE: " + str(score) + "/10")
    lunch()













def skip_class():#Caught skipping ending
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou attempt to skip class unitil you are caught by a teacher in the hall way. When he catches you, you get sent to the office and your mom is imfomed of this issue. In the past youve been known to skip class, so your mom picks you up from school and you get lectured about being a better kid. Congrats you got the \x1B[4m" + "'Caught Skipping'" + "\x1B[0m" " ending")
















def english1():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAfter some time the nurse tells you to go to second hour. you find yourself in second hour english class with the teacher beggining to talk.\n\n\n\x1B[4m" + "Ms, fiddle:" + "\x1B[0m" "\nAll right kids, settle down! Today we will be doing speeches (The kids faces around turn blue as their voices shut) yes, yes I know harsh for the firt day. But you know, if you dont challenge yourself you wont get better at things, so get ready to share something about this summer to your class.\n\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhat do you want to do next:")
    print("1. Talk about how you rotted in your bed all summer")
    print("2. start SCREAMING.")
    print("3. Say nothing when you go up")

    choice = input("> ")

    if choice == "1":
        bed_rot()
    elif choice == "2":
        scream_speech()
    elif choice == "3":
        quiet()
    else:
        print("invalid input, Put only the number of the choice")
        english1()


def bed_rot():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou step up to talk about how you bed rotted all summmer, suprisingly the class liked it and gave you praise for you speech including the teacher. After you finished your speech you listened to a couple other speeches then the class ended. What do you want to do next:")
    print("1. Go to 3rd hour.")
    print("2. Skip 3rd hour.")

    choice = input("> ")

    if choice == "1":
        science()
    elif choice == "2":
        skip_class()

    else:
        print("invalid input, Put only the number of the choice")
        bed_rot()

def scream_speech():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nWhen you walk up for your speech you Immediatly start screaming like theres no tommorow. Eventualy you are taken to the office for being a distruption and failed the speech. What do you want to do now:")
    print("1. take a nap.")
    print("2. Make up with your teacher and go back to class.")
    print("3. Complain to the office and try to get the teacher in trouble")

    choice = input("> ")

    if choice == "1":
        office_sleep()
    elif choice == "2":
        apologize()
    elif choice == "3":
        blame()
    else:
        print("invalid input, Put only the number of the choice")
        scream_speech()















def blame():#Bad kid ending
     print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou try arguring with the princible about unfairness but instead you are suspended and sent home. Your mom was called to pick you up, as she arrives shes visibly fumining with anger. When you enter her car she scolds you for being rude and you get grounded for a week. Congrats you got the \x1B[4m" + "'Bad Kid'" + "\x1B[0m" " ending")















def apologize():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou go back to you english class and apologize to the teacher, she forgives you and you move on with your day. You find yourslef in science class today you're are given questions to anwser, respond with the number of choice")
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou attempt to skip class unitil you are caught by a teacher in the hall way. He send you back to class and let off with a warning. You are now in science class and have to do a small lab, Anwser the questions only numbers given.\n>")
    question_1 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "What is gravity:" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_2 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "what is the water cycle:" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_3 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "What is friction" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_4 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "What does the do atmophere" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_5 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false the sun is solid:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_6 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false there are 3 types of rocks:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_7 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false Issac newton discoverd genetics and evolution:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_8 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false earth is the only habitable planet:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_9 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false earth is the largest planet:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_10 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false trees generate carbon dioxide:" + "\x1B[0m" "\n1. true\n2. False\n>") 


    score = 0
    
    if  question_5.lower() == "2":
        score = score + 1
        

    if  question_4.lower() == "3":
        score = score + 1
   


    if  question_3.lower() == "1":
        score = score + 1

    

    if  question_2.lower() == "4":
        score = score + 1



    if  question_1.lower() == "2":#makes it lowercse can be used to fix spelling error for upper and lower case
        score = score + 1   



    if  question_6.lower() == "1":
        score = score + 1
        
    
    
    if  question_7.lower() == "2":
        score = score + 1



    if  question_8.lower() == "1":
        score = score + 1




    if  question_9.lower() == "2":
        score = score + 1




    if  question_10.lower() == "2":
        score = score + 1
    print("SCORE: " + str(score) + "/10")
    lunch()

def office_sleep():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou begin to take a nap in detention then after the hour is done you are woken up and sent to your 3rd hour class, science. Your are given questions to anwser, respond with the number of choice")
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou attempt to skip class unitil you are caught by a teacher in the hall way. He send you back to class and let off with a warning. You are now in science class and have to do a small lab, Anwser the questions only numbers given.\n>")
    question_1 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "What is gravity:" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_2 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "what is the water cycle:" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_3 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "What is friction" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_4 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "What does the do atmophere" + "\x1B[0m" "\n1. When 2 things rub together and make heat.\n2.The force that attracts matter towards earth.\n3. Keeps out air on earth.\n4. The movement of water on earth.\n>")
    question_5 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false the sun is solid:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_6 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false there are 3 types of rocks:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_7 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false Issac newton discoverd genetics and evolution:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_8 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false earth is the only habitable planet:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_9 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false earth is the largest planet:" + "\x1B[0m" "\n1. true\n2. False\n>") 
    question_10 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "true or false trees generate carbon dioxide:" + "\x1B[0m" "\n1. true\n2. False\n>") 


    score = 0
    
    if  question_5.lower() == "2":
        score = score + 1
        

    if  question_4.lower() == "3":
        score = score + 1
   


    if  question_3.lower() == "1":
        score = score + 1

    

    if  question_2.lower() == "4":
        score = score + 1



    if  question_1.lower() == "2":#makes it lowercse can be used to fix spelling error for upper and lower case
        score = score + 1   



    if  question_6.lower() == "1":
        score = score + 1
        
    
    
    if  question_7.lower() == "2":
        score = score + 1



    if  question_8.lower() == "1":
        score = score + 1




    if  question_9.lower() == "2":
        score = score + 1




    if  question_10.lower() == "2":
        score = score + 1
    print("SCORE: " + str(score) + "/10")
    lunch()



def lunch():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAfter finishing your quiz you go to eat lunch, you end up sitting alone since you dont know anyone. After lunch ends you go to PE today you are running, what do you want to do next:")
    print("1. Listen to the teacher and begin running")
    print("2. Complain to the teacher.")

    choice = input("> ")

    if choice == "1":
        history()
    elif choice == "2":
        history()

    else:
        print("invalid input, Put only the number of the choice")
        lunch()


def history():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nYou see everyone else begin running so you follow despite wanting to do it or not. After you finish running you head to your next class. As you enter history class you are given a quiz to complete. Anwser with only the number of choice:")
    question_1 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "1. Who was the first President of the United States?:" + "\x1B[0m" "\n1. Thomas Jefferson.\n2. George Washington.\n3. Abraham Lincoln.\n4. John Adams.\n>")
    question_2 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "2. What year did the United States declare its independence from Britain?:" + "\x1B[0m" "\n1. 1776.\n2. 1812\n3. 1787.\n4. 1865.\n>")
    question_3 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "3. Which U.S. President freed the enslaved people by issuing the Emancipation Proclamation?" + "\x1B[0m" "\n1. George Washington.\n2. Franklin D. Roosevelt.\n3. Abraham Lincoln.\n4. Theodore Roosevelt.\n>")
    question_4 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "4. What event caused the United States to enter World War II?" + "\x1B[0m" "\n1. The sinking of the Titanic.\n2.The Great Depression.\n3. The bombing of Pearl Harbor.\n4. The invasion of Poland.\n>")
    question_5 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "5. true or false The Declaration of Independence was signed in 1776:" + "\x1B[0m" "\n1. true\n2. False\n>")
    question_6 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "6. true or false The U.S. bought Alaska from Russia:" + "\x1B[0m" "\n1. true\n2. False\n>")
    question_7 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "7. true or false The Great Depression ended because of World War II:" + "\x1B[0m" "\n1. true\n2. False\n>")
    question_8 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "8. true or false The U.S. Constitution guarantees freedom of speech and religion:" + "\x1B[0m" "\n1. true\n2. False\n>")
    question_9 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "9. true or false The Statue of Liberty was a gift from England:" + "\x1B[0m" "\n1. true\n2. False\n>")
    question_10 = input("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "10. true or false The American Civil War was fought between the North and South:" + "\x1B[0m" "\n1. true\n2. False\n>")


    score = 0
   
    if  question_5.lower() == "1":
        score = score + 1
       

    if  question_4.lower() == "3":
        score = score + 1
   


    if  question_3.lower() == "3":
        score = score + 1

   

    if  question_2.lower() == "1":
        score = score + 1



    if  question_1.lower() == "2":#makes it lowercse can be used to fix spelling error for upper and lower case
        score = score + 1  



    if  question_6.lower() == "1":
        score = score + 1
       
   
   
    if  question_7.lower() == "1":
        score = score + 1



    if  question_8.lower() == "1":
        score = score + 1




    if  question_9.lower() == "2":
        score = score + 1




    if  question_10.lower() == "1":
        score = score + 1
    print("SCORE: " + str(score) + "/10")
    ending()













def ending():#normal ending
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nFinaly after finishing the quiz, you can go home and rest again. You are overjoyed, maybe the first day of school wasnt so bad. Congrats you got the \x1B[4m" + "'Normal'" + "\x1B[0m" " ending.")
    






start_adventure()












