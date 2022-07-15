from bs4 import BeautifulSoup
import requests
import json
import socket
import socks
import subprocess
from stem.control import Controller
from stem import Signal
import urllib3
import orjson

def renew_tor_ip(port_num):
    with Controller.from_port(port = port_num) as controller:
        controller.authenticate(password="mnet")
        controller.signal(Signal.NEWNYM)

if __name__ == "__main__":
    """# Configuration
    SOCKS5_PROXY_HOST = 'localhost'
    SOCKS5_PROXY_PORT = 9050

    # Remove this if you don't plan to "deactivate" the proxy later
    default_socket = socket.socket

    # Set up a proxy
    socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
    socket.socket = socks.socksocket"""

    ## setting tor
    proxies = {
        'http': 'socks5://localhost:9050',
        'https': 'socks5://localhost:9050',
    }
    renew_tor_ip(9051)
    """socks.set_default_proxy(socks.SOCKS5, "localhost",port=9050)
    socket.socket = socks.socksocket"""
    http = urllib3.PoolManager()
    # Sending a GET request and getting back response as HTTPResponse object.
    print(http.request("GET", "http://httpbin.org/ip").headers)


    # - If you use urllib2:
    import urllib3
    http = urllib3.PoolManager()
    print(http.request("GET",'http://icanhazip.com/', timeout=24).headers) # outputs proxy IP

    # - If you use requests (pip install requests):
    import requests
    print(requests.get('http://icanhazip.com/', timeout=24, proxies = proxies).headers) # outputs proxy IP

    # Use this only if you plan to make requests without any proxies later
    #socket.socket = default_socket

    # Make a request normally without a proxy; this will output your own public IP
    print(http.request("GET",'http://icanhazip.com/', timeout=24).headers)