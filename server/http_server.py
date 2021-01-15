# -*- encoding=utf-8 -*-

from server.base_http_server import BaseHTTPServer

class HTTPServer(BaseHTTPServer):

    def __init__(self, server_address, handler_class):
        self.server_name = 'MyHTTPServer'
        self.version = 'v0.1'
        BaseHTTPServer.__init__(self, server_address, handler_class)


if __name__ == '__main__':
    from handler.http_handler import HTTPRequestHandler

    HTTPServer(('127.0.0.1', 8000), HTTPRequestHandler).serve_forever()
