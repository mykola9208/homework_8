import sys


def multiply(a, b):
    return a*b


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def divide(a, b):
    return a/b


if __name__ == '__main__':
    args = sys.argv[1:]

    functions = {
        'multiply': multiply,
        'add': add,
        'subtract': subtract,
        'divide': divide
    }

    if len(args) == 2:
        args.insert(0, 'add')

    if len(args) == 3:
        try:
            print(functions[args[0]](int(args[1]), int(args[2])))
        except (ValueError, KeyError):
            print('invalid data value')
            sys.exit(2)
    else:
        print('wrong amount of data')
        sys.exit(2)
