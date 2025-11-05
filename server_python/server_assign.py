"""
    This is for Assignment API: 1.4 Client/Server using JSON in Python
"""

import socket
import json

def start_server():
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind
    HOST = '127.0.0.1'
    PORT = 12345
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    try:
        # Create loop for multiple interactions in one go
        while True:
            client_socket, address = server_socket.accept()
            print(f"Connection from {address} has been established.")

            # communicate with client server and give json
            try:
                while True:
                    data = client_socket.recv(1024).decode('utf-8').strip()

                    if data.lower() == "get json":
                        # listens for get json and sends it back
                        response = json.dumps({"name": "Will"})
                    elif data.lower() == "quit": # client quit
                        break
                    else:
                        # any other prompt, send it back
                        response = f"Echo: {data}"
                    
                    client_socket.send(response.encode('utf-8'))

            # Handle Exceptions
            except Exception as e:
                print(f"Error handling client {address}: {e}")
            finally:
                print(f"Closing connection from {address}")
                client_socket.close()

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        # Close Socket
        server_socket.close()
    
if __name__ == "__main__":
    start_server()


