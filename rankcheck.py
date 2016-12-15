import sys
import os
import gobject
import argparse
from lxml import html
import requests



EMAIL = "<email>"
PWORD = "<password>"

LOGIN_URL = "http://www.saltybet.com/authenticate?signin=1"
URL = "http://www.saltybet.com"

def main():

    session_requests = requests.session()

# Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    signin = list(set(tree.xpath("//input[@name='authenticate']/@value")))[0]

# Create payload
    payload = {
        "email": EMAIL, 
        "pword": PWORD, 
        "authenticate": signin
    }

# Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

# Scrape rank data
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    rank_number = tree.xpath('//span[@class="navbar-text"]/text()')

print "%s" % rank_number

if __name__ == '__main__':
    main()
