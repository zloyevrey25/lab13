import socket
import pickle

sock = socket.socket()
sock.connect(('localhost', 9090))

obj = {"name": "alice", "n": 42}
sock.send(pickle.dumps(obj))

reply = pickle.loads(sock.recv(4096))
print("echo", reply)

sock.close()