%%writefile agent/network.py

import socket
import platform
import subprocess


class NetworkTools:

    @staticmethod
    def ping(host="8.8.8.8"):
        try:
            result = subprocess.check_output(
                ["ping", "-c", "2", host],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            return {"status": "reachable", "details": result}
        except Exception as e:
            return {"status": "unreachable", "error": str(e)}

    @staticmethod
    def get_hostname():
        return socket.gethostname()

    @staticmethod
    def get_os():
        return platform.platform()

    @staticmethod
    def ip_config():
        try:
            result = subprocess.check_output(
                ["ip", "addr"],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            return result
        except:
            return "Command not supported on this system."

    @staticmethod
    def dns_lookup(domain):
        try:
            result = subprocess.check_output(
                ["nslookup", domain],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            return result
        except:
            return "DNS lookup failed"
