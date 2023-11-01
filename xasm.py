from sys import argv,exit
from os import system

if len(argv) == 1:
    print("Invalid Usage. Correct Usage: 'xasm [program].xasm'")
    exit()

with open(argv[1],'r') as file:
    program = file.readlines()

result = []

def getNumber(line,startPos):
    idx = startPos
    num = ''
    try:
        while not line[idx] in [',']:
            num += line[idx]
            idx += 1
    except:
        # EOF
        pass
    if num[0] == 'R':
        reg = True
        num = num[1:]
    else:
        reg = False
    num = int(num) % 256
    return reg,num,idx+1

for idx in range(len(program)):
    program[idx] = program[idx].replace('\n','')
try:
    for line in program:
        if line[0:3] == "MOV":
            reg,r1,idx = getNumber(line,4)
            reg,r2_d1,idx = getNumber(line,idx)
            if not reg:
                d1 = r2_d1
                result.append(0x01)
                result.append(r1)
                result.append(d1)
            else:
                r2 = r2_d1
                result.append(0x02)
                result.append(r1)
                result.append(r2)
        elif line[0:3] == "ADD":
            reg,r1,idx = getNumber(line,4)
            reg,r2_d1,idx = getNumber(line,idx)
            if not reg:
                d1 = r2_d1
                result.append(0x03)
                result.append(r1)
                result.append(d1)
            else:
                r2 = r2_d1
                result.append(0x04)
                result.append(r1)
                result.append(r2)
        elif line[0:3] == "SUB":
            reg,r1,idx = getNumber(line,4)
            reg,r2_d1,idx = getNumber(line,idx)
            if not reg:
                d1 = r2_d1
                result.append(0x05)
                result.append(r1)
                result.append(d1)
            else:
                r2 = r2_d1
                result.append(0x06)
                result.append(r1)
                result.append(r2)
        elif line[0:3] == "MUL":
            reg,r1,idx = getNumber(line,4)
            reg,r2_d1,idx = getNumber(line,idx)
            if not reg:
                d1 = r2_d1
                result.append(0x07)
                result.append(r1)
                result.append(d1)
            else:
                r2 = r2_d1
                result.append(0x08)
                result.append(r1)
                result.append(r2)
        elif line[0:3] == "DIV":
            reg,r1,idx = getNumber(line,4)
            reg,r2_d1,idx = getNumber(line,idx)
            if not reg:
                d1 = r2_d1
                result.append(0x09)
                result.append(r1)
                result.append(d1)
            else:
                r2 = r2_d1
                result.append(0x0A)
                result.append(r1)
                result.append(r2)
        elif line[0:3] == "JMP":
            reg,a1,idx = getNumber(line,4)
            result.append(0x0B)
            result.append(a1*3)
            result.append(0x00)
        elif line[0:4] == "CALL":
            reg,a1,idx = getNumber(line,5)
            result.append(0x0C)
            result.append(a1*3)
            result.append(0x00)
        elif line[0:3] == "RET":
            result.append(0x0D)
            result.append(0x00)
            result.append(0x00)
        elif line[0:3] == "INC":
            reg,r1,idx = getNumber(line,4)
            result.append(0x0E)
            result.append(r1)
            result.append(0x00)
        elif line[0:3] == "DEC":
            reg,r1,idx = getNumber(line,4)
            result.append(0x0F)
            result.append(r1)
            result.append(0x00)
        elif line[0:3] == "AND":
            reg,r1,idx = getNumber(line,4)
            reg,r2,idx = getNumber(line,idx)
            result.append(0x10)
            result.append(r1)
            result.append(r2)
        elif line[0:2] == "OR":
            reg,r1,idx = getNumber(line,3)
            reg,r2,idx = getNumber(line,idx)
            result.append(0x11)
            result.append(r1)
            result.append(r2)
        elif line[0:3] == "XOR":
            reg,r1,idx = getNumber(line,3)
            reg,r2,idx = getNumber(line,idx)
            result.append(0x12)
            result.append(r1)
            result.append(r2)
        elif line[0:4] == "HALT":
            result.append(0x13)
            result.append(0x00)
            result.append(0x00)
        elif line[0:3] == "INT":
            reg,d1,idx = getNumber(line,4)
            reg,r1,idx = getNumber(line,idx)
            result.append(0x14)
            result.append(d1)
            result.append(r1)
        elif line[0:2] == "JE":
            reg,r1,idx = getNumber(line,3)
            reg,r2,idx = getNumber(line,idx)
            result.append(0x15)
            result.append(r1)
            result.append(r2)
        elif line[0:3] == "JNE":
            reg,r1,idx = getNumber(line,4)
            reg,r2,idx = getNumber(line,idx)
            result.append(0x16)
            result.append(r1)
            result.append(r2)
        elif line[0:3] == "JGT":
            reg,r1,idx = getNumber(line,4)
            reg,r2,idx = getNumber(line,idx)
            result.append(0x17)
            result.append(r1)
            result.append(r2)
        elif line[0:3] == "JLT":
            reg,r1,idx = getNumber(line,4)
            reg,r2,idx = getNumber(line,idx)
            result.append(0x18)
            result.append(r1)
            result.append(r2)
        elif line[0:4] == "JGTE":
            reg,r1,idx = getNumber(line,5)
            reg,r2,idx = getNumber(line,idx)
            result.append(0x19)
            result.append(r1)
            result.append(r2)
        elif line[0:4] == "JLTE":
            reg,r1,idx = getNumber(line,5)
            reg,r2,idx = getNumber(line,idx)
            result.append(0x1A)
            result.append(r1)
            result.append(r2)
except:
    print("An error occured while compiling at XASM level.")
    exit()

resultname = argv[1].replace('.xasm','')+".xe"
with open(resultname,'wb') as file:
    file.write(bytes(result))