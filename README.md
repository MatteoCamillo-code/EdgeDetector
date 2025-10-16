# Edge Detector

## Description
Edge Detector is a Python-based project for detecting edges in images. It uses image processing techniques to identify and highlight the boundaries within an image. This project is useful for applications in computer vision, object detection, and image analysis.

## Features
- Load and process images in various formats.
- Apply edge detection algorithms such as Sobel, Canny, or Prewitt.
- Save and visualize the processed images with detected edges.

## Requirements
- Python 3.7 or higher
- Required libraries:
    - OpenCV
    - NumPy
    - Matplotlib (optional, for visualization)

## Installation
1. Clone the repository:
     ```
     git clone https://github.com/yourusername/EdgeDetector.git
     ```
2. Navigate to the project directory:
     ```
     cd EdgeDetector
     ```
3. Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```

## Usage
1. Place the image you want to process in the `images` folder.
2. Run the script:
     ```
     python edge_detector.py --image images/sample.jpg --method canny
     ```
     Replace `sample.jpg` with your image file and `canny` with the desired edge detection method (`sobel`, `prewitt`, etc.).

3. The processed image with detected edges will be saved in the `output` folder.

## Example
Input Image:
![Input Image](images/sample.jpg)

Output Image:
![Output Image](output/sample_edges.jpg)

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the MIT License. See the LICENSE file for details.