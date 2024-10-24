# Commande serveur
```
[ak17@vbox ~]$ sudo nano /etc/sysconfig/network-scripts/ifcfg-enp0s8
[ak17@vbox ~]$ sudo systemctl restart NetworkManager
[ak17@vbox ~]$ sudo firewall-cmd --add-port=13337/tcp --permanent
[ak17@vbox ~]$ sudo firewall-cmd --reload
[ak17@vbox R-seauTP4]$ python bs_server_I1.py
[ak17@vbox R-seauTP4]$ ss -lnpt | grep 13337
LISTEN 0      1          10.1.2.17:13337      0.0.0.0:*    users:(("python",pid=1502,fd=3))
[ak17@vbox R-seauTP4]$ Données reçues du client : b'Meooooo !'
```


# Commande client
```
[ak17@vbox ~]$ sudo nano /etc/sysconfig/network-scripts/ifcfg-enp0s8
[ak17@vbox ~]$ sudo systemctl restart NetworkManager
[ak17@vbox ~]$ sudo firewall-cmd --add-port=13337/tcp --permanent
[ak17@vbox ~]$ sudo firewall-cmd --reload
[azu@vbox R-seauTP4]$ python bs_client_I1.py
Le serveur a répondu b'Hi mate !'
```