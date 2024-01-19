# Server
import socket,json

# Configurazione del server
IP="127.0.0.1"
PORTA = 65432
DIM_BUFFER = 1024

#Creazione della socket del server con il costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

    #Binding della socket alla porta specificata
    sock_server.bind((IP, PORTA))

    #Metti la socket in ascolto per le connessioni in ingresso
    sock_server.listen()
    print(f"Server in ascolto su {IP}:{PORTA}...")

    #Loop principale del server
    while True:
        sock_service, address_client = sock_server.accept()
        print(f"Ricevuta connessione da {address_client}")
        with sock_service as sock_client:
            while True:
                data,addr=sock_client.recvfrom(1024)
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
                    ris=primoNumero/secondoNumero
                elif(operazione=="%"):
                    ris=primoNumero%secondoNumero

                sock_client.sendall(str(ris).encode())