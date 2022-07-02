import pymongo
import os
from gridfs import GridFS
from pathlib import Path

from vars import MONGO_HOST, MONGO_PASSWORD, MONGO_PORT, MONGO_USER, CAPYBARAS_DB


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


def gridfs_put(local_path: str, gridfs: GridFS) -> None:
    for file in os.listdir(local_path):
        with open(os.path.join(local_path, file), 'rb') as f:
            contents = f.read()
            gridfs.put(contents, filename=str(file))


mongo_client = auth_mongo()
capybaras_db = mongo_client[CAPYBARAS_DB]

fs = GridFS(capybaras_db)

resources_path = os.path.join(Path.home(), 'collection')  # your own local path

gridfs_put(resources_path, fs)
