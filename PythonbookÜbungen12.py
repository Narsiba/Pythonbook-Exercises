#Exercises

from random import randint

"""data=input("Enter some data: ")
data=data.split()
data.sort()
for i in data:
    print(i)"""

"""numbers=[5, 10, -4, 9,55, 0]
numbers.sort(key=abs)
print(numbers)"""

def count_letters(string):
    abc=26*[0]
    for i in string.lower():
        if i <"a" or i>"z":
            continue
        else:
            abc[ord(i)-ord("a")]+=1
            print(abc)

#Exercise 12.1
def mgc_8_ball(answers):
    question=input("Ask your question, human: ")
    i=randint(0, len(answers)-1)
    print("The answers to the question '{}' is '{}'".format(question, answers[i]))

#Exercise 12.2
def card_deck():
    suits=["Hearts", "Clubs", "Spades", "Diamonds"]
    value=[2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    set=[]
    for s in suits:
        for v in value:
            set.append((s, v))
    return set

def shuffle_deck(deck):
    for c in deck:
        card=deck.pop(deck.index(c))
        deck.insert((randint(0, len(deck)-1)), card)
    print(deck)

#Exercise 12.3 FIFO
def main():
    queue=[]
    while True:
        user_input = input("Enter your object. Press 'Enter' to quit or '?' to display the first element. ")
        if user_input=="":
            print("You're leaving the programm")
            return
        elif user_input=="?":
            if len(queue)>0:
                print(queue.pop(0))
            else:
                print("Your list is empty")
        else:
            queue.append(user_input)

#Exercise 12.4
#Counts letters in a string and orders them according to their occurences.
def number_letters(x):
    return x[1]

def count_letters(text):
    letters=[]
    for i in range(26):
        letters.append([chr(i+65), 0])
    for letter in text.lower():
        if letter >= "a" and letter <= "z":
            letters[ord(letter)-ord("a")][1]+=1
    letters.sort(key=number_letters)
    return letters

#Exercise 12.5

def sieve(highest_number):
    numbers=[]
    for i in range(1, highest_number+1):
        numbers.append(i)
    numbers[0]=0
    for i in numbers:
        if i !=0:
            for j in range(len(numbers)):
                if numbers[j]==i:
                    continue
                elif numbers[j]%i == 0:
                    numbers[j]=0
    return numbers

text="as it turned out our chance meeting with REverendaRT HUR BElling was was to change our whole way of life, and every sunday we'd hurry along to St lOONY up the Cream BUn  and Jam..."
print(count_letters(text))
