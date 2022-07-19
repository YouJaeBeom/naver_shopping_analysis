from stem.control import Controller
from stem import Signal

def renew_tor_ip(port_num):
    with Controller.from_port(port = port_num) as controller:
        controller.authenticate(password="mnet")
        controller.signal(Signal.NEWNYM)