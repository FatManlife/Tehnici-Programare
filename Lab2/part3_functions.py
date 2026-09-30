import requests as rq
import time
# Laborator: funcții, metode și importuri pe web
# Student: <Onofrei Bogdan>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  

#Ex21
# def fetch(url:str):
#     return rq.get(url)

#print(fetch(BASE_URL).text)

#Ex22
def get_status(url:str) -> int:
    time.sleep(1)
    res = rq.get(BASE_URL + url) 
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

# res = rq.get(BASE_URL)
# print(get_title(res.text))
# help(get_title)

#Ex26
#print(get_status(123))
#adnotarile de timpul dat nu dau erori insa servesc ca recomandari sau indicatii la tipul de date ce ar trebui sa il includa utilizatorul

#Ex27
def page_exists(url:str) -> bool:
    try:
        rq.get(url).raise_for_status()
        return True
    except rq.RequestException:
        return False

#Ex28
def check_paths(base:str, paths: list[str]):
    dict = {}

    for path in paths:
        res = rq.get(base + path)
        dict[path] = res.status_code

    return dict

#print(check_paths(BASE_URL,  ["/", "/robots.txt", "/sitemap.xml"]))

#Ex29
def get_header(url, name, default="lipsește"):
    res = rq.get(url)
    return res.headers[name]

print(get_header(BASE_URL, name="Server"))

#Ex30
