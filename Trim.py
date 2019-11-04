# -*- coding:utf-8 -*-

def trim(s):

    if (s[1] != ' ') & (s[-1] != ' '):
        return s[:]
    elif (s[1] == ' ') & (s[-1] == ' '):
        return trim(s[2:-1])
    elif s[1] == ' ':
        return trim(s[2:])
    elif s[-1] == ' ':
        return trim(s[:-1])



print(trim(' 1 1 223   '))