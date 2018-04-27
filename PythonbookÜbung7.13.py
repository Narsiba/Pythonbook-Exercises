from random import randint

N=10000
dice=5
success=0

for rolls in range(N):
  result=0
  for die in range(dice):
    nresult=randint(1,6)
    if nresult < result:
      break
    elif die==4:
        success+=1
    else:
      result=nresult
      continue
print("The probability is ", success/N)
