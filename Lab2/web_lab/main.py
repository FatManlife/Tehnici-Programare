import webtools
import argparse

#Ex45 - daca vom face o functie get_title atunci interpretorul va prioritiza functia locala in favoarea celei importate
from webtools import get_title, security_headers, DEFAULT_HEADERS

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  

parser = argparse.ArgumentParser("")
parser.add_argument("url")
args = parser.parse_args()


# print(webtools.fetch(BASE_URL).text)
#Ex47
# print(DEFAULT_HEADERS)
#Ex48
#print(webtools.fetch(args.url).text)
#Ex49
# webtools.create_csv(BASE_URL, ["/", "/robots.txt", "/sitemap.xml"])
#Ex50
webtools.site_report(args.url)