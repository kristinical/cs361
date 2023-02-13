import zmq
import json
import random
from cities import cities

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Wait for request from client
    socket.recv()
    print("Generating a random location...")

    # Generate random location from list of "cities"
    city = random.choice(cities)

    # Send city in JSON format back to client
    socket.send_json(json.dumps(city))
    print("Location sent")

