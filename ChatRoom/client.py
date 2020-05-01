'''
Program name: ChatRoom
GUI Client: a GUI client that can communicate with the server.
            a client can send text messages to all parties in the chat room, 
            as well as receive notifications when other clients connect or disconnect. 
            Clients do not communicate directly with other clients. 
            Instead, all communication is routed through the central server.
'''
import socket
import threading
import tkinter as tk
from tkinter.filedialog import askopenfilename
import argparse
import os

def recvMessage(socket):
   while True:
      try:
         msg = socket.recv(4096).decode('utf8')
         msg_list.insert(tk.END, msg)
      except OSError:
         break

def sendMessage(event=None):
   msg = my_msg.get() 
   my_msg.set("")
   s.send(msg.encode('utf-8'))
   if msg == "Gotta go, TTYL!":
      s.close()
      window.quit()
      
def sendFile(event=None):
   file = askopenfilename()
   if(len(file) > 0 and os.path.isfile(file)):
      print("UI: Selected file: %s" % file)
      filename = file.split('/')
      with open(file, 'rb') as f:
         send_file_name = b'sending file name - ' + filename[-1].encode('utf-8') + b': '
         s.send(send_file_name + f.read())
   else:
      print("UI: File operation canceled")

def on_closing(event=None):
    my_msg.set("Gotta go, TTYL!")
    sendMessage()

if __name__ == '__main__':

    # Use argparse method
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('server_ip', nargs='?', default='localhost')
    parser.add_argument('server_port', nargs='?', default=8765)
    parser.add_argument('username')
    args = parser.parse_args()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.server_ip , args.server_port))
    
    window = tk.Tk()
    window.title("ChatRoom/1.0 Connected to: "+ args.server_ip + ": "+str(args.server_port))

    messages_frame = tk.Frame(window)
    my_msg = tk.StringVar()  
    my_msg.set("Enter Username...")
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

    window.protocol("WM_DELETE_WINDOW", on_closing)

    threading.Thread(target=recvMessage, args = (s,)).start()

    tk.mainloop()


