import socket

s = socket.socket()
host = socket.gethostname()
port = 10048
s.bind((host,port))  
s.listen(1)
print(host) 
print("waiting for any incoming connections ...")
conn, addr = s.accept()
print(addr, "has connected to the server") 

filename = input(str("please enter the filename of the file : "))
file = open(filename, 'rb')
file_data = file.read(1024) 
conn.send(file_data)
print("data has been transmitted successfully")