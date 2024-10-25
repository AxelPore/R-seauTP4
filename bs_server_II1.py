import socket
import sys
import argparse
import re
from psutil import net_if_addrs

def port_receive():
    port = 13337
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", action="store")
    port = parser.parse_args()
    if type(port) != int :
        TypeError("Need a valid port")
    elif 0 > port or 65535 < port :
        ValueError(f'ERROR -p argument invalide. Le port spécifié {port} est un port privilégié. Spécifiez un port au dessus de 1024.')
        sys.exit(1)
    elif 0 < port and 1024 > port :
        ValueError(f'ERROR -p argument invalide. Le port spécifié {port} est un port privilégié. Spécifiez un port au dessus de 1024.')
        sys.exit(2)
    else :
        return port 

def host_recieve():
    host = ""
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--listen", action="store")
    host = parser.parse_args()
    if not re.search(r'^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', host) :
        ValueError(f"ERROR -l argument invalide. L'adresse {host} n'est pas une adresse IP valide.")
        sys.exit(3)
    else :
        dic = net_if_addrs()
        addr = None
        compteur = 0
        for key, value in dic.items():
            for i in range(len(value)):
                addr = value[i].address                
                if addr == host :
                    compteur = 0
                    break
                else :
                    compteur += 1
                    
            if compteur != 0 :
                ValueError(f"ERROR -l argument invalide. L'adresse {host} n'est pas l'une des adresses IP de cette machine.")
                sys.exit(4)     
            else :
                return host
                    
def help():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", action="store_true")
    help = parser.parse_args()
    if help:
        print("Usage: python server.py [options]")
        print("Options:")
        print("-p, --port <port> : Port sur lequel écouter. Par défaut, 13337.")
        print("-l, --listen <adresse> : Adresse IP sur laquelle écouter. Par défaut, toutes les adresses IP disponibles.")
        print("-h, --help : Afficher cette aide.")
        sys.exit(0)
                     

def server(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))

    s.listen(1)

    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data : 
        sys.exit()
    print(f'Un client vient de se co et son IP c\'est {addr}')

    while True :
        
        try :
            
            data = conn.recv(1024)
            
            if not data : break
            message = data.decode()
            print(f"Données reçues du client : {message}")
            if "meo" in message :
                conn.sendall("Meo à toi confrère.".encode('utf-8'))
            elif "waf" in message :
                conn.sendall(b"ptdr t ki")
            else :
                conn.sendall(b"Mes respects humble humain.")
            
            
        
        except socket.error:
            
            print("Error Occured.")
            break

def main() :
    help()
    port = port_receive()
    host = host_recieve()
    server(host, port)