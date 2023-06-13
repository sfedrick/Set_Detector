import cv2
import numpy as np
import argparse

def detect_set(image):
    return  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



def cut_contour(image,contours,contourindex):
    mask = np.zeros_like(image) # Create mask where white is what we want, black otherwise
    cv2.drawContours(mask, contours, contourindex, (255, 255, 255), -1) # Draw filled contour in mask
    out = np.zeros_like(image) # Extract out the object and place into output image
    out[mask == 255] = image[mask == 255]
    return out


def find_cards(image):
    card_list = []
    # converting image into grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # setting threshold of gray image
    _, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    # using a findContours() function
    cards, _ = cv2.findContours(
        threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)    
    i = 0
    color_draw = (0, 255, 0)
    for i,contour in enumerate(cards):
        out = cut_contour(image,cards,i)
        card_list.append(out)

    return card_list

def detect_set(card):
     # converting image into grayscale image
    gray = cv2.cvtColor(card, cv2.COLOR_BGR2GRAY)
    # setting threshold of gray image
    _, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    shapes, hierarchy = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    
    newcard=cv2.drawContours(card, shapes, -1, (0,255,0), 3)
    i = 0
    for _,contour in enumerate(shapes):
        if(cv2.contourArea(contour) > cv2.arcLength(contour, True)):
            i += 1
   
    print(i)
    return newcard
   


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--photo", help="An image file name you want to find the set of")
    args = parser.parse_args()
    img = cv2.imread(args.photo)
    card_list = find_cards(img)
    i = 0
    for card in card_list:
        print(str(i)+" test.jpg")
        newcard = detect_set(card)
        cv2.imwrite(str(i)+" test.jpg",newcard)
        i+=1
    
    cv2.imwrite("test.jpg", img)