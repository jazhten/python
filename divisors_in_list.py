list = []

num = int(input("Enter number of characters: "))

i = 0
while i < num:
    list.append(input("enter the" + str(i+1) + " th number:"))
    i +=1

list = [int(i) for i in list] #converts string to integers

divisor = int(input("Enter divisor "))

n_list = [i for i in list if i % divisor == 0]

print("Numbers that are divisible by " + str(divisor) + " are " + str(n_list))

