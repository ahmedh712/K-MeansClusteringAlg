#Ahmed Hassan
from image_utils import *
from math import *
import functools
def k_means (image, k):
    """ Uses the K-Means algorithm, a clustering algorithm, to take in an image,
    create k clusters which are relative averages of the colors in the picture,
    then assign each pixel the closest cluster color"""
    width, height = get_width_height(image)

    #creates a list of random color guesses for each cluster
    centroids = [centroid() for color in range(k)]
    # Creates a 2D array corresponding to each pixel, so the assignments can be saved
    assignments = [[0 for y in range(height)] for x in range(width)]
    centroids[0].total_assignments = width * height

    #loop that keeps updating the centroids til no more changes happen to them
    changes = True
    while changes == True:
        changes=False
        # assign each pixel a centroid
        for x in range(width):
            for y in range(height):
                for c_num in range(len(centroids)):
                    if distance(centroids[c_num].color,image[x][y]) < distance(image[x][y],centroids[assignments[x][y]].color):
                        changes=True
                        centroids[c_num].total_assignments += 1
                        centroids[assignments[x][y]].total_assignments -= 1
                        centroids[c_num].sum = add_colors(image[x][y], centroids[c_num].sum)
                        centroids[assignments[x][y]].sum = subtract_colors(centroids[assignments[x][y]].sum,image[x][y])
                        assignments[x][y] = c_num
                        current_distance = distance(image[x][y], centroids[assignments[x][y]].color)
        #update centroids
        for num in range(len(centroids)):
            if centroids[num].total_assignments != 0:
                centroids[num].color = (centroids[num].sum[0] // centroids[num].total_assignments,
                                        centroids[num].sum[1] // centroids[num].total_assignments,
                                        centroids[num].sum[2] // centroids[num].total_assignments)

        # update pixels
    for x in range(width):
        for y in range(height):
            image[x][y] = centroids[assignments[x][y]].color
    return image

@functools.lru_cache(maxsize=128)
def distance(col1, col2):
    """ Finds the euclidean distance between two color RGB values"""
    return (col1[0]-col2[0])*(col1[0]-col2[0])+  (col1[1]-col2[1])*(col1[1]-col2[1]) + (col1[2]-col2[2])*(col1[2]-col2[2])

def add_colors(col1, col2):
    """since tuples cannot be added normally, takes the RGB values of 2 colors and adds each element"""
    return col1[0]+col2[0], col1[1]+col2[1], col1[2]+col2[2]

def subtract_colors(col1, col2):
    """since tuples cannot be added normally, takes the RGB values of 2 colors and subtracts each element"""
    return col1[0]-col2[0], col1[1]-col2[1], col1[2]-col2[2]

class centroid:
    def __init__(self):
        self.color= random_color()
        self.total_assignments = 0
        self.sum = (0,0,0)
