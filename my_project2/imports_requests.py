#!/usr/bin/env python3

from requests import get

def main():
    print("requests.get succcessfully imported")
    url = 'http://cohpy.org'
    print(f"attempting to fetch {url}")
    response = get(url)
    print(response)

if __name__ == '__main__':
    main()
