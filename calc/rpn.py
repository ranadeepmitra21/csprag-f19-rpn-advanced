#!/usr/bin/env python3

import operator
import sys
from termcolor import colored, cprint

operators = {
        '+': operator.add,
        '-': operator.sub,
        "*": operator.mul,
        "/": operator.floordiv,
        "^": operator.pow,
        "mod": operator.mod,
        }

def calculate(arg):
    print(colored('The stack:', 'red'))
    stack = list()
    count = 0
    for token in arg.split():
        count += 1
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)

        print(colored(count, 'red') + ': '+ colored(stack, 'blue'))

    #for token in string.split():
        #if token == '+':
         #   arg1 = stack.pop()
          #  arg2 = stack.pop()
           # result = arg1 + arg2
           # stack.append(result)
       # elif token == '-':
        #    arg2 = stack.pop()
         #   arg1 = stack.pop()
          #  result = arg1 - arg2
           # stack.append(result)
       # else:
        #    stack.append(int(token))

    if len(stack) == 0:
        raise TypeError('Empty Stack')
    if len(stack) != 1:
        raise TypeError('Malformed input: ' + arg)

    print(colored('\nResult', 'green'))
    print(colored(stack, 'green'))

    return stack.pop()

def main():
    while True:
        calculate(input('rpn calc> '))


if __name__ == '__main__':
    main()
