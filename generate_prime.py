import math

def is_prime(num):
    if(num <= 1):
        return False
    if(num==2):
         return True
    lim = int(math.sqrt(num)) +1
    for i in range(2,lim):
        if(num % i == 0):
            return False
            break
    return True


list = []
limit = int(input("Until which prime to generate:"))

#limit2 = int(input("How many primes to generate "))

for i in range(1,limit):
    if(is_prime(i)):
        list.append(i)

#i = 0
#j =0
#while i < limit2:
#    if is_prime(j):
#        list.append(j)
#        i = i +1
#    j = j+1

print(list)

