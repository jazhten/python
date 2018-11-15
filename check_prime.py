import math
number = int(input("Number to be checked: "))

def is_prime(num):
    check_lim = int(math.sqrt(num)+1)
    if num <= 1:
        return false
    elif num == 2:
        return true
    for i in range(2,check_lim):
        if(num % i == 0):
            return True
            break
        else:
            return False

if is_prime(number):
    print(str(number) + " is prime")
else:
    print(str(number) + " is not prime")
