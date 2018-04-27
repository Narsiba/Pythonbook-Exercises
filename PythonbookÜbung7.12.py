from math import sqrt

for num in range(1, 101):
  for x in range(1, 10):
    num2=num-(x**2)
    for y in range(1, 10):
      if y<x:
          continue
      if (num2-(y**2))==0:
        print("{} = {}**2 + {}**2".format(num, x, y))
    else:
        continue
