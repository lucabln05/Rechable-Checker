from tkinter import *
from tkinter import ttk
from check import start
import threading
import time
import webbrowser       #https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter


#function um website zu öffnen, noch nicht fertig
def callback(url):
    webbrowser.open_new(url)


def wait_for_check():
    
    threading.Thread(target=loading_screen).start()   #startet das Lade Fenster

    #checkt wie viele ips gecheckt werden sollen
    list_file = open('list.txt', 'r')
    check_len = len(list_file.readlines())

    prognose_check_time = check_len             #berechnet die Zeit die der check benötigt da jede ip nur 2 sekunden zum checken benötigt (maximal wenn nicht noch schneller)
    time.sleep(prognose_check_time)

    threading.Thread(target=main_window).start()    #startet das Hauptfenster wenn der check fertig ist

    loading_screen.root.destroy()                   #schließt das Lade Fenster


def loading_screen():
    #loading screen für den check
    loading_screen.root = Tk()
    loading_screen.root.title("L O A D I N G")
    loading_screen.root.geometry("250x50")

    ttk.Label(loading_screen.root, text="Checke Server Verbindungen...").pack()

    #progressbar fuer nutzerfeedback
    progress = ttk.Progressbar(loading_screen.root, orient=HORIZONTAL, length=200, mode='indeterminate')
    progress.pack()
    progress.start()
    

    ttk.Label(loading_screen.root, text="").pack()

    loading_screen.root.mainloop()


def main_window():
    #hauptfenster das die erreichbaren server anzeigt
    root = Tk()
    root.title("Moitoring System")
    root.geometry("400x400")


    reachable_file_len = len(open('reachable.txt', 'r').readlines())
    ttk.Label(root, text=f"Erreichbare Server({reachable_file_len}): ", foreground="green").pack()
   
    reachable_file = open('reachable.txt', 'r')

    for line in reachable_file:
        serverip, serveralias = line.split(" AS ")
        ttk.Label(root, text="").pack()
        server_adress = ttk.Label(root, text=f'{serveralias} ({serverip})')
        server_adress.pack()



    ttk.Label(root, text="").pack()
    unreachable_file_len = len(open('unreachable.txt', 'r').readlines())
    ttk.Label(root, text=f"Nicht Erreichbare Server({unreachable_file_len}): ", foreground="red").pack()

    unreachable_file = open('unreachable.txt', 'r')
    
    for line in unreachable_file:
        serverip, serveralias = line.split(" AS ")
        ttk.Label(root, text="").pack()
        server_adress = ttk.Label(root, text=f'{serveralias} ({serverip})')
        server_adress.pack()


    root.mainloop()



threading.Thread(target=start).start()                  #startet den server check in einem neuen Thread 
threading.Thread(target=wait_for_check).start()


