import socket
import threading

HEADER=64
SERVER=socket.gethostbyname(socket.gethostname())
PORT=5050
ADDR=(SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT= "!DISCONNECT"

server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected")
    
    connected =True
    while connected:
        msg_len=conn.recv(HEADER).decode(FORMAT)#blocking line of code, thread wird geblockt/wartet auf i/o
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            
            if msg == DISCONNECT:
                connected =False

            print(f"[{addr}]{msg}")
    conn.close()



def start():
    server.listen()
    print(f"[LISTENING] is listing on {SERVER}")
    while True:
        conn, addr = server.accept()#waartet bis nächste conn kommt
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")
print("[STARTING] Breee, ich fahre hoch")
start()
