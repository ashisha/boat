#!/usr/bin/env python
import sys
import socket
import BaseHTTPServer
import pyqrcode
import os
import shutil

class BoatHTTPServer(BaseHTTPServer.HTTPServer):
    def __init__(self, server_address, server_handler, timeout, maxrequests):
        BaseHTTPServer.HTTPServer.__init__(self, server_address, server_handler)
        self.run = True
        self.requests_served = 0
        self.max_requests = maxrequests
        self.timeout = timeout #secs

    def handle_timeout(self):
        self.run = False

class BoatHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    server_version = 'Boat/0.1'

    def do_GET(s):
        s.server.requests_served = s.server.requests_served + 1

        if (s.server.requests_served > s.server.max_requests):
            s.server.run = False

        if (s.path != '/'):
            return

        try:
            with open(s._file, 'rb') as phile:
                s.send_response(200)
                s.send_header('Content-Type', 'application/octet-stream')
                s.send_header('Content-Disposition', 'attachment;filename="%s"' % os.path.basename(s._file))
                fs = os.fstat(phile.fileno())
                s.send_header("Content-Length", str(fs[6]))
                s.end_headers()

                shutil.copyfileobj(phile, s.wfile)

        except EnvironmentError:
            s.send_error(404, "File [%s] not found" % s._file)

class Boat:
    def __init__(self, filename, qr_code, timeout, maxrequests):
        self.__filename = filename
        self.__qr = qr_code
        self.__timeout = timeout
        self.__maxrequests = maxrequests

    def run(self):
        host = socket.gethostbyname(socket.getfqdn())
        port = 0 # Let OS decide the port

        BoatHTTPHandler._file = self.__filename
        httpd = BoatHTTPServer((host, port), BoatHTTPHandler, self.__timeout, self.__maxrequests)

        self.console_out(host, httpd.server_port)
 
        try:
            # double fork?
            pid = os.fork()
            if pid > 0:
                # in parent
                return 0
            else:
                si = file('/dev/null', 'r')
                so = file('/dev/null', 'a+')
                se = file('/dev/null', 'a+', 0)
                os.dup2(si.fileno(), sys.stdin.fileno())
                os.dup2(so.fileno(), sys.stdout.fileno())
                os.dup2(se.fileno(), sys.stderr.fileno())

        except OSError:
            print("Fork failed")
            return -1

        try:
            # server_forever does not respects timeout
            # hence resort to while loop
            while httpd.run:
                httpd.handle_request()
        except KeyboardInterrupt:
            # should not happen
            pass

        httpd.server_close()

    def console_out(self, host, port):
        print "Boat serving [%s] at http://%s:%s" % (self.__filename, host, port)
        if (self.__qr):
            try:
                import pyqrcode
                qr = pyqrcode.create('http://%s:%s' % (host, port))
                print qr.terminal()
            except:
                print "Failed to generate QR code!"

def main():
    import argparse

    parser = argparse.ArgumentParser(description = "boat: Transfer files over HTTP easily",
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file')
    parser.add_argument('-q', '--qr', default = False, action = 'store_true', help = "display a QR code of the URL")
    parser.add_argument('-t', '--timeout', type = int, default = 30, help = "close the server after t secs of inactivity")
    parser.add_argument('-m', '--max', type = int, default = 10, help = "close the server after m requests are served")
    args = parser.parse_args()

    boat = Boat(args.file, args.qr, args.timeout, args.max)
    return boat.run()

if __name__ == '__main__':
    sys.exit(main())

