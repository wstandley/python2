"""
    This is for Assignment API: 1.4 Client/Server using JSON in Python
"""

import socket
import json

def client_start():
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define server address and connect
    HOST = '127.0.0.1'
    PORT = 12345

    try:
        # Connect
        client_socket.connect((HOST, PORT))

        while True:
            # Send a message to server
            message = input("Enter command: ")
            client_socket.send(message.encode('utf-8'))

            if message.lower() == "quit": # Allow client to quit out
                break

            # Receive the response from the server
            response = client_socket.recv(1024).decode('utf-8').strip()

            try:
                # Receive json and display it
                json_data = json.loads(response)
                print("Received JSON:")
                print(json.dumps(json_data, indent=4))
            except json.JSONDecodeError:
                print(f"Received: {response}")
    
    # Handle exceptions
    except ConnectionRefusedError:
        print("Connection failed. Is the server running?")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close socket
        client_socket.close()
        print("Connection Closed")

if __name__ == "__main__":
    client_start()