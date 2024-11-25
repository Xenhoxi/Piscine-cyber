import sys
import argparse


def main():
    try:
        print(sys.argv)
        if (len(sys.argv) <= 1):
            assert sys.argv == 1, "Not enought parameters !"
        else:
            data = parser(sys.argv)
        if url_ok(data.url):
            get_img_from_url(data.url)
    except AssertionError as err:
        print(err)


def get_img_from_url():
    pass


def url_ok():
    return (1)


def has_duplicate(string):
    return len(string) != len(set(string))


def parser(argv):
    parser = argparse.ArgumentParser(description="Get all the image from a given URL")
    help_txt = "T/F if the program search for image in url recursively"
    parser.add_argument('-r', action='store_true', help=help_txt)
    help_txt = "Number of recursion"
    parser.add_argument('-l', nargs='?', type=int, const=5, default=5, help=help_txt)
    help_txt = "Where the image will be saved"
    parser.add_argument('-p', nargs='?', type=str, const="./data/", default="./data/", help=help_txt)
    help_txt = "Url where the img will be search"
    parser.add_argument('url', type=str, help=help_txt)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
