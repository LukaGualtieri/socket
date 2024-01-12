import socket,json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024
NUM_MESSAGES = 5

#Creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(NUM_MESSAGES):
    #Invio delmessaggio al server
    message = "ping"
    sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    print(f"Messaggio inviato al server: {message}")

    #Ricezione della risposta dal server 
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Messaggio ricevuto dal server {addr}: {data.decode()}")

#Chiusura del socket
sock.close()

data=cs.recv(1024)
#if len(data) ==0:   
    break
data=data.decode()
data=json.loads(data)
primoNumero=data['primoNumero']
operazione=data['operazione']
secondoNumero=data['secondoNumero']