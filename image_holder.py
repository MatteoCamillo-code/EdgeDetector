from PIL import Image
import os
import numpy as np

class ImageHolder:
    
    path = None
    data = None
    width = -1
    height = -1
    channels = -1
    
    def __init__(self, path):
        path = os.path.join(os.path.dirname(__file__), path)
        self.path = path
        self.data = Image.open(path, 'r')
        if self.data is None:
            raise ValueError("The path is not found: " + self.path) 
        self.width, self.height = self.data.size
        self.channels = len(self.data.getbands())
    
    def get_data(self):
        return list(self.data.getdata())
    
    def get_shaped_data(self):
        imageData = self.get_data()
        data = np.array(imageData, dtype=np.uint8)
        return data.reshape((self.height, self.width, self.channels))

    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width

    def get_size(self):
        return self.width, self.height
    
    def update_image(self):
        self.data.save(self.path)
        
    def to_gray_scale(self):
        raw_data = self.get_data()
        size = (self.get_height(), self.get_width())
        gray_data = np.zeros(size, dtype=np.uint8)
        if self.channels != 3:
            return self.get_shaped_data()
        row, col = gray_data.shape
        for i in range(row):
            for j in range(col):
                r, g, b = raw_data[i * col + j]
                gray_data[i, j] = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray_data