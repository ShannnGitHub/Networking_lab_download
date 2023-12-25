import http.server
import socketserver

# Set the directory to the location of your files
directory = '.'

# Choose a free port, e.g., 8000
port = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Serving on port {port}")
    print(f"Open your browser and go to http://localhost:{port}/index.html")
    httpd.serve_forever()
