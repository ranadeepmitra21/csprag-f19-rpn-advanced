#!/usr/bin/env python3

import operator
import sys
import readline
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

    for token in arg.split():
        try:
            value = int(token)
            print(colored(token, 'cyan'), end = " ")
        except ValueError:
            print(colored(token, 'yellow'), end = " ")

    print()
    print()

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
