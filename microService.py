import pickle
from socket import *

lightDict = {'background': "#EFE7E5", 'foreground': "#FFFFFF", 'borderlines': "#8C8C8C", 'textcolor': "#000000"}
darkDict = {'background': "#2F2F2F", 'foreground': "#404040", 'borderlines': '#000000', 'textcolor': "#EFEFEF" }

serializedLightDict = pickle.dumps(lightDict)#.encode("base64", "strict")
serializedDarkDict = pickle.dumps(darkDict)#.encode("base64", "strict")


s = socket(type=SOCK_DGRAM)
s.bind(('localhost',5000))

while True:
    data,addr = s.recvfrom(1024)
    print(data,addr)


    if data == b"Light":
        responseMessage = serializedLightDict
    elif data == b"Dark":
        responseMessage = serializedDarkDict
    s.sendto(responseMessage, addr)
   
    
