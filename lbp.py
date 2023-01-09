import cv2
import numpy as np

#to juz nie potrzebne - to sprawdzalo tylko na jednym pliku !!!
    # pathToDataset = '/Users/mat/Desktop/studia 2022/sem1_nowy/ATAI/P/project_atai_fer/dataset/train/happy/im4.png'
    # img = cv2.imread(pathToDataset, cv2.IMREAD_COLOR)

#height, width, channel
#print(img.shape)

def getLBP(img2):
    print (img2)
    # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) czy moze byc img2 jako arg jak ponizej czy musi byc rozny???
    gray_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    image = np.zeros_like(gray_img)
    neighbor = 3

    for i in range(0,image.shape[0] - neighbor):
        for j in range(0, image.shape[1] - neighbor):
            img2 = gray_img[i: i+neighbor, j:j+neighbor]
            center = img2[1,1]
            img01 = (img2 >= center)*1.0
            img_vector = img01.T.flatten()
            img_vector = np.delete(img_vector,4)
            vector = np.where(img_vector)[0]
            if len(vector) >= 1:
                num = np.sum(2**vector)
            else:
                num = 0
            image[i+1, j+1] = num    
    
    return(image)

#to juz nie potrzebne - to sprawdzalo tylko na jednym pliku !!!
    # lbp_image = getLBP(img)
    # cv2.imshow("Input", lbp_image)
    # cv2.waitKey(0)
