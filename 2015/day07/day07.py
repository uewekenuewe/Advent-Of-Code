import re
import sys
import numpy as np
import copy 

ans1 = 0
ans2 = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("07", "r")

lines = [l.strip() for l in f.readlines()]
registers = {}
def parse_line(l:str):
    command,target = l.split("->")
    command = command.split()
    for i in range(len(command)):
        try:
            command[i] = int(command[i])
        except:
            continue

    target = target.strip()
    return command,target

def part1(l:str):
    command, target = parse_line(l)
    registers[target] = command


for l in lines:
    part1(l)

cache = {}

def resolve_command(cmd):
    if type(cmd) == int:
        return cmd
    if type(cmd) == str:
        if cmd in cache.keys():
            return cache[cmd]
        result = resolve_command(registers[cmd])
        cache[cmd] = result
        return result
    if len(cmd) == 1:
        return resolve_command(cmd[0])
    #NOT
    if len(cmd) == 2:
        return ~resolve_command(registers[cmd[1]])
    if cmd[1] == "OR":
        return resolve_command(cmd[0]) | resolve_command(cmd[2])
    if cmd[1] == "AND":
        return resolve_command(cmd[0]) & resolve_command(cmd[2])
    if cmd[1] == "LSHIFT":
        return resolve_command(cmd[0]) << resolve_command(cmd[2])
    if cmd[1] == "RSHIFT":
        return resolve_command(cmd[0]) >> resolve_command(cmd[2])

ans1 = resolve_command(registers['a'])
registers['b'] = ans1 
cache = {}
ans2 = resolve_command(registers['a'])
print("------")
print("ans1:", ans1)
print("ans2:", ans2)
