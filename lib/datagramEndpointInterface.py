from socket import socket, AF_INET, SOCK_DGRAM
import asyncio


class DatagramEndpointInterface:
    def __init__(self, handler):
        self.handler = handler

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        self.handler(message, addr)
