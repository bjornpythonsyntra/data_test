
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

import random as rnd
getallen = [rnd.randint(1, 100) for _ in range(15)]
newlist = sorted([x for x in getallen if x%2==0])

print(getallen)
print(newlist)


