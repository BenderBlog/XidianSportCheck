'''
A rewrite of hawa130's XDU-PE-query-tool.

Refrence: https://github.com/hawa130/XDU-PE-query-tool

2022 SuperBart, released under SuperBart Public Domain Software License
'''
#!/bin/python
from util import *

# Used for login.
def login(username, password):
    toLogin = {'uname':username, 'pwd': encrypt(password), 'openid':''}
    getLogined = report.post(
        'https://xd.boxkj.com/app/h5/login', headers=getHead(toLogin), data=toLogin)
    if (getLogined.status_code == 200):
        return getLogined.json()['data']
    else:
        getLogined.raise_for_status()

# Used to get the data about hit the fxxking cards!
# Kill 'em all!
def getRecord(whoami):
    print("正在获取你的打卡成绩")
    # Query Record Code
    queryBody = {'pageIndex': '1', 'pageSize': '150', 'userNum': whoami['userNum'], 'sysTermId': '11'}
    # I am too lazy to show all data to you
    allData = report.post(
        'https://xd.boxkj.com/app/stuPunchRecord/findPager', headers=getHead(queryBody), data=queryBody).json()['data']
    allTime = len(allData)
    print("你总共有{}个记录".format(allTime))
    validData = report.post(
        'https://xd.boxkj.com/app/stuPunchRecord/findPagerOk', headers=getHead(queryBody), data=queryBody).json()['data']
    theoryScore = len(validData)
    print("你的体育打卡分数应该是{}".format(theoryScore))

def getScoreDetail(meaScoreId):
    queryBody = {"meaScoreId": meaScoreId}
    scoreDetail = report.post(
        'https://xd.boxkj.com/app/measure/getStuScoreDetail', headers=getHead(queryBody), data=queryBody).json()['data']
    for each in scoreDetail:
        if 'actualScore' in each:
            print("项目{}的分数是{}\t成绩是{}({})".format(each["examName"],each["score"],each["actualScore"],each["examunit"]))
        else:
            print("项目{}的成绩未录入".format(each["examName"]))

# Used to get your PE test score!
# Are school mad?
def getScore(whoami):
    print("正在获取你的体测成绩")
    queryBody = {"userId": whoami['id']}
    scoreTotal = report.post(
        'https://xd.boxkj.com/app/measure/getStuTotalScore', headers=getHead(queryBody), data=queryBody).json()['data']
    # printFormatted(scoreTotal)
    for i in scoreTotal:
        if 'meaScoreId' in i:
            print("{} 年度的成绩是 {} ，等级是{}。详情如下：".format(i['year'],i['totalScore'],i['rank']))
            getScoreDetail(i["meaScoreId"])
        else:
            print("目前四次总分是{}".format(i['totalScore']))

# Main formula to show these.
if __name__ == "__main__":
    student = login("Your ID","Your Password")
    getRecord(student)
    getScore(student)

