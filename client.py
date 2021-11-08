import socket

client = socket.socket()

client.connect(("127.0.0.1",8787))


msg = client.recv(100) #100 is the number of bytes that can be recieved

msg = msg.decode() #convert bytes to string 

print(msg)

client.close()





