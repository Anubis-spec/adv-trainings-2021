import socket
import sys
import errno
import os

listen_socket = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)

try:
    listen_socket.bind("./superstructure")
except OSError as e:
    if e.errno == errno.EADDRINUSE:
        os.unlink("./superstructure")
        listen_socket.bind("./supersturcture")

listen_socket.listen()
conn_socket, _ = listen_socket.accept()

print("Write:")
for line in sys.stdin:
    input_bytes = bytes.fromhex(line)
    conn_socket.send(input_bytes[::-1])
    data = conn_socket.recv(4)
    print("Read {} bytes: {}".format(len(data), data.hex()))
    print("Write:")
