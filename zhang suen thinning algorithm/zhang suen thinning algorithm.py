import cv2
import numpy as np
import copy

#0 = grascale
img = cv2.imread('fingerprint.png',0)
retval,orig_thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
bin_thresh = (orig_thresh == 0).astype(int)

#algorithm building

#condition one for step 1 and 2
def pixel_is_black(arr,x,y):
    if arr[x,y]==1:
        return True
    return False

#condition two for step 1 and 2
def pixel_has_2_to_6_black_neighbours(arr,x,y):
    #check whether the sum of neighbors is between 2 and 6 ,as pixel value can only be 0 and 1
    if 2<=arr[x,y+1] + arr[x+1,y+1] + arr[x+1,y] + arr[x+1,y-1] + arr[x,y-1] + arr[x-1,y-1] + arr[x-1,y] + arr[x-1,y+1] <=6:
        return True
    return False

#condition three for step 1 and 2
def pixel_has_1_white_to_black_neighor_transition(arr,x,y):
    #creating a list of neighor pixels consisting of 9 elements as P2 appears 2 times
    neighbors = [arr[x,y+1] ,arr[x+1,y+1] ,arr[x+1,y] ,arr[x+1,y-1] ,arr[x,y-1] ,arr[x-1,y-1] ,arr[x-1,y] ,arr[x-1,y+1] ,arr[x,y+1]]
    transitions = sum((a, b) == (0, 1) for a, b in zip(neighbors, neighbors[1:]))
    if transitions == 1:
        return True
    return False

#condition four for step 1
def at_least_one_of_P2_P4_P6_is_white(arr,x,y):
    #if at least one of P2 , P4 or P6 is 0(white)
    if arr[x,y+1] and arr[x+1,y] and arr[x,y-1] == False:
        return True
    return False

#condition five for step 1
def at_least_one_of_P4_P6_P8_is_white(arr,x,y):
    #if at least one of P4 , P6 or P8 is 0(white)
    if arr[x+1,y] and arr[x,y-1] and arr[x-1,y] == False:
        return True
    return False

#condition four step 2
def at_least_one_of_P2_P4_P8_is_white(arr,x,y):
    #if at least one of P2 , P4 or P8 is 0(white)
    if arr[x,y+1] and arr[x+1,y] and arr[x-1,y] == False:
        return True
    return False

#condition five step 2
def at_least_one_of_P2_P6_P8_is_white(arr,x,y):
    #if at least one of P2,P6 or P8 is white
    if arr[x,y-1] and arr[x,y+1] and arr[x-1,y] == False:
        return True
    return False



#the thinning alogrithm
thinned_thresh = copy.deepcopy(bin_thresh)

while 1:
    thresh_copy = copy.deepcopy(thinned_thresh)
    pixels_meeting_criteria = []

    #step 1
    for i in range(1,thinned_thresh.shape[0]-1):
        for j in range(1,thinned_thresh.shape[1]-1):
            if pixel_is_black(thinned_thresh,i,j) and pixel_has_2_to_6_black_neighbours(thinned_thresh,i,j) and pixel_has_1_white_to_black_neighor_transition(thinned_thresh,i,j) and at_least_one_of_P2_P4_P6_is_white(thinned_thresh,i,j) and at_least_one_of_P4_P6_P8_is_white(thinned_thresh,i,j):
                pixels_meeting_criteria.append((i,j))

    for pixel in pixels_meeting_criteria:
        thinned_thresh[pixel] = 0

    #step 2
    pixels_meeting_criteria = []

    for i in range(1,thinned_thresh.shape[0]-1):
        for i in range(1,thinned_thresh.shape[1]-1):
            if pixel_is_black(thinned_thresh,i,j) and pixel_has_2_to_6_black_neighbours(thinned_thresh,i,j) and pixel_has_1_white_to_black_neighor_transition(thinned_thresh,i,j) and at_least_one_of_P2_P4_P8_is_white(thinned_thresh,i,j) and at_least_one_of_P2_P6_P8_is_white(thinned_thresh,i,j):
                pixels_meeting_criteria.append((i,j))

    for pixel in pixels_meeting_criteria:
        thinned_thresh[pixel] = 0

    if np.all(thresh_copy==thinned_thresh) == True:
        break

thresh = (thinned_thresh==0).astype(np.uint8)
thresh = thresh*255

#display original and thinned images
cv2.imshow('original image',orig_thresh)
cv2.imshow('thinned image',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()













print("hello")
