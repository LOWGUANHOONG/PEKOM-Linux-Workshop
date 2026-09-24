from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        user_agent = self.headers.get('User-Agent', '')
        if 'FlagBrowser' in user_agent:
            body = (
                "<html><body style='font-family:sans-serif; text-align:center; padding-top:50px;'>"
                "<h1 style='color:green;'>Access Granted!</h1>"
                "<p>Flag: <b>FLAG{http_h3ad3rs_t3ll_all}</b></p>"
                "</body></html>"
            ).encode('utf-8')
        else:
            body = (
                "<html><body style='font-family:sans-serif; text-align:center; padding-top:50px;'>"
                "<h1 style='color:red;'>Access Denied</h1>"
                "<p>Forbidden: Access restricted strictly to users running <code>FlagBrowser</code>.</p>"
                "</body></html>"
            ).encode('utf-8')
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == '__main__':
    print(f"[*] Challenge server running on http://127.0.0.1:{PORT}")
    print("[*] Press Ctrl+C to stop.")
    HTTPServer(('127.0.0.1', PORT), Handler).serve_forever()
