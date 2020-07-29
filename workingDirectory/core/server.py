# first of all import the socket library
import socket
import time
from _thread import *
import threading
from generator import generate, get_current_key

USER_KEYS = {}
KEY_PROMPT = "Please enter your key: "


# thread function - handling requests
def handle_requests(c):
    #while True:

    # data received from client
    username = c.recv(1024).decode('ascii')

    if check_valid_user(username):
        response = KEY_PROMPT
        c.send(response.encode('ascii'))
        key = c.recv(1024).decode('ascii')
        if key == USER_KEYS[username]:
            print("Key is correct")
            new_key = get_current_key()
            USER_KEYS[username] = new_key
            response = "That is the correct key. Your new key is:  " + new_key
            c.send(response.encode('ascii'))
        else:
            response = "That is not the correct key, please try again."
            c.send(response.encode('ascii'))
    else:
        key = get_current_key()
        USER_KEYS[username] = key
        response = "You are a new user, your key is: " + key
        c.send(response.encode('ascii'))

    c.close()

def check_valid_user(username):
    return (username in USER_KEYS)

def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    start_new_thread(generate, ())

    # put the socket into listening mode
    s.listen(5)

    print("Server is ready for connection...\n")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()
        s.setblocking(1)

        # Start a new thread and return its identifier
        print("Starting new client thread.")
        start_new_thread(handle_requests, (c,))
    s.close()


if __name__ == '__main__':
    Main()
