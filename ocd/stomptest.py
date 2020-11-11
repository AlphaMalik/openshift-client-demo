import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

hosts = [('172.28.134.60', 30613)]

conn = stomp.Connection(host_and_ports=hosts,auto_content_length=False)
conn.set_listener('', MyListener())
conn.connect(wait=True)
conn.subscribe(destination="/queue/anisnotifications", id=1, ack="auto")

conn.send(body='This is a python message', destination='anisnotifications')

time.sleep(5)
conn.disconnect()
