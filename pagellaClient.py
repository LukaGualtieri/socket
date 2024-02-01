import socket
import json

# Configurazione del client
indirizzo = '127.0.0.1'
porta = 22225

# Creazione del socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((indirizzo, porta))

print(f"Connesso a {indirizzo}:{porta}")

while True:
    # Mostra i comandi disponibili
    print("\nComandi disponibili;")
    print("# list : per vedere i voti inseriti")
    print("# get /nomestudente : per richiedere i voti di uno studente")
    print("# set /nomestudente : per inserire uno studente")
    print("# put /nomestudente/materia/voto/ore : per aggiungere i voti della materia allo studente")
    print("# close : per chiudere la connessione")

    # Input del comando
    comando = input("Digita il comando: ")

    # Invia il comando al server
    client_socket.send(json.dumps({"comando": comando, "parametri": ""}).encode('utf-8'))

    # Riceve la risposta dal server
    risposta = client_socket.recv(1024).decode('utf-8')
    risposta = json.loads(risposta)

    # Mostra la risposta del server
    print(risposta["risposta"])
    if risposta["valori"] is not None:
        print(risposta["valori"])

    # Chiude la connessione se il comando è #close
    if comando == "#close":
        break

# Chiusura del socket
client_socket.close()
print("Connessione chiusa")
