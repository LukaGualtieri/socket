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

    dati = input("Digita il comando: ")
    if  "list" in dati:
        comando="#list"
        parametri=""
    elif "get" in dati or "set" in dati: 
        comando,parametri = dati.split("/")
    elif "put" in dati:
        lista=dati.split("/")
        comando=lista[0]
        parametri=[lista[1],lista[2],lista[3],lista[4]]
    elif "#close" in dati:
        break 
    
    client_socket.send(json.dumps({"comando": comando.strip(), "parametri": parametri}).encode('utf-8'))

    risposta =json.loads((client_socket.recv(1024)).decode('utf-8'))    

    print(risposta["risposta"])
    if risposta["valori"] is not None:
        print(risposta["valori"])

client_socket.close()
print("Socket terminata con successo!")
