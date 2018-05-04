
#Excercises
def find_vowels():
    word=input("Enter a word: ")
    i=0

    while i <len(word):
        if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
          print("There is a vowel at index", i)
        i+=1

def shared_chars(word1, word2):
    for i in range(len(word1)):
        if i+1>len(word2):
            break
        else:
            if word1[i]==word2[i]:
                print(word1[i], i)

def rmv_non_letters(string):
    new_string=""
    for char in string:
        if char >="A" and char <="z":
            new_string+=char
        else:
            new_string+=" "
    return new_string

#Exercise 10.1
def count_vowels(string):
    a=0
    e=0
    i=0
    o=0
    u=0
    for letter in string:
        if letter.lower()=="a":
            a+=1
        elif letter.lower()=="e":
            e+=1
        elif letter.lower()=="i":
            i+=1
        elif letter.lower()=="o":
            o+=1
        elif letter.lower()=="u":
            u+=1
    print("There are {} a, {} e, {} i, {} o, {} u in your text".format(a, e, i, o, u))

#Exercise 10.2
def text_in_brackets(text):
    start=0
    while start < len(text):
        first=text.find("[", start)
        print("open", first)
        second=text.find("]", start+1)
        if first==-1 or second==-1:
            break
        print("close", second)
        print(text[(first+1):(second)])
        start=second

#Exercise 10.3
"""i=ord("A")
j=ord("A")+13
while i <= ord("Z"):
    print(chr(i), end="")
    i+=1
print()
for j in range(ord("A"), ord("Z")+1):
    if j+13 > ord("Z"):
        print(chr(j-13), end="")
    else:
        print(chr(j+13), end="")"""

#Exercise 10.4
#Find all occurences of a specific word
def find_word(text, word):
    counter=0
    text=rmv_non_letters(text).lower().split()
    for i in text:
        if i==word.lower():
            counter+=1
    return counter

#Exercise 10.5
#Takes a string and orders the characters according to their ASCII code.
def order_string(string):
    new_string=""
    index=0
    for letter1 in string:
        index+=1
        for letter2 in string:
            if letter2<letter1:
                print(letter1, letter2)
                break
        else:
            new_string+=letter1
            print("Else", new_string)

    return new_string

print(order_string("Hello world!"))

#Exercise 10.6
#Autocorrect Functions
def autocorrect(text):
    text= text.split()
    for word in text:
        if word[0] >= "A" and word[0] <="Z":
            if word[1]>="A" and word[1]<="Z":
                if word[3] >="a" and word[3]<="z":
                    word=word[0]+word[1].lower()+word[2:]
        
