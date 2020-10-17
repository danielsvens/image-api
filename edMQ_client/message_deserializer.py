import json


class MessageDeserializer:

    def __init__(self, headers, body):
        self.headers = self._deserialize_headers(headers)
        self.body = self._deserialize_body(body)

    @staticmethod
    def _deserialize_headers(headers) -> dict:
        if isinstance(headers, bytes):
            header_list = str(headers, 'UTF-8').split(';')
            return {k: v for k, v in [h.split(':') for h in header_list]}

        if isinstance(headers, list):
            return {k: v for k, v in [h.split(':') for h in headers]}

    @staticmethod
    def _deserialize_body(body) -> dict:
        if isinstance(body, bytes):
            return json.loads(str(body, 'UTF-8'))
