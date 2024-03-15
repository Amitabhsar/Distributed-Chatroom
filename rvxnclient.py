# client.py
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

HOST = '127.0.0.7'
PORT = 65528

# GUI Setup
root = tk.Tk()
root.title("Chatroom")
root.geometry("400x500")

def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

def connect():
    try:
        client.connect((HOST, PORT))
        messagebox.showinfo("Connected", f"Successfully connected to server {HOST} {PORT}")
        username = username_entry.get()
        if username:
            client.sendall(username.encode())
            threading.Thread(target=listen_for_messages_from_server, daemon=True).start()
            username_entry.config(state=tk.DISABLED)
            connect_button.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Invalid Username", "Please enter a valid username.")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Unable to connect to server {HOST} {PORT}: {e}")

def send_message():
    message = message_entry.get()
    if message:
        client.sendall(message.encode())
        message_entry.delete(0, tk.END)

def listen_for_messages_from_server():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                add_message(message)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            break

# GUI elements
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()

message_entry = tk.Entry(root)
message_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

message_box = scrolledtext.ScrolledText(root, state=tk.DISABLED)
message_box.pack(expand=True, fill='both')

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Start the GUI loop
root.mainloop()
