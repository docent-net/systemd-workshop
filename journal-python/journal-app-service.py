#!/usr/bin/python3
# See https://www.freedesktop.org/software/systemd/python-systemd/journal.html

import logging
import uuid
from time import sleep
from systemd.journal import JournalHandler

class App(object):
    def __init__(self):
        self.create_logger()

    def start(self):
        while True:
            print(1)
            message_uuid = uuid.uuid4() # Debian Random generator XD
            self.log.warning(
                "Message with ID %s",
                message_uuid,
                extra={'MESSAGE_ID': message_uuid}
            )
            sleep(3)

    def create_logger(self):
        self.log = logging.getLogger('app_logger')
        self.log.propagate = False
        self.log.setLevel(logging.DEBUG)
        self.log.addHandler(JournalHandler())

app = App()
app.start()
