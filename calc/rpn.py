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
        if token == 'exit':
            print(colored('Exiting RPN Calculator', 'magenta'))
            exit()

    print(colored('     * * * RPN Calculator * * *     ', 'white', 'on_blue'))

    print(colored('Input', 'white', 'on_cyan'))
    for token in arg.split():
        try:
            value = int(token)
            print(colored(token, 'cyan'), end = " ")
        except ValueError:
            print(colored(token, 'yellow'), end = " ")

    print()
    print()

    print(colored('RPN Stack', 'white', 'on_red'))
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

        print(colored(str(count).zfill(2), 'magenta') +
            ': '+ colored(stack, 'blue'))

    if len(stack) == 0:
        raise TypeError(colored('Empty Stack', 'red'))
    if len(stack) != 1:
        raise TypeError(colored('Malformed input: ', 'red') + arg)

    result = stack.pop()

    print(colored('\nResult', 'white', 'on_green'))
    print(colored(result, 'green'))

    print(colored('                                    ', 'white', 'on_blue'))
    return result

def main():
    while True:
        calculate(input('rpn calc> '))

if __name__ == '__main__':
    main()
