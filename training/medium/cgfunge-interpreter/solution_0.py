def run_cgfunge(program):
    program = [line.rstrip('\n') for line in program.split('\n')]
    max_col = max(len(line) for line in program)
    program = [line.ljust(max_col, ' ') for line in program]

    stack = []
    current_pos = 0
    direction = 1
    string_mode = False
    while True:
        c = program[int(current_pos.imag)][int(current_pos.real)]

        if string_mode:
            if c == '"':
                string_mode = False
            else:
                stack.append(ord(c))
        else:
            if c == '>':
                direction = 1
            elif c == '<':
                direction = -1
            elif c == '^':
                direction = -1j
            elif c == 'v':
                direction = 1j
            elif c == 'S':
                current_pos += direction
            elif c == 'E':
                break
            elif c.isdigit():
                stack.append(int(c))
            elif c == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif c == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif c == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif c == 'P':
                stack.pop()
            elif c == 'X':
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)
            elif c == 'D':
                a = stack.pop()
                stack.append(a)
                stack.append(a)
            elif c == '_':
                a = stack.pop()
                if a == 0:
                    direction = 1
                else:
                    direction = -1
            elif c == '|':
                a = stack.pop()
                if a == 0:
                    direction = 1j
                else:
                    direction = -1j
            elif c == 'I':
                a = stack.pop()
                print(a, end="")
            elif c == 'C':
                a = stack.pop()
                print(chr(a), end="")
            elif c == '"':
                string_mode = True
            
        current_pos += direction

n = int(input())
program = "\n".join([input() for _ in range(n)])
run_cgfunge(program)