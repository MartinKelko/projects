import random

a = random.uniform(1,10)
print(a)

a = random.randint(1,10)
print(a)

a = random.normalvariate(0,1)
print(a)

mylist = list("AVGDESGFDF")
a = random.choice(mylist)
print(mylist)

mylist = list("AVGDESGFDF")
b = random.sample(mylist, 3)
print(mylist)




