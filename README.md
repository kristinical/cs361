## About

This microservice generates and returns a random location as a city, country pair using ZeroMQ.

## Requesting Data

When a user clicks a button on the web interface to generate a random location, a ZeroMQ socket is established and a request is sent to the microservice I have implemented through port 5555. In order to establish this connection, the following client-side code is required (*this example uses Python. For other languages, see [ZeroMQ](https://zeromq.org/get-started/)*):

```
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```

Then, in order to call the microservice and make a request to generate a random location, the following line of code is used:

`socket.send(b'Generate location')`

Note: The sending message can be anything. 'Generate location' is one example shown here to initiate a request from the microservice server.

## Receiving Data

When the microservice receives a request from the client, it generates a location by choosing a random element from a list of (city, country) tuples. It then formats this location as a JSON list and sends it back to the client. The client can parse the JSON data as follows:

`location = json.loads(socket.recv_json())`

The location variable can then be parsed to get the city and country as strings by indexing into the list:
```
city = location[0]
country = location[1]
```

## UML Sequence Diagram
![UML sequence diagram](/UML%20Sequence%20Diagram.png)
