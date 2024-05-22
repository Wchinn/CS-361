# How to run the microservice
Required dependancies: Pickle, Socket

to do this all you have to do is run the testProgram.py file

# How to request data
The program has the byte string dark and byte string light. You set your message = to light or dark. Using the socket. Heres is an example in python for light mode.
```python
  MESSAGE = b"Light"
  s.sendto(MESSAGE,DESTINATION_ADDRESS)
```

# How to recieve data
We are recieving the data from the socket and we need to deserialize.
```python
  data,addr = s.recvfrom(1024)
  serializedLightDict = pickle.dumps(lightDict)
```

# Example Response
Example output for the light mode
```
{'background': '#EFE7E5', 'foreground': '#FFFFFF', 'borderlines': '#8C8C8C', 'textcolor': '#000000'} 
('127.0.0.1', 5000)
```

# Socket uses
s in the previous example is our socket which can be setup by doing the following
```
s = socket(type=SOCK_DGRAM)
s.bind(('localhost',5000))
```
