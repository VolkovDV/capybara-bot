import logging
import pymongo
import os
from gridfs import GridFS

from vars import (
    MONGO_HOST, MONGO_PASSWORD, MONGO_PORT, MONGO_USER, CAPYBARAS_DB, RESOURCES_PATH,
)


def auth_mongo(
        user: str = MONGO_USER,
        password: str = MONGO_PASSWORD,
        host: str = MONGO_HOST,
        port: int = MONGO_PORT,
        no_credentials: bool = False,
) -> pymongo.MongoClient:
    """
    Function for auth with default values
    :param user: mongodb login
    :param password: password
    :param host: hostname
    :param port: port
    :param no_credentials: use auth without user and password
    :return: pymongo.MongoClient instance
    """
    if no_credentials:
        return pymongo.MongoClient(f"mongodb://{host}:{port}/")
    return pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")


def _gridfs_put(local_path: str, gridfs: GridFS) -> None:
    for file in os.listdir(local_path):
        with open(os.path.join(local_path, file), 'rb') as opened_file:
            contents = opened_file.read()
            gridfs.put(contents, filename=file)


def upload_pictures():
    mongo_client = auth_mongo()
    capybaras_db = mongo_client[CAPYBARAS_DB]

    file_system = GridFS(capybaras_db)
    logging.info('start loading data to database')
    _gridfs_put(RESOURCES_PATH, file_system)
    logging.info('data was downloaded successfully')
