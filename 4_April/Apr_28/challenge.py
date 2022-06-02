import json

# Task 1
list_of_10_photos = []
list_of_100_photos = []

# Task 2
list_of_10_random_photos = []
list_of_100_random_photos = []

def main():
    photosFile = open('photos.json', 'r')
    photo_list = json.load(photosFile)
    # Put your code here
    # e.g. to print it
    # print(photo_list)
    index = 0
    import random
    while index < len(photo_list):
        if index < 10:
            #list_of_10_photos.append(photo_list[index])
            list_of_10_photos.append(photo_list[round(random.random() * 1000)])
        if index < 100:
            #list_of_100_photos.append(photo_list[index])
            list_of_100_photos.append(photo_list[round(random.random() * 1000)])
        index += 1
        #index = index + 1

    print(list_of_10_photos)
    print(list_of_100_photos)
    # set index
    # while CONDITIONAL:
        # ADD TO LIST
    import random
    import math


if __name__ == "__main__":
    main()