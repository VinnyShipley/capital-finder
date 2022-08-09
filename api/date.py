from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    
    url_components = parse.urlsplit(self.path)
    
    message = str(url_components)
    #message = f'the capital of {country} is {capital}'
    self.wfile.write(message.encode())
    return
  