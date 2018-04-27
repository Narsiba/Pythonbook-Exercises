
for A in range(1, 10):
  for B in range(10):
    if A==B:
      continue
    for C in range(10):
        if A==C or B==C:
          continue
        for D in range(1,10):
            if A==D or B==D or C==D:
                continue
            else:
              ABCD=int(str(A)+str(B)+str(C)+str(D))
              DCBA=int(str(D)+str(C)+str(B)+str(A))
              if ABCD*4==DCBA:
                print(ABCD, DCBA)
              
                
