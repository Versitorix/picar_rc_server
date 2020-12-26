import asyncio

from lib.datagramEndpointInterface import DatagramEndpointInterface
from lib.network_objects.defaultCommand import DefaultCommand
from lib.network_objects.cameraCommand import CameraCommand
from lib.settings import SETTINGS
from lib.controls.camera import Camera


class CommandsServer:
    def __init__(self):
        self.address = SETTINGS.server_ip
        self.port = SETTINGS.commands_port
        self.transport = None
        self.cameraControls = Camera()

    async def start(self):
        loop = asyncio.get_running_loop()

        transport, protocol = await loop.create_datagram_endpoint(
            lambda: DatagramEndpointInterface(self.message_handler),
            local_addr=(self.address, self.port)
        )

        self.cameraControls.ready()

        self.transport = transport
        print('CommandsServer - Running on', self.address, self.port)

    def stop(self):
        if self.transport:
            self.transport.close()

    def message_handler(self, message, sender_address):
        command_type = DefaultCommand.get_message_type(message)

        if command_type == CameraCommand.type:
            camera_command = CameraCommand.from_string(message)
            if camera_command.movement_type == 'tilt':
                self.cameraControls.to_position(
                    self.cameraControls.current_pan,
                    camera_command.movement_value,
                    5,
                )
        pass
