from random import randint
from random import choice

#minimum = input("Minimum value:")
#maximum = input("Maximum value:")

def random_number():
    n_list = [*range(1,100)]

    #random.randint(1, 100)
    print(choice(n_list))
    #print(n_list)

random_number()
    