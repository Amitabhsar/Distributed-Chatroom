# server.py
import socket
import threading
from broker import start_broker, MessageBroker
import logging

logging.basicConfig(level=logging.INFO)

HOST = '127.0.0.7'
PORT = 65528
LISTENER_LIMIT = 5

def send_message_to_client(client, message):
    client.sendall(message.encode())

def client_handler(client, username, broker: MessageBroker):
    send_func = lambda msg: send_message_to_client(client, msg)
    broker.add_listener(send_func)
    
    try:
        while True:
            message = client.recv(2048).decode('utf-8')
            if message:
                formatted_message = f"{username}: {message}"
                logging.info(f"Received message: {formatted_message}")
                broker.receive_message(formatted_message)
            else:
                raise ConnectionError("Client disconnected")
    except ConnectionError:
        logging.info(f"{username} disconnected")
        broker.remove_listener(send_func)
        client.close()

def main():
    broker = start_broker()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(LISTENER_LIMIT)
    logging.info(f"Server running on {HOST}:{PORT}")

    try:
        while True:
            client, address = server.accept()
            username = client.recv(2048).decode('utf-8')
            logging.info(f"Connected to {username} from {address}")
            threading.Thread(target=client_handler, args=(client, username, broker), daemon=True).start()
    except KeyboardInterrupt:
        logging.info("Server shutting down")
        server.close()

if __name__ == '__main__':
    main()
