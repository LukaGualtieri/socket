# Server
import socket,json
from threading import Thread

# Configurazione del server
SERVER_ADDRESS="127.0.0.1"
SERVER_PORT = 22224
DIM_BUFFER = 1024


def ricevi_comandi(sock_service, addr_client):
    while True:
        primoNumero=float(input("Inserisci il primo numero: "))
        operazione=input("Inserisci l'operazione (+,-,*,/,%): ")
        secondoNumero=float(input("Inserisci il secondo numero: "))
        messaggio={"primoNumero":primoNumero,
                "operazione":operazione,
                "secondoNumero":secondoNumero}
        messaggio=json.dumps(messaggio) #trasformiamo l'oggetto in una stringa
        sock_service.sendall(messaggio.encode("UTF-8"))
        data=sock_service.recv(DIM_BUFFER)
        print("Risultato: ",data.decode())

        risposta=(input("--- Eseguire un altro calcolo? s-si n-no --- "))
        if(risposta=='n'):
            sock_service.close()
            break


def ricevi_connessione(sock_listen):
    while True:
        sock_service, addr_client=sock_listen.accept()
        print("\nConnessione ricevuta da %s" % str(addr_client))
        print("Creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("Errore, il thread non si avvia! :(")
            sock_listen.close()


def avvia_server(SERVER_ADDRESS, SERVER_PORT):
    try:
        sock_listen=socket.socket()
        sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
        sock_listen.listen()
        print(f"Server in ascolto su {SERVER_ADDRESS}:{SERVER_PORT}...")
        ricevi_connessione(sock_listen)
    except socket.error as errore:
        print(f"Qualcosa è andato storto :(  \n{errore}")



if __name__ == ' __main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)
print("Termina servizi")