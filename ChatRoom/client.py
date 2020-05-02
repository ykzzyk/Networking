'''
Program name: ChatRoom/client.py

GUI Client: a GUI client that can communicate with the server.
            a client can send text messages to all parties in the chat room, 
            as well as receive notifications when other clients connect or disconnect. 
            Clients do not communicate directly with other clients. 
            Instead, all communication is routed through the central server.
            
Usage: Run python client.py -u <user-name> (default ip = 'localhost', default port = '8765')
'''
import socket
import threading
import tkinter as tk
from tkinter.filedialog import askopenfilename
import argparse
import os

# Receive message from the server
def recvMessage(socket):
   while True:
      try:
         msg = socket.recv(4096).decode('utf8')
         msg_list.insert(tk.END, msg)
      except OSError:
         break

# Send message to the server
def sendMessage(event=None):
   msg = my_msg.get() 
   my_msg.set("")
   s.send(msg.encode('utf-8'))
   if msg == "Gotta go, TTYL!":
      s.close()
      window.quit()
      
# Send file to the server
def sendFile(event=None):
   file = askopenfilename()
   if(len(file) > 0 and os.path.isfile(file)):
      print("UI: Selected file: %s" % file)
      with open(file, 'rb') as f:
         filename = b'sending file name - ' + file.split('/')[-1].encode('utf-8') + b': '
         s.send(filename + f.read())
   else:
      print("UI: File operation canceled")


# Close the window
def hover_close(event=None):
   my_msg.set("Gotta go, TTYL!")
   sendMessage()

# Main funciton
if __name__ == '__main__':
    # Use argparse method
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
    parser.add_argument('--server_ip', '-ip', nargs='?', default='localhost')
    parser.add_argument('--server_port', '-p', nargs='?', default=8765)
    parser.add_argument('--username', '-u')
    args = parser.parse_args()
    
    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.server_ip , args.server_port))
    
    # Use tkinter
    window = tk.Tk()
    window.title("ChatRoom/1.0 Connected to: "+ args.server_ip + ": "+str(args.server_port))
    
    messages_frame = tk.Frame(window)
    label = tk.Label(window, text = "TYPE <Gotta go, TTYL!> to QUIT", width = 53, font=("Helvetica", 12), fg="Blue", anchor="w")
    label.pack()
    
    my_msg = tk.StringVar()
    
    s.send(args.username.encode('utf-8'))
    
    
    scrollbar = tk.Scrollbar(messages_frame)  
    msg_list = tk.Listbox(messages_frame, height=25, width=40, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
    msg_list.pack()
    messages_frame.pack()

    entry_field = tk.Entry(window, textvariable=my_msg, width = 30)
    entry_field.bind("<Return>", sendMessage)
    entry_field.pack(side=tk.LEFT)
    send_button = tk.Button(window, text="Send", command=sendMessage, width=5)
    send_button.pack(side=tk.LEFT)
    
    file_button = tk.Button(window, text="File", command=sendFile, width = 5)
    file_button.pack(side=tk.LEFT)

    window.protocol("WM_DELETE_WINDOW", hover_close)

    threading.Thread(target=recvMessage, args = (s,)).start()

    tk.mainloop()


