import socket


HEADER=64
SERVER="192.168.1.104"
PORT=5050
ADDR=(SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT= "!DISCONNECT"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len=len(message)
    send_len=str(msg_len).encode(format)
    send_len += b' '*(HEADER - len(send_len))
    client.send(send_len)
    client.send(message)