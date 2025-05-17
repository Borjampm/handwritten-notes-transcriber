from image.image_handler import ImageHandler
from ocr.ocr_handler import OCRHandler

if __name__ == "__main__":
    test_image_path = "images/test.jpeg"
    test_image = ImageHandler(test_image_path)
    test_image.preprocess_image()
    preprocessed_image_path = "results/test_preprocessed.jpeg"
    test_image.save_image(preprocessed_image_path)

    ocr_handler = OCRHandler()
    print(ocr_handler.extract_text(preprocessed_image_path))


