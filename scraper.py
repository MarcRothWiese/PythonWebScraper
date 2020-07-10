# Import libraries
from bs4 import BeautifulSoup
import urllib.request

# The source code
url = 'https://wiese.xyz/'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) '\
           + 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
           + 'Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url, headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html = response.read()

# Parsing the HTML
soup = BeautifulSoup(html, "html.parser")

# Find all A tags
list = soup.find_all("a")

# Looping though all the results
for x in list:
    print(x["href"])


