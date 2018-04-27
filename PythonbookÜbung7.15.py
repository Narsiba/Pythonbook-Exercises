from random import randint
Crawlers=1000
days=0


for c in range(Crawlers):
    pos=randint(1,4)
    while True:
        days+=1
        if pos==4:
            break
        else:
            pos=randint(3,4)
print(days/Crawlers)
