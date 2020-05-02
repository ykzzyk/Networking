import socket
import threading
import tkinter
import argparse

def echo_data(socket):
   while True:
      try:
         msg = socket.recv(4096).decode('utf8')
         msg_list.insert(tkinter.END, msg)
      except OSError:
         break

def send(event=None):
   msg = my_msg.get() 
   my_msg.set("")
   s.send(msg.encode('utf-8'))
   if msg == "{quit}":
      s.close()
      top.quit()

def on_closing(event=None):
    my_msg.set("{quit}")
    send()

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
    
    top = tkinter.Tk()
    top.title("Chat Room")

    messages_frame = tkinter.Frame(top)
    my_msg = tkinter.StringVar()  
    my_msg.set("Type your messages here.")
    scrollbar = tkinter.Scrollbar(messages_frame)  
    msg_list = tkinter.Listbox(messages_frame, height=30, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msg_list.pack()
    messages_frame.pack()

    entry_field = tkinter.Entry(top, textvariable=my_msg)
    entry_field.bind("<Return>", send)
    entry_field.pack()
    send_button = tkinter.Button(top, text="Send", command=send)
    send_button.pack()

    top.protocol("WM_DELETE_WINDOW", on_closing)

    threading.Thread(target=echo_data, args = (s,)).start()

    tkinter.mainloop()


