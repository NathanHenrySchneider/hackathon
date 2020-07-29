# Import socket module
import socket
from server import KEY_PROMPT

# Sends the username to server.
# If the user already exists, they will next be prompted to enter their key.
# Otherwise, the user is assigned a new key.
def check_username(s, username):
    s.send(username.encode('ascii'))
    response = s.recv(1024) # hung here
    return response.decode('ascii')

def main():
    # local host IP
    host = '127.0.0.1'

    # Define the port on which you want to connect.
    port = 12345

    # Create server socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Connect to server on local computer.
    s.connect((host,port))

    # Prompt user for username.
    username = input('\nPlease enter your username: ')
    response = check_username(s, username)

    # If response is the key prompt (i.e. the user already exists), then user is prompted to enter their key.
    if response == KEY_PROMPT:
        key = input(KEY_PROMPT)
        s.send(key.encode('ascii'))
        response = s.recv(1024).decode('ascii')
        print(response)

    # Otherwise, the new user is given their newly generated key.
    else:
        print(response)
    print()

    # Closing the server connection.
    s.close()

if __name__ == '__main__':
    main()
