# -*- coding:utf-8 -*-
import os
from _datetime import datetime

def do_dir():
    pwd = os.path.abspath(".")

    for f in os.listdir(pwd):
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime("%Y.%m.%d %H:%M")
        flag = "/" if os.path.isdir(f) else " "
        print("%30s %10s %20s %10s"%(f,fsize,mtime,flag))

do_dir()