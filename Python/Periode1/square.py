i = int(input("voer in: "))

for x in range(i):
    output =""
    for y in range(i):
        if(x == 0 or x == (i-1) or y == 0 or y == (i-1)):
            output += "*"
        else:
            output += " "
    print (output)
