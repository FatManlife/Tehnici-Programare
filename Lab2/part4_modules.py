import requests as rq
import time
import urllib
import re
from html.parser import HTMLParser
 
# Laborator: funcții, metode și importuri pe web
# Student: <Onofrei Bogdan>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  

response = rq.get(BASE_URL)

#Ex 35
def decompose_url(url):
    res = urllib.parse.urlparse(url)

    print(f"scheme : {res.scheme}")
    print(f"netloc : {res.netloc}")
    print(f"path : {res.path}")
    print(f"fragment : {res.fragment}")
    print(f"query : {res.query}")

# decompose_url("https://cybercor.org/path?x=1#top")

#Ex36
def compunere_url(base, path):
    res = urllib.parse.urljoin(base, path)
    print(res)

# compunere_url(BASE_URL, "/about")
# compunere_url(BASE_URL, "contact.html")
# compunere_url(BASE_URL, "/index.html")

#Ex37
def extract_links(html):
    res = list(set(re.findall(r'href="([^"]+)"', html)))
    print(res)

# extract_links(response.text)

#Ex38
def split_links(links, domain):
    internal = []
    external = []

    for link in links:
        full_link = urllib.parse.urljoin(domain, link)
        print(full_link)

        if urllib.parse.urlparse(full_link).netloc == nloc:
            internal.append(full_link)
        else:
            external.append(full_link)

    return internal, external

# links = [
#     "/about",
#     "/contact",
#     "https://google.com",
#     "https://github.com/test"
# ]

# internal, external = split_links(links, "https://example.com")

# print(internal)
# print(external)

#Ex39

class ImageFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
 
    def handle_starttag(self, tag, attrs):
        pass

HTMLParser.handle_starttag("img","src")