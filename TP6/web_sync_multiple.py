import argparse
import sys
import requests
from os import path

def get_content(url):
    page = requests.get(url)
    page.raise_for_status()
    return page

def write_content(page, file):
    f = open(file, "a")
    f.write(page)
    f.close()

def main():
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", action="store")

    args = parser.parse_args()

    if not args.file:
        print("You should specify a valid file with -f or --file.")
        sys.exit(1)

    urlfile = args.file
    urlfile = "/tmp/" + urlfile
    with open(urlfile, 'r') as f :
        for line in f :
            page = get_content(line.strip()).text
            file = "/tmp/web_" + path.basename(line.strip())
            write_content(page, file)

    
    

main()