# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 02:23:30 2020

@Author: Aporlorxl23
"""
import requests, json, base64
from bs4 import BeautifulSoup

Url = "https://www.hackthebox.eu/api/invite/generate"
Agent = {"User-Agent":"Aporlorxl23 HackTheBox Invite Code Script"}
R = requests.post(Url,headers=Agent)
Data = R.json()
Code = list(Data["data"]["code"].split())[0]
Code = base64.b64decode(Code.encode())
print("[+] Invite Code>> " + Code.decode())
