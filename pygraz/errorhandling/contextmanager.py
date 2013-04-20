'''
Example context manager to be used together with the ``with`` statement.
'''
import socket


class SocketClient():
    '''Provide a ``socket`` and automatically close it when done.'''
    def __init__(self, host, port):
        self.socket = socket.create_connection((host, port))

    def __enter__(self):
        '''Value ``with`` statement should assign to its target variable.'''
        return self

    def __exit__(self, type, value, traceback):
        '''Release resources acquired by `__init__()`.'''
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()


if __name__ == '__main__':
    # Example for a working connection.
    with SocketClient('www.python.org', 80) as pythonOrg:
        pythonOrg.socket.sendall(
            'GET /index.html HTTP/1.0\n'
            + 'Host: www.python.org\n'
            + '\n')
        reply = pythonOrg.socket.recv(64)
    print('data obtained: %r...' % reply)

    # Example for a failed connection.
    hostname = 'no.such.host'
    try:
        with SocketClient(hostname, 80) as pythonOrg:
            assert False, 'connection must fail'
    except socket.error as error:
        print('cannot connect to %s: %s' % (hostname, error))
