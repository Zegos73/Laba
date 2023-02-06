import random
from num2words import num2words
k = int(input("(2-9)"))
if not (2<= k <=9):
    quit()
a=0
min=101
while a < 100:
    i = random.randint(1,99)
    if i % 2 !=0:
        if min >(i):
            min =(i)
        print(i,'i')
        x=''
        while i > 0:
            x = str(i %k) +x
            i //= k
        print(x,'x')
        a=a+1
        print (a,'-----------------------------------')
def num_to_word(num):
    try:
        print(num2words(num, lang='ru'))
    except NotImplementedError:
        print(num2words(num, lang='en'))
num_to_word(min)
