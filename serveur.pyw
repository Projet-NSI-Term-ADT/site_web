# -*- coding: utf-8 -*-
# à mettre dans chacun des scripts :
# import sys
# sys.stdout.reconfigure(encoding='utf-8')
import http.server
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
import webbrowser

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler

PORT = 8888
server_address = ("", PORT)

handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
webbrowser.open_new_tab(f"http://localhost:{str(PORT)}/index_login.py")
httpd = server(server_address, handler)
httpd.serve_forever()