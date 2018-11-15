import random

top = int(input('Enter highest number limit thing : '))

answer = random.randint(0,top)
#print(answer)
count = 0
flag = True
while flag == True:
    count +=1
    guess = int(input('Enter guess '))
    if(guess == answer):
        print("Yay! You took " + str(count) +" guesses")
        if input('Type exit to quit game:') == 'exit':
            flag = False
        else:
            count = 0
            answer = random.randint(0,top)
    if(guess > answer):
        print("Too high!")
    if(guess < answer):
        print("Too low!")

