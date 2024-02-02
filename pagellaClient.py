import socket,json

indirizzo = '127.0.0.1'
porta = 22225

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((indirizzo, porta))

print(f"Connesso a {indirizzo}:{porta}")

while True:
    # Mostra tutti i comandi a schermo
    print("\nLista dei comandi disponibili:")
    print("#list : per vedere i voti inseriti")
    print("#get /nomestudente : per richiedere i voti di uno studente")
    print("#set /nomestudente : per inserire uno studente")
    print("#put /nomestudente/materia/voto/ore : per aggiungere i voti della materia allo studente")
    print("#close : per chiudere la connessione")

    comando = input("Digita il comando: ")
    parametri = comando.split(" ")

    if comando == "#list":
        client_socket.send(json.dumps({"comando": parametri[0].strip(), "parametri": ""}).encode('utf-8'))
    elif comando == "#put":
        client_socket.send(json.dumps({"comando": parametri[0].strip(), "parametri": parametri}).encode('utf-8'))
    else:
        client_socket.send(json.dumps({"comando": parametri[0].strip(), "parametri": parametri[1]}).encode('utf-8'))
 

    risposta =json.loads((client_socket.recv(1024)).decode('utf-8'))
    print(risposta)
    

    print(risposta["risposta"])
    if risposta["valori"] is not None:
        print(risposta["valori"])

    if comando == "#close":
        break

client_socket.close()
