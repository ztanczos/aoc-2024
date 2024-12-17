
def combo(operand, reg_a, reg_b, reg_c):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c

def adv(operand, reg_a, reg_b, reg_c):
    return reg_a // (2 ** combo(operand, reg_a, reg_b, reg_c))

def bxl(operand, reg_b):
    return reg_b ^ operand

def bst(operand, reg_a, reg_b, reg_c):
    return combo(operand, reg_a, reg_b, reg_c) % 8

def bxc(reg_b, reg_c):
    return reg_b ^ reg_c

def out(operand, reg_a, reg_b, reg_c):
    return combo(operand, reg_a, reg_b, reg_c) % 8

def bdv(operand, reg_a, reg_b, reg_c):
    return reg_a // (2 ** combo(operand, reg_a, reg_b, reg_c))

def cdv(operand, reg_a, reg_b, reg_c):
    return reg_a // (2 ** combo(operand, reg_a, reg_b, reg_c))

def jnz(operand, reg_a):
    if reg_a != 0:
        ip = operand
        ip -= 2


def main():
    init_reg_a = 0o37671603002
    program = [2,4,1,4,7,5,4,1,1,4,5,5,0,3,3,0]
    while True:
        reg_a = init_reg_a
        reg_b = 0
        reg_c = 0
        output = []
        while True:
            # 2, 4
            reg_b = bst(4, reg_a, reg_b, reg_c)

            # 1, 4
            reg_b = bxl(4, reg_b)

            # 7, 5
            reg_c = cdv(5, reg_a, reg_b, reg_c)

            # 4, 1
            reg_b = bxc(reg_b, reg_c)

            # 1, 4
            reg_b = bxl(4, reg_b)

            # 5, 5
            val = out(5, reg_a, reg_b, reg_c)
            if val == program[len(output)]:
                output.append(val)
            else:
                break
            #if len(output) > 12:
            #    print("=== {0} - {0:b} - {1} ===".format(init_reg_a, oct(init_reg_a)))
            if len(output) > 15:
                break

            # 0, 3
            reg_a = adv(3, reg_a, reg_b, reg_c)

            # 3, 0
            if reg_a == 0:
                break

        if len(output) == 16:
            print(f'##### Result: {init_reg_a} #####')
            break

        init_reg_a += 0o100000000000


if __name__ == '__main__':
    main()