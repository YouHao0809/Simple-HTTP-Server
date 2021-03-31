# Simple HTTP Server

A simple http server on top of TCP protocol

实现一个简易的 Web Server，提供两个 HTTP 接口：

1. POST /ping
接受 body 参数 name，返回 200 状态码，原样输出 name

2. GET /now
返回 200 状态码，输出当前时间戳

3. 对于其他访问，返回 404 状态码

要求：仅使用 TCP 相关库、不使用 HTTP 相关库。
提示：除了功能本身的实现以外，考察评估范围还包括边缘情况的处理、代码风格、性能考量等。

实现完毕后的效果类似于：

$ curl -X POST -d 'name=hello%20world' http://127.0.0.1:8000/ping
Hello, hello world

$ curl -X POST -d 'foo=bar&name=hello%20world' http://127.0.0.1:8000/ping
Hello, hello world

$ curl http://127.0.0.1:8000/now         
1610085139

$ curl http://127.0.0.1:8000/xxx
Page not found

