import requests
from socks import setdefaultproxy
import socket
import socks, time


class Endereco:
    def __init__(self, url):
        self.url = ""
        self.set_endereco(url)

    def set_endereco(self, end):
        if not isinstance(end, str):
            raise ValueError("apenas literais {}".format(end))
        self.url = end

    def get_endereco(self):
        return self.url



class Anonymous:
    verificar = Endereco("http://www.ifconfig.me/ip")
    ip = verificar.get_endereco()

    try:
        print("Ip Real =  ", requests.get(ip).text)
        for i in range(0, 3):
            setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "localhost", 9050)# <====: porta tor...
            socket.socket = socks.socksocket
            rede_tor = requests.get(ip).text
            print("Rede TOR = ", rede_tor)
            time.sleep(600)
    except Exception:
        print("Sem conexao com a rede tor")



"""
iniciar tor:
/etc/init.d/tor start

ou

service tor start

Serviço on:
/etc/init.d/tor status

ou

service tor status



..............................................................................................................
jfc-me@jfc:~$ netstat -a 
Conexões Internet Ativas (servidores e estabelecidas)
Proto Recv-Q Send-Q Endereço Local          Endereço Remoto         Estado    
tcp        0      0 localhost:8118          *:*                     OUÇA      ====:> privoxy
tcp        0      0 localhost:9050          *:*                     OUÇA      =====:> tor
..............................................................................................................

"""

