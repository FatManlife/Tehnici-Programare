import requests as rq
import math
import ssl 
import socket
import json
import time
import urllib
import re
from html.parser import HTMLParser
import hashlib
 
# Laborator: funcții, metode și importuri pe web
# Student: <Onofrei Bogdan>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  

response = rq.get(BASE_URL, timeout=TIMEOUT)

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
        for attr in attrs:
            if attr[0].lower() == "src" and tag.lower() == "img": 
                self.images.append(attr[1])


test_html = """
<html><body>
  <img src="/logo.png" alt="Logo">
  <IMG SRC="poza.jpg">
  <img alt="imagine fără src">
  <img src="https://cdn.example.com/banner.webp" />
  <a href="/despre">Aceasta nu este o imagine</a>
</body></html>
"""
 
# finder = ImageFinder()
# finder.feed(test_html)
# print(finder.images)
 
# assert finder.images == [
#     "niga",
#     "/logo.png",                            # imagine obișnuită
#     "poza.jpg",                             # tag scris cu majuscule
#     "https://cdn.example.com/banner.webp",  # tag care se închide singur
# ], "Parserul nu a găsit exact imaginile așteptate"

# print("Testul a trecut!")

# response = rq.get(BASE_URL, timeout=TIMEOUT)
# finder = ImageFinder()
# finder.feed(response.text)
# print(len(finder.images), "imagini găsite")
# print(response.text.lower().count("<img"))

# for src in finder.images:
#     print(src)

#Ex40
def page_fingerprint(url):
    response = rq.get(url, timeout=TIMEOUT)
    return hashlib.sha256(response.content).hexdigest()

# print(page_fingerprint(BASE_URL))
#Reprezentarea ar fi diferita daca in loc de hexdigits am utiliza alta functie de conversie sau nici una sau daca contentul la pagina ar fi diferit

#EX41
def save_read_json(url):
    res = rq.get(url, timeout=TIMEOUT) 

    with open("data.json", "w+") as file:
        json.dump(dict(res.headers), file, indent=2)

    d = {}

    with open("data.json", "r+") as file:
        d = json.load(file)

    key,item = next(iter(d.items()))
    print(key,item)

# save_read_json(BASE_URL)

#Ex42
def resolve(hostname):
    return socket.gethostbyname(hostname)
# print(resolve("cybercor.org"))

#Ex43
def cert_days_left(hostname):
    context = ssl.create_default_context()
    sock = socket.create_connection((hostname, 443))
    sock = context.wrap_socket(sock, server_hostname=hostname)
    cert = sock.getpeercert()
    expiry = cert["notAfter"]
    seconds = ssl.cert_time_to_seconds(expiry)
    return str(math.ceil(seconds/86400)) + " days until it expires "

# print(cert_days_left("cybercor.org"))


#Verificati: in ex 39 clasa apeleaza automat starttag() cand faci parsing