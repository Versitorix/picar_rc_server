import asyncio

from lib.datagramEndpointInterface import DatagramEndpointInterface
from lib.settings import SETTINGS


class CommandsServer:
    def __init__(self):
        self.address = SETTINGS['server_ip']
        self.port = SETTINGS['commands_port']

    async def start(self):
        loop = asyncio.get_running_loop()

        transport, protocol = await loop.create_datagram_endpoint(
            lambda: DatagramEndpointInterface(self.messageHandler),
            local_addr=(self.address, self.port)
        )

        self.transport = transport
        print('CommandsServer - Running on', self.address, self.port)

    def stop(self):
        if self.transport:
            self.transport.close()

    def messageHandler(self, message, senderAddress):
        pass
