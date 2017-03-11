#!/usr/bin/env python3
import operator

operateDict = {
    '+': operator.add,
    '-': operator.sub,
}


def calculate(arg):
    stack = list()

    for operand in arg.split():
        try:
            operand = float(operand)
            stack.append(operand)

        except ValueError:
            value2 = stack.pop()
            value1 = stack.pop()
            result = operateDict[operand](value1,value2)
            stack.append(result)

    return stack.pop()


def main():
    while True:
        res = calculate(input("rpn calc> "))
        print ("result:", res)


if __name__ == '__main__':  # Note: that's "underscore underscore n a m e ..."
    main()