# Server
import socket,json
from threading import Thread

# Configurazione del server
SERVER_ADDRESS='127.0.0.1'
SERVER_PORT = 22224
DIM_BUFFER = 1024

def ricevi_comandi(sock_service, addr_client):
    print("Server avviato!")
    while True:
        data=sock_service.recv(DIM_BUFFER)
        if not data:
            break
        data=data.decode()
        data=json.loads(data)
        primoNumero=data["primoNumero"]
        operazione=data["operazione"]
        secondoNumero=data["secondoNumero"]

        ris=0
        if(operazione=="+"):
            ris=primoNumero+secondoNumero
        elif(operazione=="-"):
            ris=primoNumero-secondoNumero
        elif(operazione=="*"):
            ris=primoNumero*secondoNumero
        elif(operazione=="/"):
            if(primoNumero == 0):
                ris="Non puoi dividere per 0"
            else:
                ris=primoNumero/secondoNumero
        elif(operazione=="%"):
            ris=primoNumero%secondoNumero
        sock_service.sendall(str(ris).encode())
    sock_service.close()


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



if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)
print("Termina servizi")
