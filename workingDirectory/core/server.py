# first of all import the socket library
import socket
# import thread module
from _thread import *
import threading
from generator import generate, get_current_key

print_lock = threading.Lock()

# thread function - handling requests
def handle_requests(c):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break

        # change later
        print('Handling Requests')

        # send back string to client
        c.send(data)

    # connection closed
    c.close()


def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    start_new_thread(generate, ())

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(handle_requests, (c,))

        # start_new_thread(generate)
    s.close()


if __name__ == '__main__':
    Main()
