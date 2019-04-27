from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
import tkinter
from tkinter import ttk
import os
os.system("start /min Python server.py")

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    popup.configure(background="grey")
    label = ttk.Label(popup, text=msg, font=("Verdana", 12))
    label.configure(background="grey")
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break


def send(event=None):
    msg = my_msg.get()
    my_msg.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{sair}":
        client_socket.close()
        top.destroy()


def on_closing(event=None):
    my_msg.set("{sair}")
    send()

top = tkinter.Tk()
top.title("Chatzin do Zé")
top.configure(background = "grey")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)

msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set,bg = "grey")
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg,bg = "black",fg = "white")
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Enviar", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

HOST = input('Digite o ip: ')
PORT = input('Digite a porta: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
popupmsg("Obrigado por usar o chat!")