import socket
import json

# Funzione per gestire i comandi del client
def gestisci_comando(comando, parametri, voti):
    if comando == "#list":
        return "OK", voti
    elif comando.startswith("#get"):
        nome_studente = parametri.strip('/')
        if nome_studente in voti:
            return "OK", voti[nome_studente]
        else:
            return "KO", "Studente non presente"
    elif comando.startswith("#set"):
        nome_studente = parametri.strip('/')
        if nome_studente not in voti:
            voti[nome_studente] = []
            return "OK", "Studente inserito"
        else:
            return "KO", "Studente già presente"
    elif comando.startswith("#put"):
        parametri_lista = parametri.strip('/').split('/')
        nome_studente, materia, voto, ore = parametri_lista
        if nome_studente in voti:
            for materia_voto in voti[nome_studente]:
                if materia_voto[0] == materia:
                    return "KO", "Materia già presente"
            voti[nome_studente].append([materia, float(voto), int(ore)])
            return "OK", "Dati inseriti"
        else:
            return "KO", "Studente non presente"
    elif comando == "#close":
        return "Connessione chiusa", None
    else:
        return "Comando non riconosciuto", None

# Configurazione del server
indirizzo = '127.0.0.1'
porta = 22225

# Creazione del socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((indirizzo, porta))
server_socket.listen()

print(f"In ascolto su {indirizzo}:{porta}")

# Accettazione delle connessioni
connessione, indirizzo_client = server_socket.accept()
print(f"Connesso a {indirizzo_client}")

# Inizializzazione del dizionario dei voti
voti = {
    'Antonio Barbera': [['Matematica', 8, 1], ['Italiano', 6, 1], ['Inglese', 9.5, 0], ['Storia', 8, 2], ['Geografia', 8, 1]],
    'Giuseppe Gullo': [['Matematica', 9, 0], ['Italiano', 7, 3], ['Inglese', 7.5, 4], ['Storia', 7.5, 4], ['Geografia', 5, 7]],
    'Nicola Spina': [['Matematica', 7.5, 2], ['Italiano', 6, 2], ['Inglese', 4, 3], ['Storia', 8.5, 2], ['Geografia', 8, 2]]
}

while True:
    # Ricezione del comando dal client
    dati = connessione.recv(1024).decode('utf-8')
    if not dati:
        break

    # Parsing del comando JSON
    dati = json.loads(dati)
    comando = dati['comando']
    parametri = dati['parametri']

    # Gestione del comando
    risposta, valori = gestisci_comando(comando, parametri, voti)

    # Creazione della risposta in formato JSON
    risposta_json = {"risposta": risposta, "valori": valori}
    connessione.send(json.dumps(risposta_json).encode('utf-8'))

    # Chiude la connessione se il comando è #close
    if comando == "#close":
        break

# Chiusura del socket e del server
connessione.close()
server_socket.close()
print("Server chiuso")