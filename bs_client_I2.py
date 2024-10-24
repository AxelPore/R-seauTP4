import socket
import sys 

host = "10.1.2.17"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

try :
    s.sendall(b"Hello there")
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
except :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

message = input('Que veux-tu envoyer au serveur : ')

s.sendall(message.encode('utf-8'))

data = s.recv(1024)

print(f"Le serveur a répondu {repr(data.decode())}")

s.close()

sys.exit()