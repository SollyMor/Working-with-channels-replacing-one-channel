# CV-1-18 
# RGB Channel Switcher (OpenCV)

A tiny script that swaps the Red and Green channels of an image using OpenCV, then displays the result.

## Requirements
- Python 3.8+
- OpenCV (opencv-python)
- numpy
- matplotlib

Install:
pip install opencv-python numpy matplotlib

## How it works
- Splits the input image into Blue, Green, Red channels
- Swaps Red and Green
- Merges channels back and displays the image

## Usage
1. Place cat.jpg in the same directory.
2. Run:
python main.py

## Notes
- OpenCV reads images in BGR order. Swapping R and G is equivalent to swapping channels 2 and 1.
- If no window appears on Windows, ensure you’re running in a desktop session (not headless) and that cv2.waitKey(0) is reached.

## Example
![Пример](./cat1.jpg)
![Результат](./cat1_switched.jpg)

