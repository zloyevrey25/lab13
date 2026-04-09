import socket
import pickle

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

print("pickle server listening")

conn, addr = sock.accept()
print("client connected", addr)

data = conn.recv(4096)
obj = pickle.loads(data)
print("received object:", obj)

conn.send(data)

conn.close()
sock.close()