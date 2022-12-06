import socket       # to check connection to server
from tkinter import *
from tkinter import ttk

def delete():
    try:
        open('reachable.txt', 'w').close()
        open('unreachable.txt', 'w').close()
    except Exception as err:
        print(err)


def check():
    # liest die Datei aus in der die Hostname stehen
    f = open('list.txt', 'r')


    # list jede Zeile einzeln aus und ping sie
    for line in f:
        serveradress = line.strip()
        try:
            server_hostname,server_port = serveradress.split(':')       # splitte die Zeile in hostname und port

        except Exception as err:
            print(err)
            print(f'''
            Fehler in der Zeile: {line}'
            
            Bitte überprüfen Sie die Syntax der Datei "list.txt"!
            Syntax: hostname:port
            ''')
            break

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # erstelle socket
            s.settimeout(2)                                    # setze timeout
            s.connect((server_hostname, int(server_port)))   # versucht sich mit server zu verbinden
            print (server_hostname, 'ist erreichbar!')      # wenn erfolgreich, dann printe
            log('reachable', serveradress)        # und schreibe in die Datei "reachable.txt"
        # wenn nicht erfolgreich, dann printe und schreibe in die Datei "unreachable.txt"
        except Exception as err:
            print(err)
            print (server_hostname, 'ist nicht erreichbar!')
            log('unreachable', serveradress)
    
    s.close()   # schließe socket
    f.close()   # schließe datei


def log(datei, domain):
    try:
        #schreibe jede domain in die Datei "reachable.txt" oder "unreachable.txt"
        # je nachdem ob die domain erreichbar ist oder nicht
        
        f = open(datei + '.txt', 'a')
        f.write(domain+'\n')
    except Exception as err:
        print(err)




def start():
    delete()
    check()
