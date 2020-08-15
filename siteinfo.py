#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import os
import time as t
os.system("apt-get install upgrade && update")
os.system("apt-get update")
os.system("git clone https://github.com/outysles/websiteidentificationgereksinimler.git")
os.system("apt-get install python-pip")
os.system("apt-get install python3")
os.system("apt-get install figlet")
os.system("apt-get install toilet")
os.system("clear")
os.system("toilet -f eftitalic -F crop  WEBSITE  ")
os.system("toilet -f eftitalic -F crop  IDENTIFICATION ")

print("""

|----------------------------------------------|
|      KR!PTON WEBSITE TANIMLAMA ARACI         |
|               KR!PTON V1.0.1                 |
|----------------------------------------------|

""")
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
print(random.choice(colors))
print("""

 ---------------------------------------------------------------------
 1)Basit Website Tanımlama
 2)Agresif ve Detaylı Tanımlama
 ---------------------------------------------------------------------
 
 """)
print(random.choice(colors))
secim1 = raw_input("Seçim Yapınız== ")

if(secim1=="1"):
	hedef = raw_input("Hedef Siteyi Giriniz== ")
	print(random.choice(colors))
	print("TARAMA BASLATILDI.")
	print("ANALIZ SONUCLARI BELLİ OLDU.")
	print("ISTATIKLER CIKARILIYOR.")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	os.system(('whatweb' + ' ' + hedef + ' ' + '  '))

elif(secim1=="2"):
	hedef = raw_input("Hedef Siteyi Giriniz== ")
	level = raw_input("Agresiflik Seviyesi Belirleyiniz. \033[1;31m[1-5]== ")
	print(random.choice(colors))
	print("TARAMA BASLATILDI.")
	print("ANALIZ SONUCLARI BELLI OLDU.")
	print("AGRESIF MOD AKTIF EDILDI.")
	print("ISTATIKLER CIKARILIYOR.")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	print("...")
	os.system(('whatweb -v -a' + level +' ' + ' ' + hedef))


else:
	print(random.choice(colors))
	print("GEÇERSİZ KOMUT GİRDİNİZ...")






	
