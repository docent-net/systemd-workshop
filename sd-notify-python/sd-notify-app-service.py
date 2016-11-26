#!/usr/bin/python3
# https://github.com/bb4242/sdnotify

from time import sleep
import sdnotify


class App(object):
    def __init__(self):
        self.sdn = sdnotify.SystemdNotifier()

    def start(self):
        # do something specific to app startup
        sleep(2)

        # tell systemd we're ready
        self.sdn.notify("READY=1")

        count = 1
        while True:
            print("Running... {}".format(count))
            self.sdn.notify("STATUS=Count is {}".format(count))
            count += 1
            sleep(2)
            if count == 10:
                break


app = App()
app.start()
