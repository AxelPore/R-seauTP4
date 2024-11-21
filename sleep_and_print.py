import time

def compteur() :
    for i in range(11):
        print(i)
        time.sleep(0.5)

def main():
    tasks = [ compteur(), compteur() ]
    time.gather(*tasks)

main()
