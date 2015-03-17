
import time
import uinput

from http.server import BaseHTTPRequestHandler,HTTPServer

hostName = "localhost"
hostPort = 9000

events = (
	uinput.KEY_A,
	uinput.KEY_B,
	uinput.KEY_C,
	uinput.KEY_1,
	uinput.KEY_5
)

lookups = { 
	'a': uinput.KEY_A,
	'b': uinput.KEY_B,
	'c': uinput.KEY_C,
	'5': uinput.KEY_1,
	'5': uinput.KEY_5
}

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
		
        print   ('Get request received')
        with uinput.Device(events) as device:
            time.sleep(1)
            device.emit_click(uinput.KEY_5);
        
        print('sent key!')
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        return

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
