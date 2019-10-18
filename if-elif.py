# -*- coding: utf-8 -*-
try:
    w=input("Please input weight:")
    weight = float(w)

    if weight < 18.5:
        print("过轻")
    elif weight < 25:
        print("正常")
    elif weight < 28:
        print("过重")
    elif weight < 32:
        print("肥胖")
    else:
        print("严重肥胖")

except ValueError:
    print("wrong value")