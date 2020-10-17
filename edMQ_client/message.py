import json
from .exception.exception import InvalidValueError


class Message:

    HEADER_START = 'EDMQ/0.1\r\n'
    HEADER_END = '\r\n\r\n'
    CONTENT_DELIMITER = ';'
    DEFAULT_HEADERS = {'Content-Length': 0, 'Content-Type': 'edmq/json', 'Exchange-Type': 'direct'}

    def __init__(self, data, headers=None):
        self.data = self.serialize(data, headers) if headers else self.serialize(data)

    def serialize(self, dict_body, ad_headers=None) -> bytearray:
        body_string = self._convert_body(dict_body)
        payload = self._setup_headers(len(body_string), self.DEFAULT_HEADERS, ad_headers)
        payload.extend(body_string)

        return payload

    @staticmethod
    def _convert_body(body) -> bytearray:
        if isinstance(body, dict):
            return bytearray(json.dumps(body), 'UTF-8')

        raise InvalidValueError('Method only accepts dict as input, for now..')

    def _setup_headers(self, body_length, headers, properties=None) -> bytearray:
        if properties is not None:
            additional_properties = self._stringify_default_headers(properties)
        else:
            additional_properties = ''

        headers['Content-Length'] = body_length
        header = f'{self.HEADER_START}{self._stringify_default_headers(headers)}{additional_properties}{self.HEADER_END}'

        return bytearray(header, 'UTF-8')

    def _stringify_default_headers(self, properties):
        return self.CONTENT_DELIMITER.join(f'{k}:{v}' for k, v in properties.items())
