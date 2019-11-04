# -*- coding:utf-8 -*-

def odd_iter():
    n=1
    while True:
        n = n + 2
        yield n

def not_divisible(n):
    return lambda x:x%n > 0

def primes():
    yield 2
    it = odd_iter()  #init
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n),it)

#for n in primes():
#    if n < 1000:
#        print(n)
#    else:
#        break


#----------------------------------------------------------------------------------------
#----------回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：--
#----------------------------------------------------------------------------------------
def qf(s):
    n=len(s)
    flag = 1
    if n%2 != 0:
        flag = 0
        for i in range(int(n/2)):
            j = -1 - i
            if((int(s[i]) - int(s[j]))==0):
                flag = flag + 0
            else:
                flag = flag + 1
    if flag == 0:
        return s
    else:
        pass


listVar = ["12321","123456","45654"]
listNew=[]
output = filter(qf,listVar)
print(list(output))

