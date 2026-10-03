import time
import urllib
import math
import ssl
import socket
import csv
import requests as rq

DEFAULT_HEADERS = {"User-Agent": "WebLab-<numele vostru>"}

#Ex44
def fetch(url:str, timeout:int=10):
    return rq.get(url, timeout=timeout,headers=DEFAULT_HEADERS)

def get_status(base_url, url:str, timeout) -> int:
    time.sleep(1)
    res = rq.get(base_url + url, timeout=timeout) 
    return res.status_code

def get_title(html:str) -> str:
    """Extrage titlu din html text."""
    return html[html.find("<title>") + len("<title>") : html.find("</title>")].strip() 

def security_headers(url:str, timeout ):
    res = rq.get(url, timeout=timeout)
    d = {
        "Strict-Transport-Security" : True if res.headers.get("Strict-Transport-Security") else False,
        "Content-Security-Policy" : True if res.headers.get("Content-Security-Policy") else False,
        "X-Frame-Options" : True if res.headers.get("X-Frame-Options") else False,
        "X-Content-Type-Options" : True if res.headers.get("X-Content-Type-Options") else False,
        "Referrer-Policy" : True if res.headers.get("Referrer-Policy") else False
    }

    return d

#Ex49
def check_paths(base:str, paths: list[str], timeout = 10):
    l = []

    for path in paths:
        l1 = []
        res = rq.get(base + path, timeout=timeout)
        l1.append(path) 
        l1.append(res.status_code)
        l1.append(res.elapsed.total_seconds())
        l.append(l1)

    return l 

def create_csv(base:str, path: list[str]):
   l = [["path"],["status"],["checked_at"]]
   for val in check_paths(base,path):
        l.append(val)

   with open("/home/seven/Desktop/TP/Lab2/web_lab/report.csv", "w") as file:
       writer = csv.writer(file)
       writer.writerows(l)

def resolve(hostname):
    return socket.gethostbyname(hostname)


#EX46-deoarece can interpretorul interpreteaza aceasta linie el verifica mai intai unde se afla(anume in cazul acesta el verifica daca se afla in modul) si ruleaza programul in dependenta de asta
if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org", "", 10))

def security_headers(url:str):
    res = rq.get(url, timeout=TIMEOUT)
    d = {
        "Strict-Transport-Security" : True if res.headers.get("Strict-Transport-Security") else False,
        "Content-Security-Policy" : True if res.headers.get("Content-Security-Policy") else False,
        "X-Frame-Options" : True if res.headers.get("X-Frame-Options") else False,
        "X-Content-Type-Options" : True if res.headers.get("X-Content-Type-Options") else False,
        "Referrer-Policy" : True if res.headers.get("Referrer-Policy") else False
    }

    return d
    
def score_headers(results: dict):
    ctr = 0
    for _, val in results.items():
        if val: 
            ctr +=1
    print(f"{ctr}/{len(results)}")

def cert_days_left(hostname):
    context = ssl.create_default_context()
    sock = socket.create_connection((hostname, 443))
    sock = context.wrap_socket(sock, server_hostname=hostname)
    cert = sock.getpeercert()
    expiry = cert["notAfter"]
    seconds = ssl.cert_time_to_seconds(expiry)
    return str(math.ceil(seconds/86400)) + "de zile rămase"


def split_links(res, url):
    domain = urllib.parse.urlparse(url).hostname

    links = res.findall(r'<a[^>]+href=["\']([^"\']+)["\']', res.text, res.I)

    internal = []
    external = []

    for link in links:
        full_link = urllib.parse.urljoin(url, link)
        hostname = urllib.parse.urlparse(full_link).hostname

        if hostname == domain:
            internal.append(full_link)
        else:
            external.append(full_link)

    return internal, external

def disallowed_paths(html):
    if html == None:
        return 

    paths = []


    for line in html.splitlines():
        if line.startswith("Dissalow:"):
            paths.append(line.split(":")[1])

    return paths

def get_redirects(response):

    redirects = []

    for r in response.history:
        redirects.append(f"{r.status_code} -> {r.headers["Location"]}")

    return redirects
    

#Ex50
def site_report(url):
    links = [
        "/about",
        "/contact",
        "https://google.com",
        "https://github.com/test"
    ]

    internal, external = split_links(links, "https://example.com")

    lie = [internal, external]

    res = fetch(url)

    dict = {
        "Cod de stare": res.status_code,
        "Titlu": get_title(res.text),
        "Adresă IP": resolve("cybercor.org"),
        "Redirecționări": get_redirects(res),
        "Scor securitate": score_headers(security_headers(url)),
        "Certificat": cert_days_left("cybercor.org"),
        "Legături": lie,
        "Căi interzise": disallowed_paths(res.text),
    }
