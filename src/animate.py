##########################################
#
#  Simple script to automate the process
#       of drawing using Python
#
#                 by
#
#          Code Monkey King
#
##########################################

# packages
import cv2
import pyautogui as pg
import time
import random
import os

# global coordinates of where to start drawing (change if needed!)
x_start = 100
y_start = 100

# put mouse mointer into initial position
pg.moveTo(x_start, y_start)

# wait before user clicks on window to within
time.sleep(1)

# extract the number of frames
frames = len(os.listdir('./Images'))

# loop over images
for i in range(1, frames):
    # open source image
    image = cv2.imread('./Animation/image' + str(i) + '.png', cv2.IMREAD_UNCHANGED)
    
    # get row indexes
    random_rows = list(range(len(image)))

    # comment two lines below if you want a "printer" like behavior
    random_rows = random.sample(range(len(image)), len(image))
    random.shuffle(random_rows)

    # loop over pixel rows
    for y in random_rows:
        # randomize cols traversal order
        row = image[y]
        random_cols = list(range(len(row)))
        #random.shuffle(random_cols)
        
        # loop over pixel cols
        for x in random_cols:
            if row[x] == 0:
                # draw pixel!
                pg.click(x_start + x, y_start + y, _pause=False)
                print('Drawing at:', x_start + x, y_start + y)

# escape from script
#cv2.waitKey(0)

# clean up windows
#cv2.destroyAllWindows()
