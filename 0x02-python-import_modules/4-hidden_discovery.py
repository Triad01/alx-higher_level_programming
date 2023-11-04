#!/usr/bin/python3
import hidden_4

name_list = dir(hidden_4)

for name in name_list:
    if not name.startwith("__"):
        print(name)
