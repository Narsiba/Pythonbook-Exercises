#Excercises

"""
set1={"A", "B", "C"}
set2={"D", "B", "C"}

set3=set1-set2
set4=set2-set1
set5=set3|set4
print(set5)
"""
"""
wordset1=set("whatever")
wordset2=set("neverever")

wordsetnew=wordset1&wordset2
print(wordsetnew)
"""
"""
set1=set()
set2=set()
set3=set()

for i in range(0, 1000, 3):
    set1.add(i)

for i in range(0, 1000, 7):
    set2.add(i)

for i in range(0, 1000, 11):
    set3.add(i)

seta=set1&set2&set3
print(seta)

setb=(set1&set2)-set3
print(setb)

setc=set(range(1, 1000))-set1-set2-set3
print(setc)
"""
#Exercise 15.1
"""
from os import getcwd, listdir
wd=getcwd()
filesdir=listdir(wd)

for i in filesdir:
    print(wd+"/"+i)

"""
