from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os
import json
from threading import Thread
from datetime import datetime
from hashlib import md5


class MyServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def process_file(self, file_path):
        create_date = str(datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%m/%d/%Y, %H:%M:%S"))
        modify_date = str(datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%m/%d/%Y, %H:%M:%S"))
        with open(file_path, "rb") as file_content:
            md5_code = md5(b'file_content').hexdigest()

        file_metadata = {
            "name": os.path.basename(file_path).split('//')[-1],
            "size(bytes)": os.stat(file_path).st_size,
            "last_modified_date": modify_date,
            "creation_date": create_date,
            "md5": md5_code
        }
        print(json.dumps(file_metadata, indent=1))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        file_path = json.loads(post_data.decode('utf-8'))['file']
        Thread(target=self.process_file, args=(file_path,)).start()
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=MyServer, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


run()
