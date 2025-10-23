
def hurricane_classify():
    r1 =74
    r2 = 96
    r3 = 96
    r4 = 111
    r6 = 130
    r7 = 130
    r8 = 157
    r9 = 158
    r10 = 500
    mph = input("how many miles per hour was the wind speed, put in only whole numbers.\n>")


    if mph == list(range(r1,r2)):
        print("tropical storm")
    
    elif mph == list(range(r3,r4)):
        print("catergory 1")

    elif mph == list(range(r4,r6)):
        print("category 2")

    elif mph == list(range(r7,r8)):
        print("category 3")

    elif mph == 157:
        print("category 4")

    elif mph == list(range(r9,r10)):
        print("category 5")
    
    
    else:
        print("too small to be huricane")

hurricane_classify()























