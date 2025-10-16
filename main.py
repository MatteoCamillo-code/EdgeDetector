from PIL import Image
from image_holder import ImageHolder
from convolutor import Convolutor
from filters import get_filter
import numpy as np
import os

def main():
    image_name = "racoon"
    image_rel_path = ImageHolder(path=f"assets/{image_name}.jpeg")
    save_image(image_rel_path.get_gray_scale(), f"assets/{image_name}_gray.jpeg")
    filt = get_filter("sobel_x")
    convolutor = Convolutor(filt, 1/2)
    edge = convolutor.convolution(image_rel_path.get_gray_scale())
    save_image(edge, f"assets/{image_name}_edge.jpeg")
    print("Edge detection project!")
    
def save_image(image, path):
    path = os.path.join(os.path.dirname(__file__), path)
    save_image = Image.fromarray(image)
    save_image.save(path)

if __name__ == "__main__":
    main()