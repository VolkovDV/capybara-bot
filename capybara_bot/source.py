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
    if no_credentials:
        return pymongo.MongoClient(f"mongodb://{host}:{port}/")
    return pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")


def _gridfs_put(local_path: str, gridfs: GridFS) -> None:
    for file in os.listdir(local_path):
        with open(os.path.join(local_path, file), 'rb') as f:
            contents = f.read()
            gridfs.put(contents, filename=str(file))


def upload_pictures():
    mongo_client = auth_mongo()
    capybaras_db = mongo_client[CAPYBARAS_DB]

    fs = GridFS(capybaras_db)

    _gridfs_put(RESOURCES_PATH, fs)
