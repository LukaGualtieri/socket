import socket, random, sys, os, time, threading, multiprocessing, json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
NUM_WORKERS = 15

def genera_richieste(address, port):
    try:
        start_time_thread = time.time()
        s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((address, port))
    except:
        print("Qualcosa è andato storto! :(")
    
    """start_time_thread = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
        sock_service.connect((address, port))"""

    comandi=['+','-','*','/','%']
    primoNumero=random.randint(1,1000)
    operatore=random.randint(0,4)
    operazione=comandi[operatore]
    secondoNumero=random.randint(1,1000)
    messaggio={"primoNumero":primoNumero,
               "operazione":operazione,
               "secondoNumero":secondoNumero}
    messaggio=json.dumps(messaggio) 
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    print("Risultato: ", data.decode())
    end_time_thread = time.time() 
    print(f"{threading.current_thread().name} execution time =", end_time_thread - start_time_thread)



if __name__ == '__main__':
    #Run tasks using threads
    start_time = time.time()
    threads = [threading.Thread(target=genera_richieste, args=(SERVER_ADDRESS,SERVER_PORT,)) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()

    print("Total threads time= ", end_time - start_time)