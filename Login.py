import requests
  
request={
    'Accept' :'application/json, text/plain, */*',
    'Accept-Encoding' :'gzip, deflate, br',
    'Accept-Language' :'en-GB,en-US;q=0.8,en;q=0.6',
    'Authorization' :'Basic c3VkaGlyLnJhb0BhZ2lsb25lLmNvbTpzaGRmZ3k2NTZASEdGQQ==',
    'Connection' :'keep-alive',
    'Content-Type' :'application/json',
    'Host' :'cs-auth.agilone.com',
    'Origin' :'https://cs-config.agilone.com',
    'Referer' :'https://cs-config.agilone.com/login',
    'User-Agent' :'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
r = requests.post('https://cs-auth.agilone.com/authentication?action=login', headers=request)
  
print r.status_code
print r.headers
print r.content

#('sudhir.rao@agilone.com','shdfgy656@HGFA')