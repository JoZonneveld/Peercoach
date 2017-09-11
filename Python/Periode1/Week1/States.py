from random import randint

#gives a random number
test = (randint(1, 3))

# V = Variable : S = State
# Define V x : S = 10
x = 10

print(x)

if test == 1:
    x += 5
elif test == 2:
    x+=10
elif test == 3:
    x+=1


print(x)
