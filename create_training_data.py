import cv2
import numpy as np
import argparse
from set_detect import *




def save_frames(video_path, output_folder,name):
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    while True:
        # Read the next frame from the video
        ret, frame = cap.read()
        
        # Check if the frame was successfully read
        if not ret:
            break
        cards = find_cards(frame)
        # Save the frame as an image in the output folder
        card_num =0
        for card in cards:

            frame_filename = f"{output_folder}/{name}{card_num}{frame_count:04d}.jpg"
            cv2.imwrite(frame_filename, card)
            card_num +=1
        frame_count += 1

    # Release the video capture object
    cap.release()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--video", help="A video file name of the sets you want to turn into a training set")
    parser.add_argument("-n", "--name", help="name of the card")
    args = parser.parse_args()
    video_path = args.video 
    card_name = args.name
    output_folder = "sandbox/training_set"     
    save_frames(video_path,output_folder,card_name)