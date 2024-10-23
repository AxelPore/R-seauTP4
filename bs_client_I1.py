import socket
import sys 

host = "10.0.2.15"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.sendall("Meooooo !")

data = s.recv(1024)

print(f"Le serveur a répondu {repr(data)}")

s.close()

sys.exit()