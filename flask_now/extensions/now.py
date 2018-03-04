from .base import BaseSimpleExtension, BaseMvcExtension
import os
import base64


class NowSimpleExtension(BaseSimpleExtension):
    def __init__(self):
        super().__init__()

    def config(self):
        random_bytes = os.urandom(64)
        token = base64.b64encode(random_bytes).decode('utf-8')
        write_this = ['DEBUG=True',
                      'SECRET_KEY={}{}{}'.format('"', token, '"'),
                      'SERVER_NAME="127.0.0.1:5000"']
        super().writer(self.config_path, "a+", write_this)


class NowMvcExtension(BaseMvcExtension):
    def __init__(self):
        super().__init__()

    def config(self):
        random_bytes = os.urandom(64)
        token = base64.b64encode(random_bytes).decode('utf-8')
        write_this = ['DEBUG=True',
                      'SECRET_KEY={}{}{}'.format('"', token, '"'),
                      'SERVER_NAME="127.0.0.1:5000"']
        super().writer(self.config_path, "a+", write_this)

