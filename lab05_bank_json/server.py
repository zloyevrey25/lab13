import socket
import json

balance = 1000

sock = socket.socket()
sock.bind(('', 9092))
sock.listen(1)

print("bank server listening on 9092")

while True:
    conn, addr = sock.accept()
    print("client connected", addr)

    data = conn.recv(1024).decode()
    request = json.loads(data)

    action = request.get("action")

    if action == "balance":
        reply = {"ok": True, "balance": balance}

    elif action == "deposit":
        amount = request.get("amount", 0)
        balance += amount
        reply = {"ok": True, "balance": balance}

    elif action == "withdraw":
        amount = request.get("amount", 0)
        if amount > balance:
            reply = {"ok": False, "error": "not enough money"}
        else:
            balance -= amount
            reply = {"ok": True, "balance": balance}

    else:
        reply = {"ok": False, "error": "unknown action"}

    conn.send(json.dumps(reply).encode())
    conn.close()