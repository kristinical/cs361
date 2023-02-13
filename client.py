import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    choice = input("Would you like to generate a random city? (Y/N): ")
    if choice == "N":
        break
    elif choice != "Y":
        print('\nInvalid input (please enter "Y" or "N")')
        continue
    else:
        # Send request to microservice server
        socket.send(b'Generate location')

        # Receive location and parse JSON format
        location = json.loads(socket.recv_json())

        # City = index 0 / Country = index 1
        print(f"{location[0]}, {location[1]}\n")

