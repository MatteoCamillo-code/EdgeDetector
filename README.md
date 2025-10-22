# Edge Detector

Small Python project to perform basic image processing (grayscale, blur, edge detection) using simple convolution filters.

## Contents
- Core script: [main.py](main.py) — orchestrates loading, processing and saving images.
- Image I/O: [`image_holder.ImageHolder`](image_holder.py) — loads images and provides grayscale conversion.
- Convolution engine: [`convolutor.Convolutor`](convolutor.py) — applies filters to 2D image arrays.
- Filters: [`filters.get_filter`](filters.py) and predefined kernels in [filters.py](filters.py).
- Example assets: [assets/](assets/) (base, gray, processed).

## Features
- Convert color images to grayscale via [`image_holder.ImageHolder`](image_holder.py).
- Apply Gaussian blur and edge-detection filters (Sobel, Prewitt, Laplacian, etc.) via [`convolutor.Convolutor`](convolutor.py) and [`filters.get_filter`](filters.py).
- Saves outputs to `assets/gray/` and `assets/processed/`.

## Requirements
- Python 3.7+
- Pillow
- NumPy

Install dependencies:
```sh
pip install pillow numpy
```

## Quick start
1. Edit the `image_name` variable in [main.py](main.py) or replace the image in `assets/base/`.
2. Run:
```sh
python main.py
```
Outputs:
- Grayscale: `assets/gray/{image_name}_gray.jpeg`
- Blurred: `assets/processed/{image_name}_blurred.jpeg`
- Edges: `assets/processed/{image_name}_edge.jpeg`

## Important symbols
- [`image_holder.ImageHolder`](image_holder.py) — loader + to_gray_scale().
- [`convolutor.Convolutor`](convolutor.py) — set_filter(), convolution().
- [`filters.get_filter`](filters.py) — fetch named filters (e.g. `"gaussian_3x3"`, `"sobel_x"`, `"backward"`).

## Example usage (from code)
Processing pipeline in [main.py](main.py):
1. Load image with [`image_holder.ImageHolder`](image_holder.py).
2. Convert to grayscale.
3. Blur using `gaussian_3x3` (via [`filters.get_filter`](filters.py)).
4. Detect edges using a 1D/2D filter via [`convolutor.Convolutor`](convolutor.py).

## Notes & Improvements
- Current convolution expects 2D grayscale arrays; extend to handle multi-channel images if needed.
- Border handling and filter shapes can be improved for 1D filters.
- Add CLI options to select input image and filter parameters.