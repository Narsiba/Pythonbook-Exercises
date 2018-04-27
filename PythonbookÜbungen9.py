#Exercise 9.1
#Takes a number n and returns the nth number of the Fibonacci Sequence
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

#Exercise 9.2
def fibd(n, depth):
    print(depth*"   ", n)
    if n<=2:
        x=1
        print(depth*"   ","return", x)
        return 1
    y=fibd(n-1, depth+1)+fibd(n-2, depth+1)
    print(depth*"   ","return", y)
    return y

#Exercise 9.4
#Takes two integers and calculates the greatest common divider
def divider(n1, n2):
    if n2%n1==0:
        return n1
    else:
        return divider(n2%n1, n1)
