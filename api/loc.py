from email import message
from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    # grabs everything past .app in the url
    url_components = parse.urlsplit(self.path)
    # parses into tuple
    query_string_list = parse.parse_qsl(url_components.query)
    #turns tuple into dictionary so it can be accessed with key value pairs
    dict_query_str = dict(query_string_list)
    
  
    
    #separating the queries into variables 
    country = dict_query_str['country']
    capital = dict_query_str['capital']
    
    
    if 'country' in dict_query_str:
      message = f'this has country in it and the country is'
      
    else:
      message = 'this does not'
    
    # output message
    # message = f'the capital of {country} is {capital}'
    #prints the message
    self.wfile.write(message.encode())
    return
  