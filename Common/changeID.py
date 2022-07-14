import requests
import random
import json
import subprocess
from stem.control import Controller
from stem import Signal

def get_current_ip(port_num):
    try:
        subprocess.check_call("curl --proxy socks5h://localhost:9050 http://ipinfo.io/ip",shell=True)
    except Exception as e:
        print (str(e))
def renew_tor_ip(port_num):
    with Controller.from_port(port = port_num) as controller:
        controller.authenticate(password="mnet")
        controller.signal(Signal.NEWNYM)

if __name__ == "__main__":
    port = 9051
    renew_tor_ip(port)
    get_current_ip(port)