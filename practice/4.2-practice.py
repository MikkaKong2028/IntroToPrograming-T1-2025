import random

games = ["Elden Ring", "Shadow of the Collossus", "Diablo III", "Minecraft", "Super mario World"]

for game in games: #for each individual game in the games variable print all the games in a loop. game = each of these but goes around in a loop 
    print(game)




#print every number from 1 - 5 using a for loop

for i in range(0,5):
    print("Rank " + str(i) + ": " + games[i])


#print every odd number from 1 - 100

for i in range(1,100,2):
    print(i)


#create a list of 100 random numbers that range from -100 to 100
# print only positive numbers 
random_numbers = []

for i in (0,100,):
    random_numbers.append(random.randint(-100,101))

for i in range(0, len(random_numbers)):
    if random_numbers[i] < 0 :
        random_numbers.pop(i)

print(random_numbers)











