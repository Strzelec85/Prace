import http.server

s = http.server.HTTPServer(('0.0.0.0', 7999), http.server.SimpleHTTPRequestHandler)
s.serve_forever()

