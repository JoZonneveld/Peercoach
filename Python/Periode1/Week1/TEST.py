def drawShape(size):
  s = ""
  for i in range (0,size):
    for j in range(0,size):
      if j < i or j > size - i - 1:
        s = s + " "
      else:
        s = s + "#"
    s += "\n"
  print(s)

drawShape(9)
