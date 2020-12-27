from picar.front_wheels import Front_Wheels
from picar.back_wheels import Back_Wheels
import asyncio
import picar


from lib.datagramEndpointInterface import DatagramEndpointInterface
from lib.network_objects.defaultCommand import DefaultCommand
from lib.network_objects.cameraCommand import CameraCommand
from lib.network_objects.backWheelCommand import BackWheelCommand
from lib.network_objects.frontWheelCommand import FrontWheelCommand
from lib.cancellationToken import CancellationToken
from lib.settings import SETTINGS
from lib.controls.camera import Camera


class CommandsServer:
    def __init__(self):
        self.address = SETTINGS.server_ip
        self.port = SETTINGS.commands_port
        self.transport = None
        self.camera_controls = Camera(debug=False, db='./lib/controls/config')
        self.back_wheels = Back_Wheels(debug=False, db='./lib/controls/config')
        self.front_wheels = Front_Wheels(debug=False, db='./lib/controls/config')

        self.camera_task = None
        self.camera_task_token = None

    async def start(self):
        loop = asyncio.get_running_loop()

        transport, protocol = await loop.create_datagram_endpoint(
            lambda: DatagramEndpointInterface(self.message_handler),
            local_addr=(self.address, self.port)
        )

        picar.setup()
        self.camera_controls.ready()
        self.back_wheels.ready()
        self.front_wheels.ready()
        self.transport = transport
        print('CommandsServer - Running on', self.address, self.port)

    def stop(self):
        if self.transport:
            self.transport.close()

    def message_handler(self, message, sender_address):
        command_type = DefaultCommand.get_message_type(message)

        if command_type == CameraCommand.type:
            camera_command = CameraCommand.from_string(message)
            if camera_command.movement_type == 'initial':
                self.camera_controls.ready()
            elif camera_command.movement_type == 'tilt_down':
                self.camera_controls.turn_down(camera_command.movement_value)
            elif camera_command.movement_type == 'tilt_up':
                self.camera_controls.turn_up(camera_command.movement_value)
            elif camera_command.movement_type == 'pan_left':
                self.camera_controls.turn_left(camera_command.movement_value)
            elif camera_command.movement_type == 'pan_right':
                self.camera_controls.turn_right(camera_command.movement_value)
            elif camera_command.movement_type == 'set_position':
                if self.camera_task:
                    self.camera_task.cancel()
                    self.camera_task_token.cancel()

                self.camera_task_token = CancellationToken()
                self.camera_task = asyncio.create_task(self.camera_controls.to_position(
                    expect_pan=camera_command.movement_value[0],
                    expect_tilt=camera_command.movement_value[1],
                    delay=0,
                    cancellation_token=self.camera_task_token,
                ))
        elif command_type == BackWheelCommand.type:
            wheel_command = BackWheelCommand.from_string(message)

            if wheel_command.action == 'stop':
                self.back_wheels.stop()
            elif wheel_command.action == 'forward':
                self.back_wheels.speed = wheel_command.action_value
                self.back_wheels.forward()
            elif wheel_command.action == 'backward':
                self.back_wheels.speed = wheel_command.action_value
                self.back_wheels.backward()
            elif wheel_command.action == 'set_speed':
                self.back_wheels.speed = wheel_command.action_value
        elif command_type == FrontWheelCommand.type:
            wheel_command = FrontWheelCommand.from_string(message)

            if wheel_command.action == 'initial':
                self.front_wheels.ready()
            elif wheel_command.action == 'turn':
                self.front_wheels.turn(wheel_command.action_value)
