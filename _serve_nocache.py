#!/usr/bin/env python3
"""Dev server that always sends Cache-Control: no-store, so a normal reload
in the browser can never show a stale copy of band.html/index.html while
we're actively editing them. Same port/usage as `python3 -m http.server 8123`."""
import http.server
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8123

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    http.server.test(HandlerClass=NoCacheHandler, port=PORT, bind='127.0.0.1')
