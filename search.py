import socket


def delete():
    try:
        open('reachable.txt', 'w').close()
        open('unreachable.txt', 'w').close()
    except Exception as err:
        print(err)


def check():
    # liest die Datei aus in der die Hostname stehen
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    f = open('list.txt', 'r')
    # wie viele Domains gleichzeitig abgefragt werden sollen


    # list jede Zeile einzeln aus und ping sie
    for line in f:
        serveradress = line.strip()
        server_hostname,server_port = serveradress.split(':')       # splitte die Zeile in hostname und port

        try:
            s.connect((server_hostname, int(server_port)))
            print (server_hostname, 'ist erreichbar!')
            log('reachable', server_hostname)

        except Exception as err:
            print(err)
            print (server_hostname, 'ist nicht erreichbar!')
            log('unreachable', server_hostname)

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
check()
