#Ahmed Hassasn
from image_utils import *
from k_means import *

if __name__ == "__main__":
    file_name = input("What is the file name of the image you'd like to change?: ")
    k = int(input("What is the K value you would like to use?: "))
    output = input("What is the file name of the image you'd like to output to?: ")
    image = read_ppm(file_name)
    width, height = get_width_height(image)
    save_ppm(output, k_means(image, k))
