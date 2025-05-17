from PIL import Image
from PIL import ImageFilter

class ImageHandler:
    def __init__(self, path: str):
        self.path = path
        self._image = self._build_image()

    def get_image(self) -> Image.Image:
        """
        Returns the image.
        """
        return self._image

    def preprocess_image(self):
        """
        Preprocesses the image.
        """
        self._to_grayscale()
        self._apply_thresholding()

    def show_image(self):
        """
        Shows the image.
        """
        self._image.show()

    def save_image(self, path: str):
        """
        Saves the image.
        """
        self._image.save(path)

    def _build_image(self) -> Image.Image:
        """
        Loads and returns the image as a Pillow Image object.
        """
        return Image.open(self.path)

    def _to_grayscale(self):
        """
        Transforms the image to grayscale.
        """
        self._image = self._image.convert("L")

    def _apply_noise_reduction(self):
        """
        Applies noise reduction to the image.
        """
        self._image = self._image.filter(ImageFilter.GaussianBlur(radius=2))

    def _apply_thresholding(self):
        """
        Applies thresholding to the image.
        """
        self._image = self._image.point(lambda x: 255 if x > 128 else 0, "1")

    def _apply_skew_correction(self):
        """
        Applies skew correction to the image.
        """
        self._image = self._image.transform(self._image.size, Image.AFFINE, (1, 0.5, 0, 0, 1, 0))

