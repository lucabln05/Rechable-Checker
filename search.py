import os 
#multiprocessing damit domains gleichzeitig abgefragt werden können
from concurrent.futures import ThreadPoolExecutor


def delete():
    try:
        open('reachable.txt', 'w').close()
        open('unreachable.txt', 'w').close()
    except Exception as err:
        print(err)


def search():
    # liest die Datei aus in der die Hostname stehen
    f = open('list.txt', 'r')
    # wie viele Domains gleichzeitig abgefragt werden sollen
    max_workers = 10
    # startet den Thread Pool
    with ThreadPoolExecutor(max_workers) as executor:
        # list jede Zeile einzeln aus und ping sie
        for line in f:
            hostname = line.strip()
            try:
                response = os.system("ping -n 1 " + hostname)   # checkt einmal ob die domain erreichbar ist
            except Exception as err:
                print(err)
            # wenn die domain erreichbar ist wird sie in die Datei "reachable.txt" geschrieben
            if response == 0:
                print (hostname, 'is up!')
                log('reachable', hostname)
            # wenn die domain nicht erreichbar ist wird sie in die Datei "unreachable.txt" geschrieben
            else:
                print (hostname, 'is down!')
                log('unreachable', hostname)
    # schließt die Datei
    f.close()


def log(datei, domain):
    try:
        #schreibe jede domain in die Datei "reachable.txt" oder "unreachable.txt"
        # je nachdem ob die domain erreichbar ist oder nicht
        
        f = open(datei + '.txt', 'a')
        f.write(domain+'\n')
    except Exception as err:
        print(err)



delete()
search()