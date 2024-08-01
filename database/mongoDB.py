from pymongo import MongoClient, errors
from os import getenv
from dotenv import load_dotenv

load_dotenv()

uri = getenv("MONGODB_URI")

try:
    db = MongoClient(uri)

except errors.ConnectionFailure as conn_err:
    raise RuntimeError(f"Connection error: {conn_err}") from conn_err

except errors.PyMongoError as e:
    raise RuntimeError(f"Pymongo error: {e}") from e