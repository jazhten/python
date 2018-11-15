import random

top = int(input('Enter highest number limit thing : '))

answer = random.randint(0,top)
print(answer)

flag = True
while flag == True:
    guess = int(input('Enter guess '))
    if(guess == answer):
        print("Yay!")
        flag = False
    if(guess > answer):
        print("Too high!")
    if(guess < answer):
        print("Too low!")

