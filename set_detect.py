import cv2
def detect_set(image):
    return  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)