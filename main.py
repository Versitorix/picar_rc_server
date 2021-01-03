"""Application entry point."""
import asyncio

import lib.stream as stream
from modules.commandsServer import CommandsServer


async def main():
    commands_server = CommandsServer()
    await commands_server.start()
    stream.start()

    return commands_server


loop = asyncio.get_event_loop()
server = loop.run_until_complete(main())

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.stop()
    stream.stop()

