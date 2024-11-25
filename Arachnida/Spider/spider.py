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


def fill_param(argv, i, data):
    if 'r' in arg and not data['r']:
        data['r'] = True
    elif 'l' in arg and not data['l']:
        data['l'] = int(argv[i + 1])
    pass


def parser(argv):
    data = {"url": "", "r": False, "l": None, "p": './data/'}
    param_pattern = r"^-([rlp]{1,3})$"
    nb_param = 0

    for i in range(1, len(argv)):
        if '-' in argv[i]:
            if re.match(param_pattern, argv[i]) and no_duplicate(argv[i]):
                fill_param(argv, i, data)
            else:
                print(argv[i])
                raise AssertionError("Bad parameters")
        elif i == len(argv) - 1:
            data['url'] = argv[i]
        print(nb_param)
    return data


# def check_all_param(argv):

#     for i in range(1, len(argv)):
#         if "-" in argv[i]:
#             if re.match(param_pattern, argv[i]):
#                 continue
#             else:
#                 raise AssertionError("Bad parameters")
#     return 1


# def check_r(argv, data):
#     for i in range(1, len(argv)):
#         if "-" in argv[i]:
#             if argv[i] == "-r":
#                 if not data['r']:
#                     data['r'] = True
#                     data['l'] = 5
#                 else:
#                     raise AssertionError("Bad parameters")
#             else:


# def check_l(argv, data):
#     for i in range(1, len(argv)):
#         if argv[i] == "-l" and i + 1 < len(argv) and argv[i + 1]:
#             if not data['l'] or data['l'] == 5:
#                 data['l'] = int(argv[i + 1])
#             else:
#                 raise AssertionError("Bad parameters")


if __name__ == '__main__':
    main()
