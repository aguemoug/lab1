
# defining some utility functions

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt # w use plt in rather than pyplot 


def cv_show(image):
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
def to_gray(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def sbs(src,dst,title1="src",title2="dst"):
    """[summary]
    Show images side by side

    Args:
        src ([type]): [source image]
        dst ([type]): [distinction image]
        title1 ([type]): [source image title]
        title2 ([type]): [distinction image title]
    """ 
    plt.subplot(121),cv_show(src),plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),cv_show(dst),plt.title(title2)
    plt.xticks([]), plt.yticks([])
    plt.show()
