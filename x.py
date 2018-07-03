# -*-coding: utf-8 -*-
from linepy import *
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse, timeit, traceback
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#cl = LINE()
cl = LINE('EucxcMmmZkVBXiXhYkna.FhQCwCujRyNq5pMum4MTUG.+Q+WJWjfiXkJRryKNfBAT/hbgjOfM3QZCGRTSV99vhg=')
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))
print ("====國民ㄩㄗ登入成功====")
#k1 = LINE()
k1 = LINE('Eu4A9BVxJpC8JK95xVE1.v5e2pzIr/vTl1S6SSIih0q.fcABNkRxas0zmT64+BLmNipNKWHYemysC/K5u23FPbY=')
k1.log("Auth Token : " + str(k1.authToken))
k1.log("Timeline Token : " + str(k1.tl.channelAccessToken))
print ("====Bot1登入成功====")
#k2 = LINE()
k2 = LINE('EuzL0r2dYa6dwnmAUZn7.hYVUGM5iivxCNrlcChxSPW.d9cVI7s+Fr5g/8MJ7eqEIwl1OuBskpJQTZyuSORK8tw=')
k2.log("Auth Token : " + str(k2.authToken))
k2.log("Timeline Token : " + str(k2.tl.channelAccessToken))
print ("====Bot2登入成功====")
#k3 = LINE()
k3 = LINE('EuYRA9r1C1LFeFo3Eie1.aleqfE7GuDFMnIRmFot+yq.LFLdFBbu8hi8DMlUpHLGavFH8pAn5c7kIfYKubYDbfU=')
k3.log("Auth Token : " + str(k3.authToken))
k3.log("Timeline Token : " + str(k3.tl.channelAccessToken))
print ("====Bot3登入成功====")
#k4 = LINE()
k4 = LINE('Euy2J1QW8Ir0HOtbeUAf.XvQeWsOMx9EsZAhfPvUxlW.6r5npO1+JQKXUuL+qThtBQdY79HLVC9LU94rLinIAZk=')
k4.log("Auth Token : " + str(k4.authToken))
k4.log("Timeline Token : " + str(k4.tl.channelAccessToken))
print ("====Bot4登入成功====")

KAC = [cl,k1,k2,k3,k4]
clMID = cl.profile.mid
AMID = k1.profile.mid
BMID = k2.profile.mid
CMID = k3.profile.mid
DMID = k4.profile.mid
Bots = [clMID,AMID,BMID,CMID,DMID]

clProfile = cl.getProfile()
k1Profile = k1.getProfile()
k2Profile = k2.getProfile()
k3Profile = k3.getProfile()
k4Profile = k4.getProfile()

lineSettings = cl.getSettings()
k1Settings = k1.getSettings()
k2Settings = k2.getSettings()
k3Settings = k3.getSettings()
k4Settings = k4.getSettings()

oepoll = OEPoll(cl)
oepoll1 = OEPoll(k1)
oepoll2 = OEPoll(k2)
oepoll3 = OEPoll(k3)
oepoll4 = OEPoll(k4)

#==============================================================================#

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
banOpen = codecs.open("ban.json","r","utf-8")
adminOpen = codecs.open("admin.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)
ban = json.load(banOpen)
admin = json.load(adminOpen)

msg_dict = {}
bl = [""]
#==============================================================================#
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = ban
        f = codecs.open('ban.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = admin
        f = codecs.open('admin.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """╔══════════════
╠♥  ㄩㄗ5隻保鑣半垢  ♥
║
╠══✪〘 指令一覽表 〙✪═══
╠➥ Help 查看指令
╠➥ restart 重新啟動
╠➥ Speed 速度
╠➥ "集合" 保鑣進群
╠➥ "解散" 保鑣退群
╠➥ "報數" 報數測試
╠➥ autoAdd on/off 自動加入
╠➥ autoJoin on/off 自動進群
╠➥ detect on/off 標註偵測
╠➥ timeline on/off 文章網址預覽
╠➥ ri @ 來回機票
╠➥ setread 已讀點設置
╠➥ cancelread 取消偵測
╠➥ Checkread 已讀偵測
║
║〘使用者By:ㄩㄗ
╚═ 作成者By:い悠遠ゞܣ􀬁􀆐􀬁天下第一喵～〙"""
    return helpMessage
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile() 
contact = k1.getProfile() 
contact = k2.getProfile() 
contact = k3.getProfile() 
contact = k4.getProfile() 
backup = cl.getProfile() 
backup = k1.getProfile() 
backup = k2.getProfile() 
backup = k3.getProfile() 
backup = k4.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
creator =['u7c7a9c59c509ad89d0e4f9943389adba','ua10c2ad470b4b6e972954e1140ad1891','u5d44e9d1b556910a39b774d4020e6dc6','u5791363d9891f95b4bd6ceacb22207d1','u7238d00856b10d6ca735f363a92feca3','u52afe1d4ea5332242efacfeb9190d2a3','ua10c2ad470b4b6e972954e1140ad1891','ue3dedea686b4bd3c946715c8684d50db','ucd5b65e2074195908e9459b9b1103b36','ubcf921fb4313eafa16dd8512270cbca1','u58b84c3a13fa7a5a55279cd77b3e03f6','u471d64ce29a82b8a0e5c0f4d5e1c6ef3','u17dd300568da75eef185af17397d175b','ub77514d16c832a36aa3c8ecea36326be','ub40c47e7bec584026f575f3b0cf8e44b','u8afb9f9c805ed5723947dce109e34df7','uc216d8664c4e1f43772c98b1b0b8956e','u67c43239c865dfce6addb41c6b3c0edd','uf8658b92e7d79f11083d5354d1ba547b','u11b00263de7ff1cef2481434685a7e7b','uff56d19ed9502fdf33b75cea3f7a9f63','u00aacc1d54fe9c1fabc5ba7242cd7013','u7679ba9bed776f6fecbb49e27f83c29d','u9b035730aeb9d17410d96e95ad2503b8','u560c06e2d7a280e2a6de821a7614f13c','u0f26401bbba4a99eff1412a1ac27b213','u33c2b73d7daa507d123d8c571ebe9eb3','ufba410943361a1fdc81693f6a9c977e8','u4858e902079f8ceee02533b19bb7ce4a','uac3106a6f3420a5b003e0c0e5b087bcf','u1b6ab4074456a542a10af64de05e2dbb']
admin =['u7c7a9c59c509ad89d0e4f9943389adba','ua10c2ad470b4b6e972954e1140ad1891','u5d44e9d1b556910a39b774d4020e6dc6','u5791363d9891f95b4bd6ceacb22207d1','u7238d00856b10d6ca735f363a92feca3','u52afe1d4ea5332242efacfeb9190d2a3','ua10c2ad470b4b6e972954e1140ad1891','ue3dedea686b4bd3c946715c8684d50db','ucd5b65e2074195908e9459b9b1103b36','ubcf921fb4313eafa16dd8512270cbca1','u58b84c3a13fa7a5a55279cd77b3e03f6','u471d64ce29a82b8a0e5c0f4d5e1c6ef3','u17dd300568da75eef185af17397d175b','ub77514d16c832a36aa3c8ecea36326be','ub40c47e7bec584026f575f3b0cf8e44b','u8afb9f9c805ed5723947dce109e34df7','uc216d8664c4e1f43772c98b1b0b8956e','u67c43239c865dfce6addb41c6b3c0edd','uf8658b92e7d79f11083d5354d1ba547b','u11b00263de7ff1cef2481434685a7e7b','uff56d19ed9502fdf33b75cea3f7a9f63','u00aacc1d54fe9c1fabc5ba7242cd7013','u7679ba9bed776f6fecbb49e27f83c29d','u9b035730aeb9d17410d96e95ad2503b8','u560c06e2d7a280e2a6de821a7614f13c','u0f26401bbba4a99eff1412a1ac27b213','u33c2b73d7daa507d123d8c571ebe9eb3','ufba410943361a1fdc81693f6a9c977e8','u4858e902079f8ceee02533b19bb7ce4a','uac3106a6f3420a5b003e0c0e5b087bcf','u1b6ab4074456a542a10af64de05e2dbb']
creator =['u7c7a9c59c509ad89d0e4f9943389adba','ua10c2ad470b4b6e972954e1140ad1891','u5d44e9d1b556910a39b774d4020e6dc6','u5791363d9891f95b4bd6ceacb22207d1','u7238d00856b10d6ca735f363a92feca3','u52afe1d4ea5332242efacfeb9190d2a3','ua10c2ad470b4b6e972954e1140ad1891','ue3dedea686b4bd3c946715c8684d50db','ucd5b65e2074195908e9459b9b1103b36','ubcf921fb4313eafa16dd8512270cbca1','u58b84c3a13fa7a5a55279cd77b3e03f6','u471d64ce29a82b8a0e5c0f4d5e1c6ef3','u17dd300568da75eef185af17397d175b','ub77514d16c832a36aa3c8ecea36326be','ub40c47e7bec584026f575f3b0cf8e44b','u8afb9f9c805ed5723947dce109e34df7','uc216d8664c4e1f43772c98b1b0b8956e','u67c43239c865dfce6addb41c6b3c0edd','uf8658b92e7d79f11083d5354d1ba547b','u11b00263de7ff1cef2481434685a7e7b','uff56d19ed9502fdf33b75cea3f7a9f63','u00aacc1d54fe9c1fabc5ba7242cd7013','u7679ba9bed776f6fecbb49e27f83c29d','u9b035730aeb9d17410d96e95ad2503b8','u560c06e2d7a280e2a6de821a7614f13c','u0f26401bbba4a99eff1412a1ac27b213','u33c2b73d7daa507d123d8c571ebe9eb3','ufba410943361a1fdc81693f6a9c977e8','u4858e902079f8ceee02533b19bb7ce4a','uac3106a6f3420a5b003e0c0e5b087bcf','u1b6ab4074456a542a10af64de05e2dbb']
#if clMID not in owners:
#    python = sys.executable
#    os.execl(python, python, *sys.argv)
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "感謝您加入ㄩㄗ為好友！".format(str(contact.displayName)))
                cl.sendMessage(op.param1, "歡迎邀請我加群組喔!")
                cl.sendContact(op.param1, "u7c7a9c59c509ad89d0e4f9943389adba")
        if op.type == 1:
            print ("[1]更新配置文件")

        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            GS = group.creator.mid
            print ("[ 13 ] 通知邀請群組: " + str(group.name) + "\n邀請者: " + contact1.displayName + "\n被邀請者" + contact2.displayName)
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1, "歡迎邀請我加入群組")
                    if group.preventedJoinByTicket == True:
                        group.preventedJoinByTicket = False
                        cl.updateGroup(group)
                    else:
                        pass
                    ticket = cl.reissueGroupTicket(op.param1)
                    k1.acceptGroupInvitationByTicket(op.param1, ticket)
                    k2.acceptGroupInvitationByTicket(op.param1, ticket)
                    k3.acceptGroupInvitationByTicket(op.param1, ticket)
                    k4.acceptGroupInvitationByTicket(op.param1, ticket)
                    group.preventedJoinByTicket = True
                    cl.updateGroup(group)
# ----------------- 有人退出群組時1
        if op.type == 15:
            if settings["Lv"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                cl.sendMessage(op.param1, "我們的@wanping 同胞退出了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                cl.sendImageWithURL(op.param1,image)	
            except Exception as e:
                print(str(e))
# ----------------- 有人退出群組時2
        if op.type == 15:
            if settings["Lv"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                k1.sendMessage(op.param1, "我們的@wanping 同胞退出了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = k1.getContact(op.param2)
            except Exception as e:
                print(str(e))
# ----------------- 有人退出群組時3
        if op.type == 15:
            if settings["Lv"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                k2.sendMessage(op.param1, "我們的@wanping 同胞退出了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = k2.getContact(op.param2)
            except Exception as e:
                print(str(e))
# ----------------- 有人退出群組時4
        if op.type == 15:
            if settings["Lv"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                k3.sendMessage(op.param1, "我們的@wanping 同胞退出了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = k3.getContact(op.param2)
            except Exception as e:
                print(str(e))
# ----------------- 有人退出群組時5
        if op.type == 15:
            if settings["Lv"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                k4.sendMessage(op.param1, "我們的@wanping 同胞退出了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = k4.getContact(op.param2)
            except Exception as e:
                print(str(e))																
# ----------------- 有人加入群組時1				
        if op.type == 17:
            if settings["Wc"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)  		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                cl.sendMessage(op.param1, "歡迎 @wanping 同胞加入了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                cl.sendImageWithURL(op.param1,image)	
            except Exception as e:
                print(str(e))
# ----------------- 有人加入群組時2				
        if op.type == 17:
            if settings["Wc"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)  		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                k1.sendMessage(op.param1, "歡迎 @wanping 同胞加入了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = k1.getContact(op.param2)
            except Exception as e:
                print(str(e))
# ----------------- 有人加入群組時3				
        if op.type == 17:
            if settings["Wc"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)  		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                k2.sendMessage(op.param1, "歡迎 @wanping 同胞加入了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = k2.getContact(op.param2)
            except Exception as e:
                print(str(e))
# ----------------- 有人加入群組時4				
        if op.type == 17:
            if settings["Wc"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)  		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                k3.sendMessage(op.param1, "歡迎 @wanping 同胞加入了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = k3.getContact(op.param2)
            except Exception as e:
                print(str(e))
# ----------------- 有人加入群組時5				
        if op.type == 17:
            if settings["Wc"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)  		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                k4.sendMessage(op.param1, "歡迎 @wanping 同胞加入了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = k4.getContact(op.param2)
            except Exception as e:
                print(str(e))	
#==============================================================================#
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendContact(to,"u7c7a9c59c509ad89d0e4f9943389adba")
#==============================================================================#					
                elif text.lower() == '報數':
                    cl.sendMessage(msg.to,"➲ test 1")
                    k1.sendMessage(msg.to,"➲ test 2")
                    k2.sendMessage(msg.to,"➲ test 3")
                    k3.sendMessage(msg.to,"➲ test 4")
                    k4.sendMessage(msg.to,"➲ test 5")
                    cl.sendMessage(msg.to,"➲ 報數完成")
                elif text.lower() == '解散':						
                    k1.sendMessage(to,"下次再見 如果只是測試和玩此功能 記得邀我回來 愛你/妳歐♥")
                   # cl.leaveGroup(msg.to)
                    k1.leaveGroup(msg.to)
                    k2.leaveGroup(msg.to)
                    k3.leaveGroup(msg.to)
                    k4.leaveGroup(msg.to)      
                elif text.lower() == '集合':						
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    cl.sendMessage(to,"正在邀請 bot1、bot2、bot3、bot4中請稍後……")
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                    k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    cl.updateGroup(G)
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    cl.sendMessage(to, "正在檢查中….請您耐心稍等一會兒…")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")				

                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(to, "正在檢查中….請您耐心稍等一會兒…")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")								
					
                elif text.lower() == 'Speed':
                    start = time.time()
                    cl.sendMessage(to, "正在檢查中….請您耐心稍等一會兒…")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")								
				
                elif text.lower() == 'Sp':
                    start = time.time()
                    cl.sendMessage(to, "正在檢查中….請您耐心稍等一會兒…")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")								
				
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.sendMessage(to,"來回機票一張")
                                    cl.kickoutFromGroup(to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(to,[target])
                                except:
                                    cl.sendMessage(to,"掰掰瞜")
                                    pass

                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "总计{}提及".format(str(len(nama))))

                elif text.lower() == 'setread':
                    cl.sendMessage(msg.to, "已讀點設置成功")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                elif text.lower() == "cancelread":
                    cl.sendMessage(to, "已讀點已刪除")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["checkread","Checkread"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[已讀順序]%s\n\n[已讀的人]:\n%s\n查詢時間:[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "請輸入setread")


            if msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s " %("[文章傭有者]\n")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[文章預覽]\n(內容僅預覽100字)\n " + msg.contentMetadata["text"] + "\n[文章網址]\n " + msg.contentMetadata["postEndUrl"]
                            cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "\n[文章預覽]\n(內容僅預覽100字)\n " + msg.contentMetadata["text"]
                        ret_ += "\n[文章網址]\n " + msg.contentMetadata["postEndUrl"]
                        cl.sendMessage(msg.to, ret_)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in ban["mimic"]["target"] and ban["mimic"]["status"] == True and ban["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    sendMessageWithMention(to, contact.mid)
                                    cl.sendMessage(to, "為什麼要標記我呢?我正在忙線中，請私密我 謝謝您的體諒")
                                    cl.sendContact(op.param1, "u7c7a9c59c509ad89d0e4f9943389adba")
                                break
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                    elif msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        msg_dict[msg.id] = {"text":"貼圖id:"+str(stk_id),"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)

#==============================================================================#              
        if op.type == 65:
            if settings["reread"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                contact = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(contact.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, "收回訊息者 @wanping ", contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                contact = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 收回訊息 」\n"
                                ret_ += "• 收回訊息者 : {}".format(str(contact.displayName))
                                ret_ += "\n• 群組名稱 : {}".format(str(ginfo.name))
                                ret_ += "\n• 收回時間 : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• 訊息內容 : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus								
                                cl.sendImageWithURL(op.param1,image)	
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
#==============================================================================#
        if op.type == 65:
            if settings["reread"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = k1.getGroup(at)
                                contact = k1.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(contact.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                k1.sendMessage(at, "收回訊息者 @wanping ", contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                k1.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = k1.getGroup(at)
                                contact = k1.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 收回訊息 」\n"
                                ret_ += "• 收回訊息者 : {}".format(str(contact.displayName))
                                ret_ += "\n• 群組名稱 : {}".format(str(ginfo.name))
                                ret_ += "\n• 收回時間 : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• 訊息內容 : {}".format(str(msg_dict[msg_id]["text"]))
                                k1.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
#==============================================================================#
        if op.type == 65:
            if settings["reread"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = k2.getGroup(at)
                                contact = k2.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(contact.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                k2.sendMessage(at, "收回訊息者 @wanping ", contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                k2.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = k2.getGroup(at)
                                contact = k2.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 收回訊息 」\n"
                                ret_ += "• 收回訊息者 : {}".format(str(contact.displayName))
                                ret_ += "\n• 群組名稱 : {}".format(str(ginfo.name))
                                ret_ += "\n• 收回時間 : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• 訊息內容 : {}".format(str(msg_dict[msg_id]["text"]))
                                k2.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
#==============================================================================#              
        if op.type == 65:
            if settings["reread"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = k3.getGroup(at)
                                contact = k3.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(contact.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                k3.sendMessage(at, "收回訊息者 @wanping ", contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                k3.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = k3.getGroup(at)
                                contact = k3.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 收回訊息 」\n"
                                ret_ += "• 收回訊息者 : {}".format(str(contact.displayName))
                                ret_ += "\n• 群組名稱 : {}".format(str(ginfo.name))
                                ret_ += "\n• 收回時間 : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• 訊息內容 : {}".format(str(msg_dict[msg_id]["text"]))
                                k3.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
#==============================================================================#              
        if op.type == 65:
            if settings["reread"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = k4.getGroup(at)
                                contact = k4.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(contact.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                k4.sendMessage(at, "收回訊息者 @wanping ", contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                k4.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = k4.getGroup(at)
                                contact = k4.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 收回訊息 」\n"
                                ret_ += "• 收回訊息者 : {}".format(str(contact.displayName))
                                ret_ += "\n• 群組名稱 : {}".format(str(ginfo.name))
                                ret_ += "\n• 收回時間 : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• 訊息內容 : {}".format(str(msg_dict[msg_id]["text"]))
                                k4.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[※]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[※]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)

   					
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
