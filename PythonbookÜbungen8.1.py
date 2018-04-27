#Exercise 8.1 Multiplication Table
#Takes a number and displays all the multiplications from 1-10.
def multiplication_table(num):
    for i in range(10):
        print("{} * {}={}".format(i, num, (i+1)*num))

#Exercise 8.2 Common characters
#Takes two strings and returns the characters they have in common.
def common_chars(word1, word2):
    characters=""
    for letter in word1:
        if letter in word2 and letter not in characters:
            characters+=letter
    return characters

#Exercise 8.3 Gregory-Leibnitz Approximation
#Takes a number for the amount of terms to be used to approximate pi and returns the approximation of pi.
def leibnitz_pi(terms):
    x=1
    piapp=0
    for num in range(terms):
        if num%2==0:
            piapp+=(1/x)
        else:
            piapp-=(1/x)
        x+=2
    return 4*piapp

#Exercise 8.6 Binomial Coefficient
#Takes two numbers as parameters and returns the value of the binomial coefficient
def main():
    def get_factorial(n):
        for i in range(1, n):
            n*=i
        return n
    def get_Binomial_Coefficient(n, k):
        if n<k:
            print("n must be bigger or equal k")
            return
        return get_factorial(n)/(get_factorial(k)*get_factorial(n-k))

    get_Binomial_Coefficient(2, 5)

if __name__=='__main__':
    main()
