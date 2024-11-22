import argparse
import sys
import requests

def get_content(url):
    page = requests.get("https://www.ynov.com")
    return page

def write_content(page, file):
    f = open(file, "a")
    f.write(page)
    f.close()

def main():
    file = "/tmp/web_page"
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", action="store")

    args = parser.parse_args()

    if not args.url:
        print("You should specify a valid URL with -u or --url.")
        sys.exit(1)

    url = args.url

    page = get_content(url).text

    write_content(page, file)

main()