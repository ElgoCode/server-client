import socket

server = socket.socket()

server.bind(("127.0.0.1",8787))

server.listen(1)


print("waiting for connections...")

# this line will block until someone connected
client,address = server.accept()


# sending msg to client in bytes-->(encode)
client.send("Hello World".encode())

client.close()

server.close()

print("ElgoCode $erver shutdowned...")
print("bye :)")









