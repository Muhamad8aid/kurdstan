# kurdstan
import marshal
import sys
import os
import time
import base64
import uuid
import requests
import webbrowser
os.system('clear')
A="\033[1;31m"
bA="\033[1;32m"
cA="\033[1;33m"
dA="\033[1;34m"
eA="\033[1;35m"
fA="\033[1;36m"
oo=True
while oo==True:
	user=input(f" {fA}[{cA}?{fA}] User Name : {cA}")
	if user=="M416":
		print(f'\n {eA}[{cA}✓{eA}]{bA} Username Rasta ... \n')
		pas=input(f' {fA}[{cA}?{fA}]  password :  {cA}')
		if pas =="M416":
			print(f' \n{eA} [{cA}✓{eA}]{bA} Password Rasta ...')
			oo=False
		else:
			print(f"\n {dA}[✗]{A} Password Hlaya : \n")
			webbrowser.open('https://t.me/MuHaMaD3D')
	else:
		print(f'\n {dA}[✗{dA}] {A}UserName Hlaya :\n')
		webbrowser.open('https://t.me/MuHaMaD3D')
webbrowser.open('https://t.me/MuHaMaD3D')
print(f'\n\n  {fA}[{A}➢{fA}] {bA}join Mychanal  \n\n ')
time.sleep(2)
print(f'\n {A}[{eA}#{A}]{bA} Chuna Zhwrawa Sarkautwtoo Boo .......\n\n')
time.sleep(3)
os.system('clear')
def enc():
    print("&"*24,f"{fA}</>Make By MuHaMaD<\>",f"{bA}&"*24)
    print(f"""[T.B]//✹MARJA AWTOLAY ENCRYPT DAKAY LAHECH FOLDARY NABET✹\n
{A}[{fA}~{A}]{cA} Encrypt By Marshal ➢ [1] 
\n
{A}[{fA}~{A}]{cA} Encrypt By base85  ➢ [2]
\n
{A}[{fA}~{A}]{cA} Encrypt By base64  ➢ [3]
\n
{A}[{fA}~{A}]{cA} Encrypt By base 32 ➢ [4]
\n
{A}[{fA}~{A}]{cA} Encrypt By base 16 ➢ [5]
""")
    print(f"{fA}∞"*35)
    print(f" \n{fA}Make TooL By CHANAL TELEGRAM¦{bA}>>https://t.me/MuHaMaD3D \n\n{fA}Join My GROOP TELEGRAM¦{bA}>>https://t.me/MuHaMa4D\n\n")
    print(f"{bA}&"*24,f"{fA}</>Make By MuHaMaD<\>",f"{bA}&"*24)
    EN=input(f"\n{dA}[{bA}?{dA}]{cA} choice  :  {eA}")
    t=time.strftime(" Hours>>%l : Mint >>%M :  Secont>> %S")
    G=time.strftime(" Day>>%d : Munth>> %m : Yars>> %Y")
    if EN =="1":
    	BN= input(f"\n  {bA}Name File :  ")
    	file=open("/sdcard/"+(BN)).read()
    	B=compile(file,"<file>","exec")
    	B1=marshal.dumps(B)
    	V=f"#CHANAL TELEGRAM>>https://t.me/MuHaMaD3D\n#GROOP TELEGRAM>>https://t.me/MuHaMa4D\n#Encrypt To Marshal Name File>> [{BN}]\n#Make By >>MuHaMaD \n#at>>{G}{t}\nimport marshal\nexec(marshal.loads({B1}))"
    	F=open(f"/sdcard/enc marshal[{BN} ","w")
    	print(F.write(V))
    	print(f"\n Tawaw....Ecrypt Boo.._LA FILE BA NAWY encmarshal[{BN}")
    	input('\n\n  Back ... ')
    	os.system('clear')
    	return enc()
    if '2' in EN:
    	Fg=input(f"   \n{bA}Name File  : ")
    	fg1=open("/sdcard/"+(Fg)).read()
    	fg2=base64.b85encode(fg1.encode("utf-8"))
    	FL=open(f'/sdcard/encb85[{Fg}',"w")
    	FLi=f"#CHANAL TELEGRAM>>https://t.me/MuHaMaD3D\n#GROOP TELEGRAM>>https://t.me/MuHaMa4D\n#decode >>(utf-8)\n#Encrypt Name File>>{Fg}\n#Encrypt  Base85 By>>MuHaMaD\n#at={G}{t}\n#MeKa BY >>MuHaMaD\nimport base64\nexec(base64.b85decode({fg2}))"
    	print(FL.write(f"{FLi}"))
    	print("\n Tawaw....Ecrypt Boo..__LA FILE BA NAWY encb85[{BN}")
    	input('\n\n  Back .. ')
    	os.system('clear')
    	return enc()
    if EN=="3":
    	f1=input(f"\n  {bA}Name File :  ")
    	f12=open("/sdcard/"+(f1)).read()
    	f13=base64.b64encode(f12.encode("utf-8"))
    	f14=open(f"/sdcard/encb64 [{f1}","w")
    	f15=f"#CHANAL TELEGRAM>>https://t.me/MuHaMaD3D\n#GROOP TELEGRAM>>https://t.me/MuHaMa4D\n#decode >>(utf-8)\n#Encrypt Name File >> {f1}\n#Encrypt Base64 By>> MuHaMaD\n#at={G}{t}\n#Meka By>>MuHaMaD>\nimport base64\nexec(base64.b64decode({f13}))"
    	print(f14.write(f"{f15}"))
    	print("\n Tawaw....Ecrypt Boo..__LA FILE BA NAWY encb64[{BN}")
    	input('\n\n  Back .. ')
    	os.system('clear')
    	return enc()
    if EN=="4":
    	f1=input(f"\n  {bA}Name File :  ")
    	f12=open("/sdcard/"+(f1)).read()
    	f13=base64.b32encode(f12.encode("utf-8"))
    	f14=open(f"/sdcard/encb32 [{f1}","w")
    	f15=f"#CHANAL TELEGRAM>>https://t.me/MuHaMaD3D\n#GROOP TELEGRAM>>https://t.me/MuHaMa4D\n#decode >>(utf-8)\n#Encrypt Name File>> {f1}\n#Encrypt Base64 By>> MuHaMaD\n#at ={G}{t}\n#Meka By>>MuHaMaD\nimport base64\nexec(base64.b32decode({f13}))"
    	print(f14.write(f"{f15}"))
    	print("\n Tawaw....Ecrypt Boo.._LA FILE BA NAWY encb32[{NA}")
    	input('\n\n  Back .. ')
    	os.system('clear')
    	return enc()
    if EN=="5":
    	f1=input(f"\n  {bA}Name File :  ")
    	f12=open("/sdcard/"+(f1)).read()
    	f13=base64.b16encode(f12.encode("utf-8"))
    	f14=open(f"/sdcard/encb16 [{f1}","w")
    	f15=f"#CHANAL TELEGRAM>>https://t.me/MuHaMaD3D\n#GROOP TELEGRAM>>https://t.me/MuHaMa4D\n#decode >>(utf-8)\n#Encrypt Name File >> {f1}\n#Encrypt Base64 By>> MuHaMaD\n#at ={G}{t}\n#Meka By>>MuHaMaD\nimport base64\nexec(base64.b16decode({f13}))"
    	print(f14.write(f"{f15}"))
    	print("\n Tawaw....Ecrypt Boo..__LA FILE BA NAWY encb16[{NA}")
    	input('\n\n  Back .. ')
    	os.system('clear')
    	return enc()
os.system("clear")
enc()
