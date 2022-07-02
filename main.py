import os

from server import run_server

if __name__ == '__main__':
    token = os.environ.get('TOKEN', None) or input("Input your token\n")
    run_server(token=token)
