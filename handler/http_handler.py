# -*- encoding=utf-8 -*-

import time
from urllib.parse import unquote
from handler.base_http_handler import BaseHTTPRequestHandler

class HTTPRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, server, request, client_address):
        BaseHTTPRequestHandler.__init__(self, server, request, client_address)

    def do_GET(self):
        if self.path != "/now":
            self.write_error(404)
            self.send()
        else:
            msg = str(time.time())
            self.write_response(200, 'Success')
            self.write_header('Content-Length', len(msg))
            self.end_headers()
            self.write_content(msg)

    def do_POST(self):
        if self.path != "/ping":
            self.write_error(404)
            self.send()
        else:
            # 从body取出数据
            body = unquote(self.body).split("&")
            name = ""
            for para in body:
                if "name" in para:
                    name = para.split("=")[1]
            msg = "Hello, " + name
            # 组成应答报文
            self.write_response(200, 'Success')
            self.write_header('Content-Length', len(msg))
            self.end_headers()
            self.write_content(msg)
