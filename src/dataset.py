#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:25:22 2020

@author: aparnami
"""

import os
import random
import numpy as np
from PIL import Image
from .util import pillow_to_numpy

data_path = {
'faces':"/Users/aycanaslan/Dropbox/Uni:Learning/MA/test_dp_pixel/at&t"        
}

def choose_random_path(path):
    files = os.listdir(path)
    file = random.choice(files)
    path = os.path.join(path, file)
    return path

class Dataset:
    def __init__(self):
        self.data_dir = ''
        self.scale = None
    
    def get_random_image():
        pass 
    
    def load_images(self, n=16):
        image_paths = set([self.get_random_image() for i in range(n)])
        images = list(map(pillow_to_numpy, map(Image.open, image_paths)))
        return images

class FacesDataset(Dataset):
    def __init__(self):
        self.data_dir = data_path['faces']
        self.scale = (25,25)
        
    def get_random_image(self):
        person = choose_random_path(self.data_dir)
        image = choose_random_path(person)
        return image
