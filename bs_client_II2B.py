import socket
import sys 
import re
import logging

logger = logging.getLogger("logs")
logger.setLevel(10)
fmt = "%(asctime)s %(levelname)8s %(message)s"
class CustomFormatter(logging.Formatter):

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'
    white = '\x1b[38;5;255m'


    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.fmt,
            logging.INFO: self.fmt,
            logging.WARNING: self.fmt,
            logging.ERROR: self.fmt,
            logging.CRITICAL: self.fmt,
            
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)
    
console_handler = logging.StreamHandler()
console_handler.setLevel(10)
console_handler.setFormatter(CustomFormatter(fmt))

file_handler = logging.FileHandler("/var/log/bs_server/bs_server.log", mode="a", encoding="utf-8")
file_handler.setLevel(10)
file_handler.setFormatter(logging.Formatter(fmt))

logger.addHandler(console_handler)
logger.addHandler(file_handler)


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
if type(message) != str :
    raise TypeError
elif not re.search(r'[a-z,A-Z,0-9,\s]*(meo)[a-z,A-Z,0-9,\s]*|[a-z,A-Z,0-9,\s]*(waf)[a-z,A-Z,0-9,\s]*', message):
    raise ValueError("Data not sent, can only send 'meo' or 'waf'. Piece of shit of human !")
s.sendall(message.encode('utf-8'))

data = s.recv(1024)

response = data.decode()

print(f"Le serveur a répondu {repr(response)}")

s.close()

sys.exit()