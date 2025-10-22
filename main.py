from PIL import Image
from image_holder import ImageHolder
from convolutor import Convolutor
from filters import get_filter
import numpy as np
import os

image_name = "tiger"

def main():
    image_rel_path = ImageHolder(path=f"assets/base/{image_name}.jpeg")
    convolutor = Convolutor()

    gray__image = gray_scale_image(image_rel_path)
    
    blurred_image = blurr_image(gray__image, 1/16, convolutor)

    edged_image = detect_edges(blurred_image, "backward", convolutor)
    
    print("Image processing complete.")

def save_image(image, path):
    path = os.path.join(os.path.dirname(__file__), path)
    save_image = Image.fromarray(image)
    save_image.save(path)
    
def blurr_image(image, gamma, convolutor=None):
    filter = get_filter("gaussian_3x3")
    blurred_image = convolute_image(image, filter, gamma, convolutor)
    save_image(blurred_image, f"assets/processed/{image_name}_blurred.jpeg")
    return blurred_image

def gray_scale_image(image_holder):
    gray_image = image_holder.to_gray_scale()
    save_image(gray_image, f"assets/gray/{image_name}_gray.jpeg")
    return gray_image

def detect_edges(image, filter_id, convolutor=None):
    filter = get_filter(filter_id)
    edge_image = convolute_image(image, filter, 1, convolutor)
    save_image(edge_image, f"assets/processed/{image_name}_edge.jpeg")
    return edge_image

def convolute_image(image, filter, gamma, convolutor=None):
    if convolutor is None:
        convolutor = Convolutor(filter, gamma)
    else:
        convolutor.set_filter(filter, gamma)
    convoluted_image = convolutor.convolution(image)
    return convoluted_image

if __name__ == "__main__":
    main()