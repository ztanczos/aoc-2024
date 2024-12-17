import re

instr_map = {
    0: lambda operand: adv(operand),
    1: lambda operand: bxl(operand),
    2: lambda operand: bst(operand),
    3: lambda operand: jnz(operand),
    4: lambda operand: bxc(operand),
    5: lambda operand: out(operand),
    6: lambda operand: bdv(operand),
    7: lambda operand: cdv(operand)
}

def combo(operand):
    global reg_a, reg_b, reg_c

    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c

def adv(operand):
    global reg_a
    reg_a = reg_a // (2 ** combo(operand))

def bxl(operand):
    global reg_b
    reg_b = reg_b ^ operand

def bst(operand):
    global reg_b
    reg_b = combo(operand) % 8

def bxc(operand):
    global reg_b, reg_c
    reg_b = reg_b ^ reg_c

def out(operand):
    print(f'{combo(operand) % 8},', end='')

def bdv(operand):
    global reg_a, reg_b
    reg_b = reg_a // (2 ** combo(operand))

def cdv(operand):
    global reg_a, reg_c
    reg_c = reg_a // (2 ** combo(operand))

def jnz(operand):
    global ip, reg_a
    if reg_a != 0:
        ip = operand
        ip -= 2

def main():
    global reg_a, reg_b, reg_c, ip
    with open("17_input.txt", "r") as f:
        reg_a = int(re.search(r"(\d+)", f.readline())[0])
        reg_b = int(re.search(r"(\d+)", f.readline())[0])
        reg_c = int(re.search(r"(\d+)", f.readline())[0])

        f.readline()
        program = [int(opcode) for opcode in re.findall(r"(\d+)", f.readline())]

    print(f'{reg_a=}, {reg_b=}, {reg_c=}, {program=}')
    while 0 <= ip < len(program):
        instr_map[program[ip]](program[ip+1])
        ip += 2

reg_a: int = 0
reg_b: int = 0
reg_c: int = 0
ip: int = 0
if __name__ == '__main__':
    main()