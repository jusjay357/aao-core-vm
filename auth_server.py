import http.server
import socketserver
import base64

USERNAME = "aaoadmin"
PASSWORD = "Tooblessed88!!"

class AuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"AAO Dashboard\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        auth_header = self.headers.get('Authorization')
        expected = "Basic " + base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
        if auth_header == expected:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.do_AUTHHEAD()
            self.wfile.write(b'Authentication failed.')

PORT = 8800
with socketserver.TCPServer(("", PORT), AuthHandler) as httpd:
    print(f"Serving with auth on port {PORT}")
    httpd.serve_forever()
