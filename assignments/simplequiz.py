
def present():
    print("\n\n\n\n---------------------------------------------------------------------------------------------------------------\n\x1B[4m" + "Inner voice:" + "\x1B[0m" "\nAs the teacher marks your name off, home room eventualy ends and you find yourself in math class. You are tasked with solving review problems for math class input only numbers.\n\n ")
    question_1 = input("2+2 = \n>")
    question_2 = input("3+9 = \n>")
    question_3 = input("4+1 = \n>")
    question_4 = input("5-2 = \n>")
    question_5 = input("4+8 = \n>") 

    
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
        present()   
    print("SCORE: " + str(score) + "/5")
    present()
















