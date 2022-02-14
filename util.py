'''
Useful utils for main formula.

Refrence: https://github.com/hawa130/XDU-PE-query-tool

2022 SuperBart, released under SuperBart Public Domain Software License
'''
#!/bin/python
import json
import time
import base64
from hashlib import md5
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import requests

report = requests.session()

# Following are some useful value I took from the website's js.
# appId and appSecret are used to get sign in the header.
# public_key is used to encrypt the password.
appId = "3685bc028aaf4e64ad6b5d2349d24ba8"
appSecret = "e8167ef026cbc5e456ab837d9d6d9254"
public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq4laolA7zAk7jzsqDb3Oa5pS/uCPlZfASK8Soh/NzEmry77QDZ2koyr96M5Wx+A9cxwewQMHzi8RoOfb3UcQO4UDQlMUImLuzUnfbk3TTppijSLH+PU88XQxcgYm2JTa546c7JdZSI6dBeXOJH20quuxWyzgLk9jAlt3ytYygPQ7C6o6ZSmjcMgE3xgLaHGvixEVpOjL/pdVLzXhrMqWVAnB/snMjpCqesDVTDe5c6OOmj2q5J8n+tzIXtnvrkxQSDaUp8DWF8meMwyTErmYklMXzKic2rjdYZpHh4x98Fg0Q28sp6i2ZoWiGrJDKW29mntVQQiDNhKDawb4B45zUwIDAQAB"

# Print return data clearly, instead of jam.
# For debug.
def printFormatted(toPrint):
    print(json.dumps(toPrint, indent=1, separators=(', ', ': '), ensure_ascii=False))

# Although clear, still ugly.
def getSign(toSend):
    toSend['appId'] = appId
    toSend['appSecret'] = appSecret
    reSort = sorted(toSend.items(),key=lambda s:s[0])
    toDeal = ''
    for i in reSort:
        toDeal += str(i[0]) + '=' + str(i[1]) +'&'
    toDeal = toDeal.strip('&')
    # Robotxm: actually it is md5 xmggtql
    return md5(toDeal.encode('utf-8')).hexdigest()

# I can't believe it could work!
def getTimestrip():
    return str(int((time.time())*1000))

# Copied from the Internet, seems it is widely used:-P
def encrypt(password):
    PubKey = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
    rsakey = RSA.importKey(PubKey)
    cipher = PKCS1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    return cipher_text.decode()

# Hope it could used in every part of the step, finger cross.
def getHead(head, token = None):
    beWith = {
        "version": "99999",
        'channel': "H5",
        'timestamp': getTimestrip(),
        'type': "0",
        'sign': getSign(head),
    }
    if (token != None):
        beWith['token'] = token
    return beWith

# Giant Hogweed Lives!
