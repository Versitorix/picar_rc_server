from json import loads


class DefaultCommand(object):
    type = 'DefaultCommand'

    @staticmethod
    def get_message_type(message):
        """

        @type message: string
        @return: string
        """
        json_string = loads(message)

        try:
            return json_string['type']
        except KeyError:
            return None

    @staticmethod
    def from_string(json_string):
        """
        Build a CommandObject from a json string.

        @type json_string: string
        """
