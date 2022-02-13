'''
A rewrite of hawa130's XDU-PE-query-tool.

Refrence: https://github.com/hawa130/XDU-PE-query-tool

2022 SuperBart, released under SuperBart Public Domain Software License

SuperBart Public Domain Software License

Following are non-additional terms:

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

Two additional terms:

1. As long as you use this software, you acknowledge that the author of
the software strongly against improper competition and labour, for
example, 996 working schedule. And he or she dislike anything which are
bureaucratization, such as meaningless meeting and courses.

2. The additional terms have no mandatory in either laws, or other fields.
You don't need to agree with the additional terms in order to use this
software. And you may delete the additional terms when using this software,
as long as you obey the non-additional terms above.
'''
#!/bin/python
#!/bin/python
import requests
import time
import base64
from hashlib import md5
import json
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

# Two getSign formula need to be rewritten, this part is just functionable right now.
# After all, I have just started writing python for two days! I treat them like shell script:-P
def getSignForBody(username):
    toDeal = "appId=3685bc028aaf4e64ad6b5d2349d24ba8&appSecret=e8167ef026cbc5e456ab837d9d6d9254&pageIndex=1&pageSize=150&sysTermId=11&userNum=" + username
    # Robotxm: this sign is calculated with md5. xmggtql
    return md5(toDeal.encode('utf-8')).hexdigest()
def getSignForPassword(username, password):
    toDeal = "appId=3685bc028aaf4e64ad6b5d2349d24ba8&appSecret=e8167ef026cbc5e456ab837d9d6d9254&openid=&pwd=" + password + "&uname=" + username
    return md5(toDeal.encode('utf-8')).hexdigest()

# I can't believe it could work!
def getTimestrip():
    return str(int((time.time())*1000))

def encrypt(password):
    public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq4laolA7zAk7jzsqDb3Oa5pS/uCPlZfASK8Soh/NzEmry77QDZ2koyr96M5Wx+A9cxwewQMHzi8RoOfb3UcQO4UDQlMUImLuzUnfbk3TTppijSLH+PU88XQxcgYm2JTa546c7JdZSI6dBeXOJH20quuxWyzgLk9jAlt3ytYygPQ7C6o6ZSmjcMgE3xgLaHGvixEVpOjL/pdVLzXhrMqWVAnB/snMjpCqesDVTDe5c6OOmj2q5J8n+tzIXtnvrkxQSDaUp8DWF8meMwyTErmYklMXzKic2rjdYZpHh4x98Fg0Q28sp6i2ZoWiGrJDKW29mntVQQiDNhKDawb4B45zUwIDAQAB"
    PubKey = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
    rsakey = RSA.importKey(PubKey)
    cipher = PKCS1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    return cipher_text.decode()

def login(username, password):
    # Login Code
    report = requests.session()
    toLogin = {
        'uname':username,
        'pwd': encrypt(password),
        'openid':''
    }
    beWith = {
        'Content-Type': 'application/x-www-form-urlencoded',
        "version": "99999",
        'channel': "H5",
        'timestamp': getTimestrip(),
        'type': "0",
        'sign': getSignForPassword(username, toLogin['pwd']),
    }
    situation = report.post(
        'https://xd.boxkj.com/app/h5/login', headers=beWith, data=toLogin)
    print(situation.json()['returnMsg'])
    token = situation.json()['data']['token']
    data_id = situation.json()['data']['id']

    # Query Code
    queryBody = {
        'pageIndex': '1',
        'pageSize': '150',
        'userNum': toLogin['uname'],
        'sysTermId': '11'
    }
    forQuery = {
        'Content-Type': 'application/x-www-form-urlencoded',
        "version": "99999",
        'channel': "H5",
        'type': "0",
        'token': token,
        'timestamp': getTimestrip(),
        'sign': getSignForBody(username),
    }
    # Need to be more comfortable to see.
    returnAllData = report.post(
        'https://xd.boxkj.com/app/stuPunchRecord/findPager', headers=forQuery, data=queryBody)
    allTime = len(returnAllData.json()['data'])
    print("你总共有 {} 个记录。".format(allTime))
    returnValidData = report.post(
        'https://xd.boxkj.com/app/stuPunchRecord/findPagerOk', headers=forQuery, data=queryBody)
    theoryScore = len(returnValidData.json()['data'])
    print("你的体育打卡分数应该是 {}  。".format(theoryScore))
    if theoryScore > 30:
        print("兄弟，最多30分好嘛。")
    elif theoryScore == 30:
        print("正好:-)")
    else:
        print("快打卡吧，一寸光阴一寸金啊！")
    # Magic smoke during getting my PE's score, god damn it!
    '''
    returnScoreTotal = report.post(
        'https://xd.boxkj.com/app/measure/getStuTotalScore', headers=forQuery, data={"userId":data_id})
    print(returnScoreTotal.json())
    returnScoreDetail = report.post(
        'https://xd.boxkj.com/app/measure/getStuScoreDetail', headers=forQuery, data={"userId":data_id})
    print(returnScoreDetail.json())
    '''

if __name__ == "__main__":
    login("Your ID","Your Password")
