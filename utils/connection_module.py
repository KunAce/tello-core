import threading
import socket

# Client Device info
host = ''
port = 9000
device_address = (host, port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(device_address)

print("Tello Python3 Terminal")
print('Command List: ')
print('')
print('exit -- exit the Command Terminal')


# Receiving data
def recv():
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding='utf-8'))
        except Exception:
            print("\nError happened. Exiting...\n")
            break


recv_thread = threading.Thread(target=recv())
recv_thread.start()


# Command Dictionary
# command_dict = {'':}

# The Command Terminal
while True:
    try:
        cmd = input("Please enter the command:")
        if not cmd:
            break
        if cmd == 'exit':
            print("Exiting the Command Terminal...")
            sock.close()
            break
        cmd = cmd.encode(encoding="utf-8")
        sent_result = sock.sendto(cmd, tello_address)
    except KeyboardInterrupt:
        print('\n Closing the socket...')
        sock.close()
        break

