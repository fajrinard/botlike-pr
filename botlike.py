import requests, json, sys

host = "https://api.prisga.id/api/v7-release/method"
headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"}

def login(username, password):
    link = host + "/account.signIn"
    data = {'username': username, 'password': password, 'clientId': '1'}
    r = requests.post(url = link, data = data, headers = headers)
    hasil = r.text
    hasil = json.loads(hasil)
    return hasil

def like(token, accid, item):
    link = host + "/items.like"
    data = {'accessToken': token, 'accountId': accid, 'itemId': item}
    r = requests.post(url = link, data = data, headers = headers)
    hasil = r.text
    hasil = json.loads(hasil)
    return hasil

def stream(token, accid):
    link = host + "/stream.get"
    data = {'accessToken': token, 'language': 'en', 'accountId': accid, 'itemId': 0}
    r = requests.post(url = link, data = data, headers = headers)
    hasil = r.text
    hasil = json.loads(hasil)
    return hasil

def botlike(token, accid, hasil):
    target = {}
    for a in hasil['items']:
        if a['myLike'] == False:
            target[(a['id'])] = a['fromUserFullname']
    for a in target.items():
        data = like(token, accid, a[0])
        err = ''
        er = ''
        if data['error'] == True:
            err += 'Fail'
            er += str(data['error_code'])
        if like == 'Fail':
            print ('\n (Like)\n user: '+a[1]+', post id: '+a[0]+', like: '+err+', error code: '+er+'.')

try:
    f = open('token.txt', 'r')
    x = f.read().split('\n')
    acc = x[0]
    tok = x[1]
except:
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        x = login(username, password)
        acc = x['accountId']
        tok = x['accessToken']
        f = open('token.txt', 'w')
        f.write(acc+'\n'+tok)
        f.close()
    except:
        pass

while True:
    try:
        h = stream(tok, acc)
        botlike(tok, acc, h)
    except Exception as e:
        print(e)