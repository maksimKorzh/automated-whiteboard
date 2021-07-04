#####################################
#
#  Simple python script to extract 
#        edges from images
#
#               by
#
#        Code Monkey King
#
#####################################

# packages
import cv2
import os

# extract the number of frames
frames = len(os.listdir('./Images'))

# loop over images
for i in range(1, frames):
    # open source image
    image = cv2.imread('./Images/image' + str(i) + '.png', cv2.IMREAD_UNCHANGED)

    # convert image to grayscale
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # reduce image noice
    image_blur = cv2.medianBlur(image_grayscale, 9)

    # extract edges
    image_edges = cv2.adaptiveThreshold(
        image_blur,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        blockSize=7,
        C=2
    )
               
    # write output images
    cv2.imwrite('./Animation/image' + str(i) + '.png', image_edges)
    
    # debug message
    print('Storing frame:', './Animation/image' + str(i) + '.png')

    # display image in a window
    #cv2.imshow('Image', image_cartoon)

    # break out of a program
    #cv2.waitKey(0)

    # clean up windows
    #cv2.destroyAllWindows()
