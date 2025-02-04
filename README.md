# Image Converter App

A simple graphical user interface (GUI) to convert and resize images using Python and the `PIL` (Pillow) library. This app allows users to select an image, resize it for preview, and convert it to a different format, while also resizing the final saved image.

## Features

- **Image Selection**: Choose an image file from your computer.
- **Preview Size Adjustment**: Set the preview size of the image before conversion.
- **Conversion**: Convert the selected image into a desired format and resize it.
- **Save Image**: Save the converted image with a new size and format.

## Requirements

- **Python 3.x** (Tested on Python 3.7+)
- **Pillow**: Python Imaging Library (PIL) fork
- **python-magic**: Used to detect MIME type of the image files

# Installation

Install Python 3.x: [Download Python](https://www.python.org/downloads/)

Install the required Python libraries:

```bash
pip install pillow python-magic
```

# Usage

1. Run the `image_converter.py` script.
2. In the GUI, click **Select an image** to choose an image file.
3. Set the desired **Preview size** (preview size) and **The size of the saved image** (saved image size).
4. Click **Convert** to convert the image.
5. Choose where to save the converted image and select the desired output format (e.g., `.jpg`, `.png`, `.gif`).
6. The status label will display a success message or an error message if there was an issue.

# Code Explanation

- **File Dialog**: Used to select the input image file and save the converted image.
- **Image Preview**: Displays a resized preview of the image based on the input size.
- **Image Conversion**: Converts the image to a new format and resizes it as per user input.
- **Magic Library**: Validates that the selected file is an image and checks its MIME type.
- **Error Handling**: Provides error messages if the selected file is not an image or if there are issues during saving.

# Troubleshooting

- **File Type Issues**: If the selected file is not an image, the app will display an error message.
- **Unsupported Image Formats**: The app supports a variety of image formats. If the image cannot be saved in the selected format, ensure that you choose a supported output format.
- **Preview Not Displaying**: Ensure that the preview size is entered correctly in the format `width x height` (e.g., `200x200`).

# License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Contact

If you have any questions or need further assistance, feel free to open an issue or reach out directly to the repository owner.
