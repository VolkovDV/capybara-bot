"""
vars for setting enviroment, connections, etc
"""
from os.path import join
from pathlib import Path

MONGO_HOST = 'mongo'
MONGO_PORT = '27017'
MONGO_PASSWORD = 'example'
MONGO_USER = 'root'

CAPYBARAS_DB = 'capybaras'

RESOURCES_PATH = join(Path.home(), 'collection')  # your own local path
