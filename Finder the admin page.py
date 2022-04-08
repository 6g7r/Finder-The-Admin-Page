import time,ctypes
from  threading import  Thread
import requests,os
from colorama import *
clear2 = lambda: os.system('cls')
clear2()
print(Fore.LIGHTRED_EX,f"""


           ▄▀▀▀█▄    ▄▀▀█▄   ▄▀▀▄▀▀▀▄ 
          █  ▄▀  ▀▄ ▐ ▄▀ ▀▄ █   █   █ 
          ▐ █▄▄▄▄     █▄▄▄█ ▐  █▀▀▀▀  
           █    ▐    ▄▀   █    █      
           █        █   ▄▀   ▄▀       
          █         ▐   ▐   █         {Fore.RESET}[{Fore.LIGHTGREEN_EX}?{Fore.RESET}] By 6G7R
                                      {Fore.RESET}[{Fore.LIGHTGREEN_EX}?{Fore.RESET}] PW Team > https://discord.gg/pw1
                                      {Fore.RESET}[{Fore.LIGHTGREEN_EX}?{Fore.RESET}] Finder the admin page
            
                          {Fore.RESET}[{Fore.LIGHTGREEN_EX}1{Fore.RESET}] |PHP|     {Fore.RESET}[{Fore.LIGHTGREEN_EX}4{Fore.RESET}] |JS |
                          {Fore.RESET}[{Fore.LIGHTGREEN_EX}2{Fore.RESET}] |ASP|     {Fore.RESET}[{Fore.LIGHTGREEN_EX}5{Fore.RESET}] |CGI|         
                          {Fore.RESET}[{Fore.LIGHTGREEN_EX}3{Fore.RESET}] |CFM|     {Fore.RESET}[{Fore.LIGHTGREEN_EX}6{Fore.RESET}] |BRF|
                            


""")
class start:
    def __init__(self):
        self.b=0
        self.g=0
        self.Ch=0
        self.r = requests.Session()
        try:
           self.asp= open('search/Asp.txt').read().splitlines()
        except:
            print('Asp.txt Not Found  !')
            input('Enter For Exit')
        try:
            self.brf=open('search/BRf.txt').read().splitlines()
        except:
            print('BRf.txt Not Found  !')
            input('Enter For Exit')
        try:
            self.cfm=open('search/Cfm.txt').read().splitlines()
        except:
            print('Cfm.txt Not Found  !')
            input('Enter For Exit')
        try:
            self.cgi=open('search/CGi.txt').read().splitlines()
        except:
            print('CGi.txt Not Found  !')
            input('Enter For Exit')

        try:
            self.js=open('search/Js.txt').read().splitlines()
        except:
            print('Js.txt Not Found  !')
            input('Enter For Exit')
        try:
            self.php=open('search/Php.txt').read().splitlines()
        except:
            print('Php.txt Not Found  !')
            input('Enter For Exit')
        self.wep = input(f'{Fore.RESET}[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Enter Name Wep Like This  https://google.com  : ')
        self.i=input(f'{Fore.RESET}[{Fore.LIGHTGREEN_EX}+{Fore.RESET}]  >>> 1/6 : ')
        if '1' in self.i:
            self.php1()
        if '4' in self.i:
            self.js1()
        if '5' in self.i:
            self.cgi1()
        if '3' in self.i:
            self.cfm1()
        if '2' in self.i:
            self.asp1()
        if '6' in self.i:
            self.brf1()
    def php1(self):
        for self.php11 in self.php:
            ctypes.windll.kernel32.SetConsoleTitleW(str('By  6G7R | [?] MY INSTA > 6G7R <  |   Checking >>>  {}   |  '.format(self.php11)))

            print(f'''\rGood admin page[{Fore.RESET}{Fore.GREEN}{self.g}{Fore.RESET}] Bad [{Fore.RESET}{Fore.RED}{self.b}{Fore.RESET}]-[ 302 ] [!] Possible admin page  [{self.Ch}]''',end="")
            self.sendphp=self.r.get(f'{self.wep}/{self.php11}')
            if self.sendphp.status_code == 200:
                print(f'{Fore.LIGHTRED_EX}[!] Have been reached > {self.wep}/{self.php11} \n \n')
                with open(f"Fucked {self.wep}.txt", "a") as mix:
                    mix.write(f"Admin page > {self.wep}/{self.php11}\n")
                    mix.close()
                input()
                os._exit(0)
            if self.sendphp.status_code == 404:
                self.b +=1
            if self.sendphp.status_code == 302:
                self.Ch +=1
                with open(f"status_code 302  {self.wep}.txt", "a") as mix:
                    mix.write(f" Possible admin page > {self.wep}/{self.php1}\n")
    def js1(self):
        for self.js11 in self.js:
            ctypes.windll.kernel32.SetConsoleTitleW(str('By  6G7R | [?] MY INSTA > 6G7R <  |   Checking >>>  {}   |  '.format(self.js11)))
            print(f'''\rGood admin page[{Fore.RESET}{Fore.GREEN}{self.g}{Fore.RESET}] Bad [{Fore.RESET}{Fore.RED}{self.b}{Fore.RESET}]-[ 302 ][!]Possible admin page [{self.Ch}]''',end="")
            self.sendphp=self.r.get(f'{self.wep}/{self.js11}')
            if self.sendphp.status_code == 200:
                print(f'{Fore.LIGHTRED_EX}[!] Have been reached > {self.wep}/{self.js11} \n \n')
                with open(f"Fucked {self.wep}.txt", "a") as mix:
                    mix.write(f"Admin page > {self.wep}/{self.js11}\n")
                    mix.close()
                input()
                os._exit(0)
            if self.sendphp.status_code == 404:
                self.b +=1
            if self.sendphp.status_code == 302:
                self.Ch +=1
                with open(f"status_code 302  {self.wep}.txt", "a") as mix:
                    mix.write(f" Possible admin page > {self.wep}/{self.js11}\n")
    def cgi1(self):
        for self.cgi11 in self.cgi:
            ctypes.windll.kernel32.SetConsoleTitleW(str('By  6G7R | [?] MY INSTA > 6G7R <  |   Checking >>>  {}   |  '.format(self.cgi11)))
            print(f'''\rGood admin page [{Fore.RESET}{Fore.GREEN}{self.g}{Fore.RESET}] Bad  [{Fore.RESET}{Fore.RED}{self.b}{Fore.RESET}]-[ 302 ][!] Possible admin page [{self.Ch}]''',end="")
            self.sendphp=self.r.get(f'{self.wep}/{self.cgi11}')
            if self.sendphp.status_code == 200:
                print(f'{Fore.LIGHTRED_EX}[!] Have been reached > {self.wep}/{self.cgi11} \n \n')
                with open(f"Fucked {self.wep}.txt", "a") as mix:
                    mix.write(f"Admin page > {self.wep}/{self.cgi11}\n")
                    mix.close()
                input()
                os._exit(0)
            if self.sendphp.status_code == 404:
                self.b +=1
            if self.sendphp.status_code == 302:
                self.Ch +=1
                with open(f"status_code 302  {self.wep}.txt", "a") as mix:
                    mix.write(f" Possible admin page > {self.wep}/{self.cgi11}\n")
    def cfm1(self):
        for self.cfm11 in self.cfm:
            ctypes.windll.kernel32.SetConsoleTitleW(str('By  6G7R | [?] MY INSTA > 6G7R <  |   Checking >>>  {}   |  '.format(self.cfm11)))
            print(f'''\rGood admin page[{Fore.RESET}{Fore.GREEN} {self.g}{Fore.RESET} ] Bad[ {Fore.RESET} {Fore.RED} {self.b} {Fore.RESET}]-[ 302 ] [!] Possible admin page [{self.Ch}]''',end="")
            self.sendphp=self.r.get(f'{self.wep}/{self.cfm11}')
            if self.sendphp.status_code == 200:
                print(f'{Fore.LIGHTRED_EX}[!] Have been reached > {self.wep}/{self.cfm11} \n \n')
                with open(f"Fucked {self.wep}.txt", "a") as mix:
                    mix.write(f"Admin page > {self.wep}/{self.cfm11}\n")
                    mix.close()
                input()
                os._exit(0)
            if self.sendphp.status_code == 404:
                self.b +=1
            if self.sendphp.status_code == 302:
                self.Ch +=1
                with open(f"status_code 302  {self.wep}.txt", "a") as mix:
                    mix.write(f" Possible admin page > {self.wep}/{self.cfm11}\n")
    def brf1(self):
        for self.brf11 in self.brf:
            ctypes.windll.kernel32.SetConsoleTitleW(str('By  6G7R | [?] MY INSTA > 6G7R <  |   Checking >>>  {}   |  '.format(self.brf11)))

            print(f'''\rGood admin page[{Fore.RESET}{Fore.GREEN}{self.g}{Fore.RESET}] Bad [{Fore.RESET}{Fore.RED}{self.b}{Fore.RESET}]-[ 302 ] [!] Possible admin page [{self.Ch}]''',end="")
            self.sendphp=self.r.get(f'{self.wep}/{self.brf11}')
            if self.sendphp.status_code == 200:
                print(f'{Fore.LIGHTRED_EX}[!] Have been reached > {self.wep}/{self.brf11} \n \n')
                with open(f"Fucked {self.wep}.txt", "a") as mix:
                    mix.write(f"Admin page > {self.wep}/{self.brf11}\n")
                    mix.close()
                input()
                os._exit(0)
            if self.sendphp.status_code == 404:
                self.b +=1
            if self.sendphp.status_code == 302:
                self.Ch +=1
                with open(f"status_code 302  {self.wep}.txt", "a") as mix:
                    mix.write(f" Possible admin page > {self.wep}/{self.brf11}\n")
    def asp1(self):
        for self.asp11 in self.asp:
            ctypes.windll.kernel32.SetConsoleTitleW(str('By  6G7R | [?] MY INSTA > 6G7R <  |   Checking >>>  {}   |  '.format(self.asp11)))
            print(f'''\rGood the admin page [{Fore.RESET}{Fore.GREEN}{self.g}{Fore.RESET}] Bad[{Fore.RESET}{Fore.RED}{self.b}{Fore.RESET}]-[ 302 ] [!] Possible admin page [ {self.Ch} ] ''',end="")
            self.sendphp=self.r.get(f'{self.wep}/{self.asp11}')
            if self.sendphp.status_code == 200:
                print(f'{Fore.LIGHTRED_EX}[!] Have been reached > {self.wep}/{self.asp11} \n \n')
                with open(f"Fucked {self.wep}.txt", "a") as mix:
                    mix.write(f"Admin page > {self.wep}/{self.asp11}\n")
                    mix.close()
                input()
                os._exit(0)
            if self.sendphp.status_code == 404:
                self.b +=1
            if self.sendphp.status_code == 302:
                self.Ch +=1
                with open(f"status_code 302  {self.wep}.txt", "a") as mix:
                    mix.write(f" Possible admin page > {self.wep}/{self.asp11}\n")


if __name__ == '__main__':
    Thread(target=start).start()
