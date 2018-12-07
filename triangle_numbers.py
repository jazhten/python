num = int(input("How many triangle numbers to generate?: "))

list =[]

for i in range(1,num+1):
    list.append((i*(i+1)/2))

list=[int(i) for i in list]

print(list)
