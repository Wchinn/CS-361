import pickle
from socket import *

s = socket(type=SOCK_DGRAM)
MESSAGE = b'Light'
DESTINATION_ADDRESS = ('localhost', 5000)
print(f'sending message:{MESSAGE}')
s.sendto(MESSAGE,DESTINATION_ADDRESS)
print(f'Message sent')
print(f'Recieving message')
data,addr = s.recvfrom(1024)
print(f'Message recieved')
print(pickle.loads(data),addr)

s = socket(type=SOCK_DGRAM)
MESSAGE = b'Dark'
DESTINATION_ADDRESS = ('localhost', 5000)
print(f'sending message:{MESSAGE}')
s.sendto(MESSAGE,DESTINATION_ADDRESS)
print(f'Message sent')
print(f'Recieving message')
data,addr = s.recvfrom(1024)
print(f'Message recieved')
print(pickle.loads(data),addr)
