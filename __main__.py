"""Application entry point."""
import asyncio

from lib.commandsServer import CommandsServer

commands_server = None


async def main():
    commands_server = CommandsServer()
    await commands_server.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    if commands_server:
        commands_server.stop()
