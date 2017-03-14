#!/usr/bin/env python3
import operator
import readline
import sys

operateDict = {
    '+': operator.add,
    '-': operator.sub,
    '^': operator.pow,
    '*': operator.mul,
}


def calculate(arg):
    stack = list()
    # counter handles more than two inputs
    counter = 0;

    for operand in arg.split():
        try:
            if (counter == 3):
                print ("Sorry, you can only input two values")
                return 0
            
            operand = float(operand)
            stack.append(operand)
            counter += 1

        except ValueError:
            value2 = stack.pop()
            value1 = stack.pop()

            #print colored output
            # print (colored(value1, 'red') , colored(operand, 'blue') , colored(value2, 'red'), colored('=', 'cyan'), )
            result = operateDict[operand](value1,value2)
            stack.append(result)
            counter = 0

    return stack.pop()


def main():
    while True:
        res = calculate(input("rpn calc> "))
        if res:
            print (res)


if __name__ == '__main__':  # Note: that's "underscore underscore n a m e ..."
    main()