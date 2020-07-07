'''Class to connect to NordVPN'''
import subprocess
from models.vpn_base import VPNConnection

class ConnectNordVPN(VPNConnection):

    def __init__(self):
        pass

    def connect_to_vpn():

        subprocess.call("nordvpn connect", shell=True)

    def disconnect_to_vpn():

        subprocess.call("nordvpn disconnect", shell=True)