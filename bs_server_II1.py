import socket
import sys
import argparse

host = "10.1.2.17"
port = 13337

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
