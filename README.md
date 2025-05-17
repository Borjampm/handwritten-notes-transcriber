# Handwritten Notes to Markdown Converter

## Project Overview

This project aims to build a fully local system that takes an image of handwritten notes and converts it into a structured Markdown file. The system emphasizes privacy, accuracy, and compatibility with macOS systems, particularly the MacBook Air M1.

## Goals

* Convert handwritten notes to digital Markdown format.
* Ensure the process runs entirely offline.
* Maximize OCR accuracy through preprocessing.
* Maintain extensibility for different handwriting styles and layouts.

## Functional Requirements

* Accept image input (`.jpg`, `.png`, `.jpeg`).
* Preprocess image to enhance text clarity.
* Extract text using OCR tuned for handwriting.
* Parse OCR output into structured Markdown syntax.
* Export `.md` files with optional frontmatter.

## Non-Functional Requirements

* Run locally without internet access.
* Perform efficiently on a MacBook Air M1.
* Modular design for future enhancements (GUI, retraining, multi-page input).

## Tech Stack

### Language

* Python 3.12+

### Image Preprocessing

* OpenCV
* Pillow
* (Optional) scikit-image

### OCR

* Default: PaddleOCR (for higher accuracy)
* Optional: Tesseract OCR (via pytesseract)
* Optional: Kraken (for historical or messy handwriting)

### Markdown Conversion

* Custom Python parser using regex and formatting rules
* `markdown` Python library (optional)

### Local Runtime

* Homebrew (to install Tesseract)
* pyenv (to manage Python versions)
* virtualenv or Poetry (for dependency management)

## System Architecture

1. **Image Handler**

   * Loads image(s) from specified directory or GUI.
   * Converts to grayscale.
   * Applies noise reduction, thresholding, and skew correction.

2. **OCR Module**

   * Applies chosen OCR engine to the processed image.

3. **Markdown Formatter**

   * Applies text structure parsing.
   * Outputs Markdown file with detected headings, lists, and paragraphs.

4. **Output Module**

   * Saves the result as `.md` in a target directory.

## Optional Extensions

* GUI with Streamlit or Tkinter
* Live folder monitoring with Watchdog
* Model fine-tuning for improved handwriting accuracy

## Security and Privacy

* Entire system operates offline
* No data is sent or stored externally
* Temporary files can be auto-deleted post-processing

## Status

* [ ] Environment Setup
* [ ] OCR Baseline with Tesseract
* [ ] Image Preprocessing Pipeline
* [ ] Markdown Formatter Implementation
* [ ] CLI Wrapper
* [ ] Optional GUI

## License

MIT License (or internal use only, to be defined based on distribution goals)

## Author

\[Your Name Here]

---

For setup, usage, and contribution guidelines, refer to the `README.md` (to be created).
