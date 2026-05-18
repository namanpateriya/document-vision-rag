import logging
import uuid


def get_logger(name: str):

    if not logging.getLogger().hasHandlers():

        logging.basicConfig(
            level=logging.INFO,
            format=(
                "%(asctime)s | "
                "%(levelname)s | "
                "%(name)s | "
                "%(message)s"
            )
        )

    return logging.getLogger(name)


def get_request_id():

    return str(uuid.uuid4())[:8]
