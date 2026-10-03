import requests as rq
import time
# Laborator: funcții, metode și importuri pe web
# Student: <Onofrei Bogdan>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  

#Ex21
# def fetch(url:str):
#     return rq.get(url, timeout=TIMEOUT)

#print(fetch(BASE_URL).text)

#Ex22
def get_status(url:str) -> int:
    time.sleep(1)
    res = rq.get(BASE_URL + url, timeout=TIMEOUT) 
    return res.status_code

# print(get_status("/"))
# print(get_status("/robots.txt"))
# print(get_status("/sitemap.xml"))

#Ex23
def fetch(url:str, timeout:int=10):
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
    try:
        rq.get(url, timeout=TIMEOUT).raise_for_status()
        return True
    except rq.RequestException:
        return False

#Ex28
def check_paths(base:str, paths: list[str]):
    dict = {}

    for path in paths:
        res = rq.get(base + path, timeout=TIMEOUT)
        dict[path] = res.status_code

    return dict

#print(check_paths(BASE_URL,  ["/", "/robots.txt", "/sitemap.xml"]))

#Ex29
def get_header(url, name, default="lipsește"):
    res = rq.get(url, timeout=TIMEOUT)
    return res.headers[name]

#print(get_header(BASE_URL, name="Server"))

#Ex30
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


# print(security_headers(BASE_URL))

#Ex31
# def score_headers(results: dict):
#     ctr = 0
#     for _, val in results.items():
#         if val: 
#             ctr +=1
#     print(f"{ctr}/{len(results)}")

# score_headers(security_headers(BASE_URL))

#Ex33
def fetch_robots(base):
    res = rq.get(base + "/robots.txt", timeout=10)
    return res.text if res.status_code == 200 else None

def disallowed_paths(robots_text):
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
    str = message

    for detail in details:
        str += " | " + f"{detail}={details[detail]}"

    print(str)

# log("verificat", url=BASE_URL, status=200)

#daca doar o afisam atunci nu o putem utiliza valaorea mai tarziu dar daca o returnam putem 