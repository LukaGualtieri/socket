import json

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


data=cs.recv(1024)
#if len(data) ==0:   
   break
data=data.decode()
data=json.loads(data)
primoNumero=data['primoNumero']
operazione=data['operazione']
secondoNumero=data['secondoNumero']