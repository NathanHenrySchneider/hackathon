import socket
import time
from _thread import *
import threading
from generator import generate, get_current_key

# Stores the users and their associated keys.
USER_KEYS = {}
KEY_PROMPT = "Please enter your key: "

# Handles each client individually.
def handle_requests(c):
    # Getting username from client.
    username = c.recv(1024).decode('ascii')

    # If user already exists, prompt them for their key.
    if check_valid_user(username):
        response = KEY_PROMPT

        # Ask user for key.
        c.send(response.encode('ascii'))

        # Get key from user. 
        key = c.recv(1024).decode('ascii')

        # If the key is correct...
        if key == USER_KEYS[username]:

            # Generate a new key for the user and store it.
            new_key = get_current_key()
            USER_KEYS[username] = new_key
            response = "That is the correct key. Your new key is: " + new_key

            # Inform the user that their key was correct and give them the new key.
            c.send(response.encode('ascii'))

        # If the key is incorrect...
        else:
            response = "That is not the correct key, please try again."

            # Inform the user that the key was incorrect.
            c.send(response.encode('ascii'))

    # If it is a brand new user...
    else:

        # Get a brand new key.
        key = get_current_key()
        USER_KEYS[username] = key
        response = "You are a new user, your key is: " + key

        # Give the new user their key.
        c.send(response.encode('ascii'))

    c.close()

# Checks to see if a user exists.
def check_valid_user(username):
    return (username in USER_KEYS)

def main():
    host = ""
    port = 12345

    # Create socket for client to connect to.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    # Start the infinite key generation.
    start_new_thread(generate, ())

    # Socket listens for clients.
    s.listen(5)
    print("Server is ready for connection...\n")

    while True:

        # Establish connection with client.
        c, addr = s.accept()
        s.setblocking(1)

        # Start a new thread for each individual client.
        print("Starting new client thread.")
        start_new_thread(handle_requests, (c,))
    s.close()


if __name__ == '__main__':
    main()
