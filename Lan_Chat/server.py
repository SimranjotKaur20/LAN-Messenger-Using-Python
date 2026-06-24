import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))
server.listen()

print("Waiting for client...")

client, address = server.accept()
print("Connected:", address)

while True:
    msg = client.recv(1024).decode()

    if msg.lower() == "exit":
        break

    print("Client:", msg)

    reply = input("You: ")
    client.send(reply.encode())

client.close()
server.close()