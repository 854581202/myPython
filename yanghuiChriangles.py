# -*- coding:utf-8 -*-

def traingle():
   N = [1]
   while True:
       yield N
       N.append(0)
       N=[ N[k]+N[k-1] for k in range(len(N))]

def print_traingle(count):
    i = 1N = [1]
for i in range(10):  #打印10行
    print(N)
    N.append(0)
    N = [N[k] + N[k-1] for k in range(i+2)]
    for n in traingle():
        print(n)
        i = i + 1
        if i>=count:
            break

print_traingle(10)
