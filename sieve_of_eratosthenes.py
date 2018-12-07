def SieveOfEratosthenese(n):
    ##Create boolean array from 0 to n and initialise all to be true. A value will becomes false if it is not a prime
    #else it will reamin true

    prime = [True for i in range(n+1)]
    p = 2
    while(p*p <=n):
        #Change for non prime values
        if(prime[p] == True):
            #update all multiples of p
            for i in range(p * 2, n+1,p):
                prime[i] = False
        p+=1
    for p in range(2,n):
        if prime[p]:
            print(p)


limit = int(input("Limit of prime to sieve: "))
print("Prime numbers smaller than input are :")
SieveOfEratosthenese(limit)

