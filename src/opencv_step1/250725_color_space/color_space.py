import cv2 as cv
import numpy as np

flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)