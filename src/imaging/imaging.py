import cv2
from numpy import ndarray


def check_images_match(image_1: ndarray, image_2: ndarray) -> bool:
    assert type(image_1) == ndarray
    assert type(image_2) == ndarray


    # Dimensions and color channels
    #image_1.shape == image_2.shape

    color_differences = cv2.split(cv2.subtract(image_1, image_2))

    return \
        cv2.countNonZero(color_differences[0]) == \
        cv2.countNonZero(color_differences[1]) == \
        cv2.countNonZero(color_differences[2]) == 0

