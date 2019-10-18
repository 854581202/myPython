# -*- coding:utf-8 -*-

def product(*intVar):
    if intVar is None:
        varSum = None
    else:
        varSum = 1

    for var in intVar:
        varSum = varSum * var
    return varSum

#print(product(1,2,3,4,5))