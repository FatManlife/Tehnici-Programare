import requests as rq
# Laborator: funcții, metode și importuri pe web
# Student: <Onofrei Bogdan>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  


#Ex 9
# response = requests.get(BASE_URL)
# print(response.status_code) #atribut
# print(response.ok) #atribut
# print(response.url) #atribut
# print(response.encoding) #atribut

#Ex 10
# try:
#     requests.get(BASE_URL).raise_for_status()
#     requests.get(BASE_URL + "/this-page-neadfsa-not-exist").raise_for_status() 
# except requests.HTTPError:
#     print("A aparut o eroare")

#Ex 11
# for name, val in requests.get(BASE_URL).headers.items():
#     print(f"{name} : {val}")

#Ex 12
# response = requests.get(BASE_URL)
# print(response.headers.get("Server"))
# print(response.headers.get("Content-Type","lipseste"))
# print(response.headers.get("content-type"))
#antetele nu sunt case sensitive

#Ex13
# response = requests.get(BASE_URL)
# print(response.text.lower().count("cyber"))
#pot sa le inlantuiesc deoarece text e atribut lower returneaza un string care poate sa fie contorizat 

#Ex14
# response = requests.get(BASE_URL)
# print(response.text[response.text.find("<title>") + len("<title>") : response.text.find("</title>")].strip())

#Ex15
# res = requests.get(BASE_URL)
# print(len(res.text.splitlines()), max(res.text.splitlines(),key=len))

#Ex16
# res = rq.get(BASE_URL)
# print("Conexiune securizata" if res.url.startswith("https://") else "Conexiune nesecurizata")
    
#Ex17
# res = rq.get("http://cybercor.org")

# for resp in res.history:
#     print(resp.status_code, resp.url)

# print(res.url)

#Ex18
# res1 = rq.get(BASE_URL)
# res2 = rq.head(BASE_URL)

# print(len(res1.content), len(res2.content))
#unul cere sa ii fie trimis tot corpul cu header altul doar headerul

#Ex19
# res = rq.get(BASE_URL)

# if len(res.cookies) == 0:
#     print("There are no coockies")

# for cookie in res.cookies:
#     print(cookie.name, cookie.secure)

#Ex20
# session = rq.Session()
# session.headers.update({"User-Agent": "WebLab-Igor Filip"})

# try:
#     response = session.get(ECHO_URL + "/headers")
#     response.raise_for_status()

#     print(response.text)

# except rq.HTTPError:
#     print("Nu a fost trimis antetul")

#Verificate: respons.json() si response.text unul este metoda altu este atribut

