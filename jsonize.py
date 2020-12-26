#!/usr/bin/env python3
import sys
import json
from cmd import Cmd 
def str_to_arr(line):
    arr = []
    for _ in range(len(line)):
        arr += line[_]
    return json.dumps(arr)
if __name__ == "__main__":
    # execute only if run as a script
    try:
        print(str_to_arr(sys.argv[1]))
    except:
        print(__file__ + ": missing operand")
    #prompt
    #Cmd.cmdloop()
