import os
from pathlib import Path

from app.utils.logger import get_logger

logger = get_logger(__name__)


class DocumentLoader:

    @staticmethod
    def load(file_path: str):

        if not os.path.exists(file_path):
            raise ValueError(
                f"File not found: {file_path}"
            )

        ext = Path(file_path).suffix.lower()

        if ext != ".pdf":
            raise ValueError(
                "Only PDF supported in Step 1"
            )

        logger.info(f"Loaded file: {file_path}")

        return file_path
