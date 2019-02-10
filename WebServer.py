from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = ""
        with open("C:\\Users\\Maria\\Desktop\\HTTPClientServer\\VacationPlanner.html") as f:
            for line in f:
                message = message + line
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        parsed_path = parse.urlparse(self.path)
        message_parts = [
            'CLIENT VALUES:',
                'client_address={} ({})'.format(self.client_address, self.address_string()),
                'command={}'.format(self.command),
                'path={}'.format(self.path),
                'real path={}'.format(parsed_path.path),
                'query={}'.format(parsed_path.query),
                'request_version={}'.format(self.request_version),
            '',
            'SERVER VALUES:',
                'server_version={}'.format(self.server_version),
                'sys_version={}'.format(self.sys_version),
                'protocol_version={}'.format(self.protocol_version),
            '',
            'HEADERS RECEIVED:',
        ]
        for name, value in sorted(self.headers.items()):
            message_parts.append('{}={}'.format(name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        print(message)
        return


def run():
    print('starting server...')

    # Server settings
    server_address = ('127.0.0.1', 8899)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()