# Client
import socket,json

HOST = '127.0.0.1' # Indirizzo del server
PORT = 65432 # Porta usata dal server
DIM_BUFFER = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
   sock_service.connect((HOST, PORT))
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
        break

#a questo punto la socket è stata chiusa automaticamente
print('Socket chiusa!')