#Exercises
#t1= ("apple", "banana", "cherry", "mango", "fruits", 23, 8)
#for t in range(len(t1)):
#    print(t1[t], t)


#Takes 2 compex numbers and adds them
def add_cnumbers(cnum1, cnum2):
    return (cnum1[0]+cnum2[0])+(cnum1[1]+cnum2[1])

def mult_cnumber(cnum1, cnum2):
    return (cnum1[0]*cnum2[0]-cnum1[1]*cnum2[1])+(cnum1[0]*cnum2[1]-cnum1[1]*cnum2[0])

def intsininttuple(inttuple):
    for i in inttuple:
        if isinstance(i, tuple):
            intsininttuple(i)
        else:
            print(i)
            
        

inttuple=( 1, 2, ( 3, 4 ), 5, ( ( 6, 7, 8, ( 9, 10 ), 11 ), 12, 13 ), ( ( 14, 15, 16 ), ( 17, 18, 19, 20 ) ) )
intsininttuple(inttuple)
