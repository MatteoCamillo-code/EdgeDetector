import numpy as np
import math 

class Convolutor:
    
    filter_arr = None
    gamma = -1
    
    def __init__(self, filter, gamma):
        self.filter_arr = filter
        self.gamma = gamma
        pass
    
    def set_filter(self, filter, gamma):
        self.filter_arr = filter
        self.gamma = gamma
    
    def convolution(self, image):
        if self.filter_arr is None or self.gamma == -1:
            raise ValueError("Filter not set")
        filt = np.flip(self.filter_arr)
        if filt.ndim == 1:
            filt = np.expand_dims(filt, axis=0)
        filt_h, filt_w = filt.shape if filt.ndim > 1 else (filt.shape[0], 0)
        pad_h, pad_w = filt_h // 2, filt_w // 2 if filt_w > 0 else 0
        
        # Pad the image to handle borders, add enough space to make the filter be able to go on the edges of the image
        padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
        result = np.zeros_like(image)

        # Efficient sliding window convolution
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                region = padded[i:i+filt_h, j:j+filt_w]
                result[i, j] = int(np.sum(region * filt) * self.gamma)

        return result 