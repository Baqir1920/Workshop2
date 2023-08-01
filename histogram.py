import os
import sys
import string

lines = sys.stdin.readlines()
key_value_Dict = {}
total_count = 0
while lines != "":
    key_value = lines.split()
    key = lines[0]
    value - int(key_value[1])

    key_value_list[key] = value

    total_count += key_value

    lines = sys.stdin.readlines()

for key, value in key_value_dict.items():
    print(key.ljust(15),"\t [",sep="",end="")
    per = (value/total_count)*100
    for i in range(0,pre,5):
        print("*",sep="",end="")
    print("]",per,"*",sep="")