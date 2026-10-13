import socket , pickle

#host = socket.gethostname()
host = "localhost"
#host = "192.168.1.131"

port = 12345  # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send('si'.encode())  # we send this string
domanda = s.recv(4090)
print('Server:[',domanda.decode(),']')
s.send('si manda pure.'.encode())
array1 = s.recv(4096)
array = pickle.loads(array1)

print('Server:[','Ecco il nostro array:',array,']')
s.close()
