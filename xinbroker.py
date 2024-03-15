# broker.py
import socket
import threading
import queue
import logging

log_file_name = 'xinbroker.log'

logging.basicConfig(filename='log_file_name', level=logging.INFO, format='%(asctime)s %(message)s')

class MessageBroker:
    def __init__(self):
        self.messages = queue.Queue()
        self.listeners = []
        self.message_count = 0

    def add_listener(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_listener(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def distribute_message(self):
        while True:
            message = self.messages.get()
            self.message_count += 1
            logging.info(f"Distributed Message: {message}")
            for listener in self.listeners:
                listener(message)

    def receive_message(self, message):
        self.messages.put(message)

def start_broker():
    broker = MessageBroker()
    threading.Thread(target=broker.distribute_message, daemon=True).start()
    return broker

if __name__ == "__main__":
    start_broker()
    input("Broker running... Press Enter to exit.\n")
