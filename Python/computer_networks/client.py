import socket

import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Variable to track if the thread should stop
stop_thread = True


def stop():
    global stop_thread
    stop_thread = False


# Listening to Server and Sending Nickname
def receive():
    while stop_thread is True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break
    client.close()


def write():
    while stop_thread is True:
        user_input = input('')
        message = '{}: {}'.format(nickname, user_input)
        client.send(message.encode('ascii'))
        if user_input.lower() == 'exit':
            stop()

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread.join()
write_thread.join()
