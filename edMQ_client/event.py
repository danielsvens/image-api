from edMQ_client.message import Message


class EdMQEvent:

    def __init__(self, exchange, routing_key):
        self.headers = {'Exchange': exchange, 'Routing-Key': routing_key}

    def __call__(self, func):
        def wrapper(*args):
            f = func(*args)
            message = Message(f, self.headers)

            # Send message.

            return 'Queued.'

        return wrapper
