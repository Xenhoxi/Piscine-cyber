import sys
import re

def main():
    try:
        print(sys.argv)
        if (len(sys.argv) <= 1):
            assert sys.argv == 1, "Not enought parameters !"
        else:
            data = parser(sys.argv)
            print(data)
    except AssertionError as err:
        print(err)


def param_checker(data, arg):
    if 'r' in arg and not data['r']:
        data['r'] = True
    elif 'l' in arg and not data['l']:
        data['l'] 
    pass


def parser(argv):
    data = {"url": "", "r": False, "l": 5, "p": './data/'}
    param_pattern = r"^\-[rlp]$"

    for i in range(1, len(argv)):
        if re.match(param_pattern, argv[i]):
            if 'r' in argv[i]:
                data['r'] = True
            if 'l' in argv[i] and i + 1 < len(argv) and argv[i + 1].isnumeric():
                data['l'] = int(argv[i + 1])
            if 'p' in argv[i] and i + 1 < len(argv):
                data['p'] = argv[i + 1]
        elif i == len(argv) - 1:
            data['url'] = argv[i]
        else:
            raise AssertionError("Bad parameters")
    return data


if __name__ == '__main__':
    main()
