import cv2
import imutils
#import pytesseract
import easyocr
import keras
import numpy as np
import matplotlib.pyplot as plt



MyPlate = 'BJY6688'
image = cv2.imread('3.jpg')
image = imutils.resize(image, width = 500)


#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

cv2.imshow("Original Image", image)
#cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRay Scale Image", gray)
#cv2.waitKey(0)

gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("Smoother Image", gray)
#cv2.waitKey(0)

edged = cv2.Canny(gray, 170, 200)
cv2.imshow("Canny edge",edged)
#cv2.waitKey(0)

cnts , new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

image1 = image.copy()
cv2.drawContours(image1, cnts, -1, (0,255,0),3)
cv2.imshow("Canny after contouring", image1)
#cv2.waitKey(0)

cnts =sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
NumberPlateCount = None

image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0,255,0),3)
cv2.imshow("Top 30 Contours", image2)
#cv2.waitKey(0)

#loop

count = 0
name = 1
for i in cnts:
    perimeter = cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, 0.03*perimeter, True)
    if(len(approx) == 4):
        NumberPlateCount = approx
        x, y, w, h = cv2.boundingRect(i)
        crp_img = image[y:y+h, x:x+w]
        cv2.imwrite(str(name)+ '.png',crp_img)
        name += 1

        break

cv2.drawContours(image,[NumberPlateCount], -1, (0,255,0),3)
cv2.imshow("Final Image", image)
#cv2.waitKey(0)

crop_img_loc = '1.png'
cv2.imshow("Cropped Image",cv2.imread(crop_img_loc))
#cv2.waitKey(0)


reader = easyocr.Reader(['en'])
output = reader.readtext(crop_img_loc)

#cord =output[-1][0]
print(output)

plate = []
for word in output:
    #plate.append(word[1])
    #if word[2]>= 0.8:
    plate.append(word[1])

plate1 = ''
for i in range(0,len(plate)):
    temp = len(plate) - i - 1
    plate1 += plate[temp]



print("The detected Number plate is : ",plate1)

if plate1==MyPlate:

    print("Gate shall open")
    cap = cv2.VideoCapture('Gate.mp4')
    if (cap.isOpened() == False):
        print("Error opening video  file")

    while (cap.isOpened()):

        ret, frame = cap.read()
        if ret == True:

            cv2.imshow('Frame', frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        else:
            break

    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

else:
    platenotrecognised1=cv2.imread('platenotrecognised1.jpg')
    cv2.imshow('MY.jpg', platenotrecognised1)
    print('Gate Shall Not Open')
    cv2.waitKey(0)



#text = pytesseract.image_to_string(crop_img_loc)
