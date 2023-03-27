import socket
import argparse

parser = argparse.ArgumentParser(description="This utility is used to send a message (read from a file) to TCPIP server endpoint",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-s", "--server", help="IP addr or hostname of the TCPIP server")
parser.add_argument("-p", "--port", help="Port of the TCPIP server")
parser.add_argument("-f", "--file", help="provide a file that contains a XML message")
args = parser.parse_args()
config = vars(args)
print(config)

# Define the server IP address and port number
SERVER_IP = config['server']
SERVER_PORT = int(config['port'])

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((SERVER_IP, SERVER_PORT))

# Read the file content
with open(config['file'], 'r') as file:
    message = file.read()
file.close();

# Send the message to the server
print(f'Sending: {message}')
sock.sendall(message.encode("utf-8"))
print(f'Sent!');

# print(f'Receiving ...')
response = sock.recv(1024).decode("utf-8")
print(f'Received: {response}')

# Close the socket
sock.close()