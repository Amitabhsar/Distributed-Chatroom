import socket
import threading
import time
import random
import string
import logging

logging.basicConfig(filename='test_client_large_case_scenario.log', level=logging.INFO, format='%(asctime)s %(message)s')

HOST = '127.0.0.7'
PORT = 65528
NUM_CLIENTS = 5
MESSAGE_LENGTHS = [30000, 50000]
MESSAGES_PER_CLIENT = 300

def generate_message(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def client_simulation(client_id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((HOST, PORT))
            client_socket.sendall(f"TestClient{client_id}".encode())

            for _ in range(MESSAGES_PER_CLIENT):
                message_length = random.choice(MESSAGE_LENGTHS)
                message = generate_message(message_length)
                start_time = time.time()
                client_socket.sendall(message.encode())
                end_time = time.time()

                logging.info(f"TestClient{client_id} sent {message_length}-byte message in {end_time - start_time:.4f} seconds")
        except Exception as e:
            logging.error(f"TestClient{client_id} encountered an error: {e}")

def main():
    threads = []
    for i in range(NUM_CLIENTS):
        thread = threading.Thread(target=client_simulation, args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
