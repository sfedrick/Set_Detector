import cv2
import numpy as np
import argparse
import pdb
def detect_set(image):
    return  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



def cut_contour(image,contours,contourindex):
    mask = np.zeros_like(image) # Create mask where white is what we want, black otherwise
    cv2.drawContours(mask, contours, contourindex, (255, 255, 255), -1) # Draw filled contour in mask
    out = np.zeros_like(image) # Extract out the object and place into output image
    out[mask == 255] = image[mask == 255]
    #crop
    y, x, *trash = np.where(mask == 255)
    topy, topx = (np.min(y), np.min(x))
    bottomy, bottomx = (np.max(y), np.max(x))
    out = out[topy:bottomy+1, topx:bottomx+1]
    return out

def resize_to_resolution(image, target_width=256, target_height=256):

    # Step 2: Determine the current dimensions of the image
    current_height, current_width = image.shape[:2]

    # Step 3: Calculate the scaling factors for resizing
    width_scale = target_width / current_width
    height_scale = target_height / current_height

    # Step 4: Resize the image using the calculated scaling factors
    resized_image = cv2.resize(image, (target_width, target_height))

    # Step 5: Save the resized image (optional)
    # If you want to save the resized image, uncomment the following line:
    # cv2.imwrite("resized_image.jpg", resized_image)

    return resized_image

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
        out = resize_to_resolution(out)
        card_list.append(out)

    return card_list

def detect_set(card):
    return newcard
   
def extract_card(card):
    
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
        cv2.imwrite("sandbox/"+str(i)+"test.jpg",card)
        i+=1
    
    cv2.imwrite("sandbox/test.jpg", img)