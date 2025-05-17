from paddleocr import PaddleOCR
from typing import Optional, List, Tuple, Union
from PIL import Image
import numpy as np

class OCRHandler:
    """
    OCRHandler wraps the PaddleOCR engine for handwritten and printed text recognition.
    Designed for modularity and future extensibility (Tesseract, Kraken, etc.).
    """
    def __init__(self, lang: str = 'en', use_angle_cls: bool = True, ocr_version: str = 'PP-OCRv4', **kwargs):
        """
        Initialize the OCR engine.
        Args:
            lang (str): Language code for OCR (default: 'en').
            use_angle_cls (bool): Whether to use angle classification.
            ocr_version (str): Version of the OCR model to use.
            **kwargs: Additional PaddleOCR parameters.
        """
        self.lang = lang
        self.ocr = PaddleOCR(
            use_angle_cls=use_angle_cls,
            lang=lang,
            ocr_version=ocr_version,
            **kwargs
        )

    def recognize(self, image: Union[str, Image.Image, np.ndarray], cls: bool = True) -> List[Tuple[List, Tuple[str, float]]]:
        """
        Recognize text from an image file path, Pillow Image, or numpy array.
        Args:
            image (str | Image.Image | np.ndarray): Image file path or image object.
            cls (bool): Whether to use angle classification during recognition.
        Returns:
            List of tuples: Each tuple contains bounding box and (text, confidence).
        """
        # Convert Pillow Image to numpy array if needed
        if isinstance(image, Image.Image):
            image = np.array(image)
        try:
            result = self.ocr.ocr(image, cls=cls)
            # result: List[List[Tuple[box, (text, score)]]]
            return result[0] if result else []
        except Exception as e:
            print(f"OCR failed: {e}")
            return []

    def extract_text(self, image: Union[str, Image.Image, np.ndarray], join: bool = True) -> str:
        """
        Extract recognized text as a single string.
        Args:
            image (str | Image.Image | np.ndarray): Image file path or image object.
            join (bool): If True, join lines with newlines.
        Returns:
            str: Recognized text.
        """
        results = self.recognize(image)
        lines = [text for _, (text, score) in results]
        return '\n'.join(lines) if join else lines
