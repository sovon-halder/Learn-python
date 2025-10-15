# import random
# computer = random.choice([-1,0,1])
# you = input("enter your choice: ")
# youDict = {"s":1, "w":-1, "g":0}
# you = youDict[you]
#
# if(computer == you):
#     print("its a draw")
# else:
#     if(computer == -1 and you == 1):
#         print("you win")
#     elif(computer == -1 and you == 0):
#         print("you lose")
#     if(computer == 1 and you == -1):
#         print("you lose")
#     elif(computer == 1 and you == 0):
#         print("you win")
#     if(computer == 0 and you == -1):
#         print("you lose")
#     elif(computer == 0 and you == 1):
#         print("you win")
#     else:
#         print("something went wrong!")
#



import random

computer = random.choice([-1, 0, 1])
you = input("enter your choice (s for snake, w for water, g for gun): ")

youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[you]

if computer == you:
    print("It's a draw")
elif (computer == -1 and you == 1):
    print("You win")
elif (computer == -1 and you == 0):
    print("You lose")
elif (computer == 1 and you == -1):
    print("You lose")
elif (computer == 1 and you == 0):
    print("You win")
elif (computer == 0 and you == -1):
    print("You lose")
elif (computer == 0 and you == 1):
    print("You win")
else:
    print("Something went wrong!")
