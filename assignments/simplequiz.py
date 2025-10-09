question_1 = input("what is 2+2\n>")
question_2 = input("what is 3+9\n>")
question_3 = input("what is 4+1\n>")
question_4 = input("what is 5-2\n>")
question_5 = input("what is 4+8\n>")



def tally_score():
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
    
    print("SCORE: " + str(score) + "/5")
   
tally_score()

















