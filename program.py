import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def get_image():
    image_path = input("Please enter the file path of the image you want to load: ").strip().strip('"')
    try:
        make_histogram(Image.open(image_path)) 
    except FileNotFoundError as e:
       raise FileNotFoundError("File does not exist. " + str(e))
    except ValueError as e:
        raise ValueError("Unsupported image format. Please use one of the supported formats. " + str(e))
    except Exception as e:
        raise Exception("Error was occurred while uploading the image. " + str(e))

def make_histogram(image):
    image_np = np.array(image)

    plt.figure(figsize=(10, 6))

    for index, c in enumerate(['red','green', 'blue']):
        hist, bins = np.histogram(image_np[:,:,index], bins=256, range=(0, 256))
        plt.plot(bins[:-1], hist, color=c, alpha=0.6, label=c)

    plt.title('RGB Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

get_image()
