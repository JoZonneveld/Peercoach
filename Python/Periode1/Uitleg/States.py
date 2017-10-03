#OR V1 =TRUE  V2 = TRUE  == TRUE
#OR V1 =FALSE  V2 = TRUE  == TRUE
#OR V1 =TRUE  V2 = FALSE  == TRUE
#OR V1 =FALSE  V2 = FALSE  == FALSE

#AND V1 =TRUE  V2 = TRUE  == TRUE
#AND V1 =FALSE  V2 = TRUE  == FALSE
#AND V1 =TRUE  V2 = FALSE  == FALSE
#AND V1 =FALSE  V2 = FALSE  == FALSE

# x = 3
# y = 7
#
# while x >= 0 or y >= 0:
#   x = x - 1
#   y = y - 3
#
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
