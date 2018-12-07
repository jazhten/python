import random
import string
length = int(input("Length of password: "))

random = "".join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(length)])

print(random)
