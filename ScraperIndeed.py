#!/usr/bin/python3

"""module docstring"""

__version__ = "0.1.0"

import sys
import urllib.request
import ssl
from bs4 import BeautifulSoup

print(sys.version, end='\n\n')

def main(terms, loc):
    """docstring"""
    print('Scraping all {} from {}'.format(terms, loc))
    terms = terms.replace(' ', '+')
    loc = loc.replace(' ', '+')
    loc = loc.replace(',', '%2C')
    requrl = 'https://www.indeed.com/jobs?q={}&l={}'.format(terms, loc)
    print(requrl)
    https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
    opener = urllib.request.build_opener(https_sslv3_handler)
    urllib.request.install_opener(opener)
    resp = opener.open(requrl)
    udata = resp.read().decode('utf-8')
    asciidata=udata.encode("ascii","ignore")
    print(asciidata)

if __name__ == "__main__":
    main('DevOps Engineer', 'San Rafael, CA')
