import socket,json

indirizzo = '127.0.0.1'
porta = 22225

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((indirizzo, porta))
server_socket.listen()

print(f"In ascolto su {indirizzo}:{porta}")

connessione, indirizzo_client = server_socket.accept()
print(f"Connesso a {indirizzo_client}")


# Funzione gestisci_comando
def gestisci_comando(comando, parametri, voti):
    print(comando,parametri)
    if comando == "#list":
        return "Caricamento...", voti
    elif comando == "#get":
        nome_studente = parametri.strip('/')
        if nome_studente in voti:
            return "Certo! I voti dello studente sono:", voti[nome_studente]
        else:
            return "Attenzione, errore!", "Studente non presente!"
    elif comando.startswith("#set"):
        nome_studente = parametri.strip('/')
        if nome_studente not in voti:
            voti[nome_studente] = []
            return "Inserimento dello studente in corso, attendere...", "Studente inserito con successo!"
        else:
            return "Attenzione, errore!", "Studente già presente!"
    elif comando.startswith("#put"):
        nome_studente, materia, voto, ore = parametri
        if nome_studente in voti:
            for materia_voto in voti[nome_studente]:
                if materia_voto[0] == materia:
                    return "Attenzione, errore!", "Materia già presente!"
            voti[nome_studente].append([materia, float(voto), int(ore)])
            return "Inserimento della materia in corso, attendere...", "Materia inserita con successo!"
        else:
            return "Attenzione, errore!", "Studente non presente!"
    elif comando == "#close":
        return "Connessione chiusa con successo!", None
    else:
        return "Comando non riconosciuto", None

# Dizionario dei voti
voti = {
    'Antonio Barbera': [['Matematica', 8, 1], ['Italiano', 6, 1], ['Inglese', 9.5, 0], ['Storia', 8, 2], ['Geografia', 8, 1]],
    'Giuseppe Gullo': [['Matematica', 9, 0], ['Italiano', 7, 3], ['Inglese', 7.5, 4], ['Storia', 7.5, 4], ['Geografia', 5, 7]],
    'Nicola Spina': [['Matematica', 7.5, 2], ['Italiano', 6, 2], ['Inglese', 4, 3], ['Storia', 8.5, 2], ['Geografia', 8, 2]]
}

while True:
    dati = connessione.recv(1024).decode('utf-8')
    if not dati:
        break

    dati = json.loads(dati)
    comando = dati['comando']
    parametri = dati['parametri']

    risposta, valori = gestisci_comando(comando, parametri, voti)

    risposta_json = {"risposta": risposta, 
                     "valori": valori
                     }
    connessione.send(json.dumps(risposta_json).encode('utf-8'))

    if comando == "#close":
        break

connessione.close()
server_socket.close()
print("Server chiuso")