#!/usr/bin/env python3
import requests, json, time, re, os

# Warna
KUNING = ('\x1b[1;93m')
MERAH = ('\x1b[1;91m')
HIJAU = ('\x1b[1;92m')
PUTIH = ('\x1b[1;97m')
BIRU = ('\x1b[36;1m')
COKLAT = ('\x1b[33;1m')
BLU = ('\x1b[0;36m')

# Banner
banner = (f"""                    {MERAH}({PUTIH}★ SELAMAT DATANG ★{MERAH}){PUTIH}
{BLU}◢████◣░█████◣
{BLU} ██░░░░░██░░█◤
{BLU} ████◤░░█████◣  
{BLU} ██░░░░░██░░██ 
{BLU} █◤░░░░░█████◤
{COKLAT} **********************************************************
{PUTIH}                Author : Baz Hengker Tzy                                                 
{PUTIH}                Github : https://github.com/Basari-ID              
{COKLAT} **********************************************************
""")
# Convert Cookie Ke Token
class convert:

  def __init__(self):
    os.system('clear')
    print(f"""{banner}
{HIJAU}»1«{PUTIH} Mendapatkan Token EAAI {HIJAU}({HIJAU}on{HIJAU}){HIJAU}
{HIJAU}»2«{PUTIH} Mendapatkan Token EAAB {HIJAU}({HIJAU}on{HIJAU}){HIJAU}
{HIJAU}»3«{PUTIH} Mendapatkan Informasii {HIJAU}({HIJAU}on{HIJAU}){HIJAU}
{HIJAU}»4«{PUTIH} Hack Facebook {HIJAU}({MERAH}of{HIJAU}){MERAH}
{HIJAU}»5«{PUTIH} Keluar {HIJAU}({MERAH}out{HIJAU}){MERAH}
   """)
    masuk = input(f"{KUNING}.+.{PUTIH} Pilih :{HIJAU} ")
    if masuk == '1' or masuk == '01':
      cookie = input(f"\n{HIJAU}.+.{PUTIH} Masukkan Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__satu__(cookie)
      else:
        exit(f"{MERAH}.-.{MERAH} Cookie Tidak Valid")
    elif masuk == '2' or masuk == '02':
      cookie = input(f"\n{HIJAU}.+.{PUTIH} Masukkan Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__dua__(cookie)
      else:
        exit(f"{MERAH}.-.{MERAH} Cookie Tidak Valid")
    elif masuk == '3' or masuk == '03':
      print(f"{KUNING}.+.{PUTIH} Anda akan diarahkan ke facebook...");time.sleep(3);os.system('xdg-open https://www.facebook.com/basari.shp');exit()
    elif masuk == '4' or masuk == '04':
      exit()
    else:
      exit(f"{MERAH}-{MERAH}ERROR NOT FOUND-")
  def __satu__(self,cookie):
    try:
      with requests.Session() as r:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': cookie
        }
        response = r.get('https://web.facebook.com/ads/manager/account_settings/account_billing/?_rdc=1&_rdr', headers = headers)
        find = re.findall('(EAAI\w+)', response.text)
        if len(find) == 0:
          exit(f"{MERAH}.-.{MERAH} Token tidak ditemukan")
        else:
          for token in find:
            print(f"\n{KUNING} {PUTIH}[Berhasil Mendapatkan Token]> :{HIJAU} {token}")
    except Exception as e:
      exit(f"{MERAH}.-{MERAH} {e}")
  def __dua__(self,cookie):
    try:
      with requests.Session() as r:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': cookie
        }
        respon = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
        find = re.findall('act=(.*?)&nav_source', respon.text)
        if len(find) == 0:
          exit(f"{MERAH}eror.{MERAH} Token tidak ditemukan")
        else:
          for y in find:
            response = r.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={y}&nav_source=no_referrer', headers = headers)
            token = re.search('(EAAB\w+)', response.text).group(1)
            print(f"\n{KUNING} {PUTIH} [Berhasil Mendapatkan Token]> :{HIJAU} {token}")
    except Exception as e:
      exit(f"{MERAH}!.{MERAH} {e}")
      

if __name__=='__main__':
  os.system('git pull');convert()