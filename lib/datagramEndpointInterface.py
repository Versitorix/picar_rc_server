from socket import socket, AF_INET, SOCK_DGRAM
from asyncio import BaseProtocol


class DatagramEndpointInterface(BaseProtocol):
    def __init__(self, handler):
        self.handler = handler
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        self.handler(message, addr)
