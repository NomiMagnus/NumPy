# NumPy - RGB Histogram
View the RBG diagram of an image using `NumPy` library.

This project demonstrates how to generate an RGB histogram from an image using Python.
The histogram represents the frequency distribution of pixel intensities for each color channel (Red, Green, Blue) in the image.

## Prerequisites
Before running the code, ensure you have Python installed on your system. The required libraries are specified in the requirements.txt file.

## Installation
1. Clone the repository:
   ```cmd
    git clone https://github.com/NomiMagnus/NumPy.git
    cd numpy
   ```
2. Install the required libraries:
    ```python
    pip install -r requirements.txt
    ```

## Usage
1. Run the script:
    ```python
    python program.py
    ```
2. When prompted to enter the file path of the image, enter the full path of the file. Make sure that the path:
    - Uses forward slashes (/) instead of backslashes (\), for example:
        `C:/Users/User/Desktop/numpy/pic1.png`
    - Does not include extra spaces or double quotes at the beginning or end of the path.
3. If the image is loaded successfully, an RGB histogram of the image will be displayed.

## Docker
To run the project using Docker, follow these steps:
1. Make sure you have Docker installed on your computer.
2. Build the Docker image:
   ```docker
   docker build -t <IMAGE_NAME>
   ```
3. Run the Docker container:
   ```docker
   docker run -it --rm <IMAGE_NAME>
   ```

program.py - is the main script that generates the RGB histogram.
requirements.txt - the required libraries for this project.


### Sources
The following sources were used to gather information for this project:
- NumPy Documentation
- Geeks for Geeks
- W3Schools Tutorials
- NumPy Official Website
- PyPI - NumPy
- Stack Overflow
