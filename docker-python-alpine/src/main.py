import socketserver
from flag import flag

class HashHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(b'Hello world! Here is your flag!\n')
        try:
            flag = flag.encode()
        except:
            pass
        self.request.sendall(flag)

if __name__ == '__main__':
    HOST, PORT = '0.0.0.0', 8080
    with socketserver.ThreadingTCPServer((HOST, PORT), HashHandler) as server:
        server.serve_forever()
            
