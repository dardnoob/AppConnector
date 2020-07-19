# AppConnector
AppConnector is a simple TCP server/client written for Python 2/3 using Qt.


### Requirements
* PySide for Python <= 2.7
* PySide2 for Python >= 2.7
* Six


### How to use

##### Server example

```
from appconnector.server import Server

server = Server("127.0.0.1", 8080)

def parse(data):
    if data == "hello, it`s me":
        return "hello, it`s you"
    return ""

def received_slot(key, message):
    response = parse(message)
    if response:
        server.get(key).send(response)

server.received.connect(received_slot)
server.start()
```

##### Client example

```
from appconnector.client import Client

client = Client("127.0.0.1", 8080)

def parse(data):
    if data == "hello, it`s you":
        return "goodbye"
    return ""

def received_slot(key, message):
    response = parse(message)
    if response:
        client.send(response)

def connected_slot():
    client.send("hello, it`s me")

client.connected.connect(connected_slot)
client.received.connect(received_slot)
client.open()
```


### Problems
* 'incomingConnection' was not implemented on python 2.7 with PySide 1 for the QLocalServer.
* 'socketDescriptor' was not implemented on python 2.7 with PySide 1 for the QLocalSocket.


### TODO
* Add custom thread pool
* Rewrite the logic for working with sockets
* Find QLocalServer solution for python 2.7 with PySide 1
