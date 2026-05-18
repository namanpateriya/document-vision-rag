import fitz  # PyMuPDF

from app.utils.logger import get_logger

logger = get_logger(__name__)


class DocumentExtractor:

    @staticmethod
    def extract_text(file_path: str):

        doc = fitz.open(file_path)

        all_text = []

        for page_num, page in enumerate(doc):

            text = page.get_text()

            if text.strip():
                all_text.append(text)

            logger.info(f"Processed page {page_num + 1}")

        return "\n".join(all_text)
