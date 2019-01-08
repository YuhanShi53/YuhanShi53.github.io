import os
import cv2

def get_results(image_name, dir_1, dir_2, dir_3):

    dirs = [dir_1, dir_2, dir_3]
    images = []
    for dir in dirs:
        image_path = os.path.join(dir, image_name+".jpg")
        try:
            image = cv2.imread(image_path)[:,:,-1]
            images.append(image)
        except Exception:
            print("Image path {} not exists".format(image_path))
    return images