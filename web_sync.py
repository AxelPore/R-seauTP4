import argparse
import requests

def get_content(url):
    page = requests.get(url)
    return page
    
def write_content(page, file):
    f = open(file, "a")
    f.write(page)
    f.close()

def main():
    file = "/tmp/web_page"
    parser = argparse.ArgumentParser()
    parser.add_argument("web_sync.py", action="store")
    args = parser.parse_args()
    url = args
    print(url)
    page = get_content(url)
    write_content(page, file)
    
main()