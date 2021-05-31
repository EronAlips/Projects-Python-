import socket as u, threading, os
bind_ip ="0.0.0.0"
bind_port = 190

server = u.socket(u.AF_INET, u.SOCK_STREAM)

server.bind((bind_ip, bind_port))                                     # 1
server.listen(5)                                                      # 2

#print("listening on %s:%d" % (bind_ip, bind_port))
print(f"Listening on {bind_ip}: {bind_port}")

def handleClient(clientSocket):                                     # 3
    request = clientSocket.recv(1024)
    #print("[*] Received: %s:" % request)
    print(f"Recieved {request}")

    clientSocket.send("ACK")
    clientSocket.close()


while True:
    client, addr = server.accept()                                     # 4

    #print("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))
    print(f"Accepted connection from {addr[0]}, {addr[1]}")

    clientHandler = threading.Thread(target=handleClient, args=(client))
    clientHandler.start()                                            # 5



host = '192.168.0.196'
if i.name == 'nt':
    socketProtocol = u.IPPROTO_IP
else:
    socketProtocol = u.IPPROTO_ICMP

sniffer = u.socket(u.AF_INET, u.SOCK_RAW, socketProtocol)
sniffer.bind((host, 0))
sniffer.setsockpot(u.IPPROTO_IP, u.IP_HDRINCL, 1)

if i.name == 'nt':
    sniffer.ioctl(u.SIO_RCVALL, u.RCVALL_ON)
print(sniffer.recvfrom(65565))







