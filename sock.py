import socket
class net:
    def __init__(self):
         self.s = 0
    def news(self):
         self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock = net()
