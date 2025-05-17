from image_handler.image_handler import ImageHandler

if __name__ == "__main__":
    test_image_path = "images/test.jpeg"
    test_image = ImageHandler(test_image_path)
    test_image.preprocess_image()
    test_image.save_image("results/test_preprocessed.jpeg")
