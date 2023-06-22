# """
#  ______   _______  _______  _        _______  _______  _______ 
# (  __  \ (  ____ \(  ____ \| \    /\(  ____ )(  ___  )(  ___  )
# | (  \  )| (    \/| (    \/|  \  / /| (    )|| (   ) || () () |
# | |   ) || (__    | (_____ |  (_/ / | (____)|| (___) || || || |
# | |   | ||  __)   (_____  )|   _ (  |     __)|  ___  || |(_)| |
# | |   ) || (            ) ||  ( \ \ | (\ (   | (   ) || |   | |===>("Ali")
# | (__/  )| (____/\/\____) ||  /  \ \| ) \ \__| )   ( || )   ( |
# (______/ (_______/\_______)|_/    \/|/   \__/|/     \||/     \|
# """         ___                  
# User --- > <(-_-)> Attcker --> :) 
# [+] Tool Spam Instgram Mwssages! 
import requests
import json
import random
from uuid import uuid4
from pyfiglet import Figlet
from colorama import Fore
f = Figlet(font='epic')  
print(Fore.GREEN + f.renderText('DeskRam'))
class InstagramSpammer:
    def __init__(self, username, password, target_user, message, num_messages):
        self.uuid = uuid4()
        self.rr = requests.session()
        self.username = username
        self.password = password
        self.target_username = target_user
        self.message = message
        self.num_messages = num_messages
        self.headers = {
            'User-Agent': 'Instagram 113.0.0.39.125 Android 7.1.1; 412dpi; 412x732; Xiaomi/google; MI 9T; angler; angler; en_US)',
            'Accept': "*/*",
            'Cookie': 'missing',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com'
        }
    
    def login(self):
        data_log = {
            'uuid': self.uuid,
            'password': self.password,
            'username': self.username,
            'device_id': self.uuid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'
        }

        log = self.rr.post('https://i.instagram.com/api/v1/accounts/login/', headers=self.headers, data=data_log, allow_redirects=True)
        if log.text.find("is_private") >= 0:
            print(f'[+] Logged in: @{self.username}')
            self.co = log.cookies
            self.coo = self.co.get_dict()
            self.csrf = self.coo["csrftoken"]
            self.ds_user_id = self.coo["ds_user_id"]
            self.mid = self.coo["mid"]
            self.sid = self.coo["sessionid"]
            self.headers.update({'Cookie': f'mid={self.mid}; sessionid={self.sid}; ds_user_id={self.ds_user_id}; csrftoken={self.csrf}'})
        elif "The username you entered doesn't appear to belong to an account" in log.text:
            print(Fore.RED + f"[-] Username is wrong : @{self.username}")
            exit()
        elif "The password you entered is incorrect. Please try again." in log.text:
            print(Fore.RED + f'[-] Password is wrong : @{self.username}')
            exit()
        elif "challenge_required" in log.text:
            print(Fore.RED + f'[-] Secure required : @{self.username}')
            exit()
        elif '"two_factor_required":true' in log.text:
            print(Fore.RED + f"[-] Two factor required : @{self.username}")
            exit()
        elif 'missing_parameters' in log.text:
            print(Fore.RED + "[-] Missing Parameters : Please Enter Parameters")
            exit()
        elif 'checkpoint_challenge_required' in log.text:
            print(log.text)
            print(Fore.RED + f"[-] Checkpoint Challenge Required : @{self.username}")
            exit()
        else:
            print(Fore.RED + "Some Error Happened, Try again !")
            print(log.text)
            print(log.json())
            exit()
    
    def send_messages(self):
        req_id = requests.get(f'https://i.instagram.com/api/v1/users/{self.target_user}/usernameinfo/', headers=self.headers)
        id = json.loads(req_id.text)["user"]["pk"]
        url_send = 'https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/'
        iddict =  679397915473+random.randint(0,100)
        done = 0
        error = 0
        
        for _ in range(self.num_messages):
            iddict += 5
            data_send = {
                'recipient_users': f'[[{id}]]',
                'action': 'send_item',
                'is_shh_mode': 0,
                'send_attribution': 'inbox_search',
                'client_context': f'{iddict}',
                'text': f'{self.message}',
                'device_id': f'{self.uuid}',
                'mutation_token': f'{iddict}',
                '_uuid': f'{self.uuid}',
                'offline_threading_id': f'{iddict}'
            }

            req = requests.post(url_send, data=data_send, headers=self.headers)
            
            if '"status":"ok"' in req.text:
                done += 1
                print(f'[{done}] Done Send Message To: @{self.target_user}')
            else:
                error += 1
                print(f'[{error}] Error Send Message')

user = input('[+] Username: ')
password = input('[+] Password: ')
target_user = input('[+] Target: ')
message = input('[+] Message: ')
num_messages = int(input('[+] How Many Messages? : '))

instagram_spammer = InstagramSpammer(user, password, target_user, message, num_messages)
instagram_spammer.login()
instagram_spammer.send_messages()