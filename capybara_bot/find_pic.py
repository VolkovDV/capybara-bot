from random import randint

import gridfs
import pymongo

from vars import CAPYBARAS_DB


def get_picture_from_db(mongo_client: pymongo.MongoClient) -> bytes:
    capybaras_db = mongo_client[CAPYBARAS_DB]
    files = []

    for file in capybaras_db['fs.files'].find({}):
        files.append(file['filename'])
    index = randint(0, len(files))
    bucket = gridfs.GridFSBucket(capybaras_db)
    return bucket.open_download_stream_by_name(files[index]).read()
