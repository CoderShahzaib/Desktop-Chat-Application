import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

def receive_messages():
    while True:
        try:
            msg = s.recv(1024).decode("utf-8")
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, msg + "\n")
            chat_area.config(state=tk.DISABLED)
        except:
            break

def send_message():
    msg = message_entry.get()
    s.send(msg.encode("utf-8"))
    message_entry.delete(0, tk.END)
    if msg == "quit":
        s.close()
        window.quit()

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set server IP and port (make sure this matches the server's IP address)
host = '192.168.100.21'  # Change this to your server's IP address
port = 1255

# Connect to the server
s.connect((host, port))

# Create the main window
window = tk.Tk()
window.title("Chat Client")

# Create a scrolled text widget for displaying messages
chat_area = scrolledtext.ScrolledText(window, state=tk.DISABLED)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an entry widget for typing messages
message_entry = tk.Entry(window)
message_entry.pack(padx=10, pady=10, fill=tk.X, expand=True)

# Create a send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start the Tkinter event loop
window.mainloop()
