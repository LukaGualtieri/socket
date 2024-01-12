import socket,json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

#Creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

primoNumero=float(primoNumero)
operazione=input("Inserisci l'operazione: (+,-,*,/,%)")
secondoNumero=float(input("Inserisci il secondo numero: "))
messaggio={'primoNumero': primoNumero,
           'operazione': operazione,
           'secondoNumero': secondoNumero}
messaggio=json.dumps(messaggio) #trasformiamo l'oggetto in stringa
s.sendall(messaggio.encode("UTF-8"))
data=s.recv(1024)
print("Risultato: ",data.decode())

print("Server in attesa di messaggi...")

while True:
    #Ricezione dei dati dal client
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Messaggio ricevuto dal client {addr}: {data.decode()}")

    #Invio di una risposta al client
    reply = "pong"
    sock.sendto(reply.encode(), addr)


