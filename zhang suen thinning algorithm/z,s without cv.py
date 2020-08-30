#code
import numpy as np
import copy
#algorithm building

#condition one for step 1 and 2
def pixel_is_black(arr,x,y):
    if arr[x][y]==1:
        return True
    return False

#condition two for step 1 and 2
def pixel_has_2_to_6_black_neighbours(arr,x,y):
    #check whether the sum of neighbors is between 2 and 6 ,as pixel value can only be 0 and 1
    temp = arr[x-1][y] + arr[x-1][y+1] + arr[x][y+1] + arr[x+1][y+1] + arr[x+1][y] + arr[x+1][y-1] + arr[x][y-1] + arr[x-1][y-1]
    if temp>=2 and temp<=6:
        return True
    return False

#condition three for step 1 and 2
def pixel_has_1_white_to_black_neighbor_transition(arr,x,y):
    #creating a list of neighbor pixels consisting of 9 elements as P2 appears 2 times
    neighbors = [arr[x-1][y] ,arr[x-1][y+1] ,arr[x][y+1] ,arr[x+1][y+1] ,arr[x+1][y] ,arr[x+1][y-1] ,arr[x][y-1] ,arr[x-1][y-1] ,arr[x-1][y]]
    transitions = sum((a, b) == (0, 1) for a, b in zip(neighbors, neighbors[1:]))
    if transitions == 1:
        return True
    return False

#condition four for step 1
def at_least_one_of_P2_P4_P6_is_white(arr,x,y):
    #if at least one of P2 , P4 or P6 is 0(white)
    temp = arr[x-1][y] and arr[x][y+1] and arr[x+1][y]
    if temp == 0:
        return True
    return False

#condition five for step 1
def at_least_one_of_P4_P6_P8_is_white(arr,x,y):
    #if at least one of P4 , P6 or P8 is 0(white)
    temp = arr[x][y+1] and arr[x+1][y] and arr[x][y-1]
    if temp == 0:
        return True
    return False

#condition four for step 2
def at_least_one_of_P2_P4_P8_is_white(arr,x,y):
    #if at least one of P2 , P4 or P8 is 0(white)
    temp = arr[x-1][y] and arr[x][y+1] and arr[x][y-1]
    if temp == 0:
        return True
    return False

#condition five for step 2
def at_least_one_of_P2_P6_P8_is_white(arr,x,y):
    #if at least one of P2,P6 or P8 is white
    temp = arr[x-1][y] and arr[x+1][y] and arr[x][y-1]
    if temp == 0:
        return True
    return False



bin_thresh = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
[0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0],
[0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0],
[0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0],
[0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,0],
[0,1,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



#the thinning alogrithm
thinned_thresh = copy.deepcopy(bin_thresh)

while 1:

    thresh_copy = copy.deepcopy(thinned_thresh)
    pixels_meeting_criteria = []

    #step 1
    for i in range(1,9):
        for j in range(1,31):
            if pixel_is_black(thinned_thresh,i,j) and pixel_has_2_to_6_black_neighbours(thinned_thresh,i,j) and pixel_has_1_white_to_black_neighbor_transition(thinned_thresh,i,j) and at_least_one_of_P2_P4_P6_is_white(thinned_thresh,i,j) and at_least_one_of_P4_P6_P8_is_white(thinned_thresh,i,j):
                pixels_meeting_criteria.append((i,j))

    for pixel in pixels_meeting_criteria:
        thinned_thresh[pixel[0]][pixel[1]] = 0

    pixels_meeting_criteria = []

    #step 2
    for i in range(1,9):
        for j in range(1,31):
            if pixel_is_black(thinned_thresh,i,j) and pixel_has_2_to_6_black_neighbours(thinned_thresh,i,j) and pixel_has_1_white_to_black_neighbor_transition(thinned_thresh,i,j) and at_least_one_of_P2_P4_P8_is_white(thinned_thresh,i,j) and at_least_one_of_P2_P6_P8_is_white(thinned_thresh,i,j):
                pixels_meeting_criteria.append((i,j))

    for pixel in pixels_meeting_criteria:
        thinned_thresh[pixel[0]][pixel[1]] = 0

    if thresh_copy==thinned_thresh:
        break

#displaying
#without using algorithm
for i in bin_thresh:
	for j in i:
		if j==1:
			print('#',end="")
		else:
			print(' ',end="")
	print()

#after using algorithm
for i in thinned_thresh:
	for j in i:
		if j==1:
			print('#',end="")
		else:
			print(' ',end="")
	print()
