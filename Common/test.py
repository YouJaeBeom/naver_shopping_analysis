try:
    subprocess.check_call("curl --proxy socks5h://localhost:9050 http://ipinfo.io/ip",shell=True)
except Exception as e:
    print (str(e))