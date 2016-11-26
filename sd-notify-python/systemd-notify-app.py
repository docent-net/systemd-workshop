#!/usr/bin/python3
# https://pypi.python.org/pypi/systemd/

from time import sleep
from systemd.daemon import notify, Notification


class App(object):
    def __init__(self):
        pass

    def start(self):
        # do something specific to app startup
        sleep(2)

        # tell systemd we're ready
        notify(Notification.READY)

        count = 1
        while True:
            print("Running... {}".format(count))
            notify(Notification.STATUS, "STATUS=Count is {}".format(count))
            count += 1
            sleep(2)
            if count == 10:
                break

            # Send stopping
            # notify(Notification.STOPPING)


app = App()
app.start()
