import os

DATA_PATH = os.getenv(
    "DATA_PATH",
    "data"
)

CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", 500)
)
