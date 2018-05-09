
#Exercises 16
"""
from os import chdir

chdir("..")
fp=open("pc_rose.txt")
while True:
    buffer=fp.readline()
    if "name" in buffer:
        print(buffer)
    if buffer=="":
        break
fp.close()
"""
"""
from os import chdir

chdir("..")
fp=open("pc_rose.txt")
buffer=fp.read()
fp.close()

fp=open("pc_writetest.tmp", "w")
fp.write(buffer)
fp.close()

fp=open("pc_writetest.tmp")
buffer2=fp.read()
fp.close()
print(buffer2)
"""
"""
from os import chdir

chdir("..")
fp=open("pc_rose.txt")
buffer=fp.readlines()
fp.close()
new_buffer=""
for i in buffer:
    new_buffer+=i[::-1]

fp=open("pc_writetest.tmp", "w")
fp.write(new_buffer)
fp.close()

fp=open("pc_writetest.tmp")
buffer2=fp.read()
fp.close()
print(buffer2)
"""
"""
from os.path import getsize
from os import listdir

filesize=0
files=listdir()
for i in files:
    filesize+=getsize(i)

print(filesize)
"""

#Exercise 16.1
from os import chdir

def clean_str(text):
    new_str=""
    new_text=text.lower()
    for i in new_text:
        if i >="a" and i<="z":
            new_str+=i
        else:
            new_str+=" "
    return new_str

buffer_dict={}

chdir("..")
fp=open("pc_woodchuck.txt")

count=0
buffer_list=[]
while count<5:
    buffer=fp.readline()
    buffer=clean_str(buffer)
    buffer_list+=buffer.split()
    count+=1

for i in buffer_list:
    buffer_dict[i]=buffer.count(i)
print(buffer_dict)
