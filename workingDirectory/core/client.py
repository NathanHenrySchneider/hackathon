# Import socket module
import socket
from server import KEY_PROMPT

def check_username(s, username):
    s.send(username.encode('ascii'))
    response = s.recv(1024) # hung here
    return response.decode('ascii')

def Main():
    # local host IP '127.0.0.1'
    host = '127.0.0.1'

    # Define the port on which you want to connect
    port = 12345

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host,port))

    username = input('\nPlease enter your username: ')
    response = check_username(s, username)

    if response == KEY_PROMPT:
        key = input(KEY_PROMPT)
        s.send(key.encode('ascii'))
        response = s.recv(1024).decode('ascii')
        print(response)
    else:
        print(response)
    print()

    s.close()

if __name__ == '__main__':
    Main()
