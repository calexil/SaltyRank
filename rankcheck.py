#Welcome to SaltyRank, a tool to check your rank on saltybet.com from terminal
from lxml import html
import requests
import getpass


#If you prefer not to enter your password every time simply change the lines below so they read
#EMAIL = "your email"
#PWORD = "your password"
EMAIL = raw_input("What is your email? ")
PWORD = getpass.getpass("Enter your password: ")

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

# Perform Login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

# Scrape rank data from navbar span
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    rank_number = tree.xpath('//span[@class="navbar-text"]/text()')

    print "%s" % rank_number

if __name__ == '__main__':
    main()
