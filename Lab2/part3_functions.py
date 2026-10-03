import requests as rq
import time
# Laborator: funcții, metode și importuri pe web
# Student: <Onofrei Bogdan>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  

#Ex21
# def fetch(url:str):
"""Trimite o cerere HTTP către URL-ul specificat și returnează răspunsul."""
#     return rq.get(url, timeout=TIMEOUT)

#print(fetch(BASE_URL).text)

#Ex22
def get_status(url:str) -> int:
    """Returnează codul de stare HTTP pentru URL-ul specificat."""
    time.sleep(1)
    res = rq.get(BASE_URL + url, timeout=TIMEOUT) 
    return res.status_code

# print(get_status("/"))
# print(get_status("/robots.txt"))
# print(get_status("/sitemap.xml"))

#Ex23
def fetch(url:str, timeout:int=10):
    """Trimite o cerere HTTP către URL-ul specificat și returnează răspunsul."""
    return rq.get(url, timeout=timeout)

# print(fetch(BASE_URL))
# print(fetch(BASE_URL,3))

#Ex24/25
def get_title(html:str) -> str:
    """Extrage titlu din html text."""
    return html[html.find("<title>") + len("<title>") : html.find("</title>")].strip() 

# res = rq.get(BASE_URL, timeout=TIMEOUT)
# print(get_title(res.text))
# help(get_title)

#Ex26
#print(get_status(123))
#adnotarile de timpul dat nu dau erori insa servesc ca recomandari sau indicatii la tipul de date ce ar trebui sa il includa utilizatorul

#Ex27
def page_exists(url:str) -> bool:
    """Verifică dacă pagina specificată există și poate fi accesată.""" 
    try:
        rq.get(url, timeout=TIMEOUT).raise_for_status()
        return True
    except rq.RequestException:
        return False

#Ex28
def check_paths(base:str, paths: list[str]):
    """Verifică codul de stare HTTP pentru fiecare cale relativă specificată."""
    dict = {}

    for path in paths:
        res = rq.get(base + path, timeout=TIMEOUT)
        dict[path] = res.status_code

    return dict

#print(check_paths(BASE_URL,  ["/", "/robots.txt", "/sitemap.xml"]))

#Ex29
def get_header(url, name, default="lipsește"):
    """Returnează valoarea unui header HTTP specificat pentru URL-ul dat."""
    res = rq.get(url, timeout=TIMEOUT)
    return res.headers[name]

#print(get_header(BASE_URL, name="Server"))

#Ex30
def security_headers(url:str):
    """Verifică prezența headerelor HTTP de securitate pentru URL-ul specificat."""
    res = rq.get(url, timeout=TIMEOUT)
    d = {
        "Strict-Transport-Security" : True if res.headers.get("Strict-Transport-Security") else False,
        "Content-Security-Policy" : True if res.headers.get("Content-Security-Policy") else False,
        "X-Frame-Options" : True if res.headers.get("X-Frame-Options") else False,
        "X-Content-Type-Options" : True if res.headers.get("X-Content-Type-Options") else False,
        "Referrer-Policy" : True if res.headers.get("Referrer-Policy") else False
    }

    return d


# print(security_headers(BASE_URL))

#Ex31
# def score_headers(results: dict):
#     """Verifica cat din headeri sunt prezenti"""
#     ctr = 0
#     for _, val in results.items():
#         if val: 
#             ctr +=1
#     print(f"{ctr}/{len(results)}")

# score_headers(security_headers(BASE_URL))

#Ex33
def fetch_robots(base):
    """Descarcă fișierul robots.txt al site-ului și returnează conținutul acestuia."""
    res = rq.get(base + "/robots.txt", timeout=10)
    return res.text if res.status_code == 200 else None

def disallowed_paths(robots_text):
    """Extrage și returnează căile interzise din conținutul unui fișier robots.txt."""
    if robots_text == None:
        return 

    paths = []


    for line in robots_text.splitlines():
        if line.startswith("Dissalow:"):
            paths.append(line.split(":")[1])

    return paths
    

# print(disallowed_paths(fetch_robots(BASE_URL)))

#Ex33
def  response_times(*urls):
    """Măsoară și returnează timpul de răspuns pentru fiecare URL specificat."""
    if len(urls) == 0: 
        return 

    d = {}

    for url in urls:
        res = rq.get(url)
        d[url] = res.elapsed.total_seconds()

    return d

# print(response_times(BASE_URL ,BASE_URL + "/robots.txt"))

#Ex34
def log(message, **details):
    """Afișează un mesaj împreună cu detaliile suplimentare specificate."""
    str = message

    for detail in details:
        str += " | " + f"{detail}={details[detail]}"

    print(str)

# log("verificat", url=BASE_URL, status=200)

#daca doar o afisam atunci nu o putem utiliza valaorea mai tarziu dar daca o returnam putem 