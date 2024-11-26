import sys
import argparse
import os
from curl_cffi import requests as cureq
from bs4 import BeautifulSoup


def main():
    try:
        if (len(sys.argv) <= 1):
            assert sys.argv == 1, "Not enought parameters !"
        else:
            data = parser(sys.argv)
        if url_ok(data.url):
            get_img_from_url(data.url)
    except AssertionError as err:
        print(err)


def get_img_from_url(url):
    print(url)
    req = cureq.get(url, impersonate='chrome')
    print(req.status_code)
    soup = BeautifulSoup(req.text, "html.parser")
    all_img = soup.find_all("img")
    for img in all_img:
        src = img.get('src')
        if src:
            if str(src).endswith(('.png', '.jpg', '.jpeg', '.jpeg', '.gif', '.bmp')):
                img_req = cureq.get(str(src), impersonate='chrome')
                print(str(src), img_req.status_code)
                if img_req.status_code == 200:
                    with open("./data/" + os.path.basename(str(src)), "wb") as file:
                        file.write(img_req.content)
                else:
                    img_req = cureq.get(os.path.dirname(url) + '/' + str(src), impersonate='chrome')
                    print(os.path.dirname(url) + '/' + str(src), img_req.status_code)
                    if img_req.status_code == 200:
                        with open("./data/" + os.path.basename(str(src)), "wb") as file:
                            file.write(img_req.content)


def url_ok(url):
    try:
        cureq.get(url, impersonate='chrome')
        return 1
    except Exception:
        print("Impossible to access the url")
        return 0


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
