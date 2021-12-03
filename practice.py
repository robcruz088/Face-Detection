import cv2

# Loading pre-trained data on frontal face

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Choosing an image
img = cv2.imread('rdj_tommy.jpg')

# converting to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces using rectangles - x, y, width, height
face_coordinates = face_cascade.detectMultiScale(gray_img)

# print(face_coordinates)

# draw rectangle for the faces - image, top left coord, x+width/y+height , line color (BGR), line thicc
# loop through list of face coordinates for multiple individuals
i = 0
while i < len(face_coordinates):
    (x,y,w,h) = face_coordinates[i]
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),5)
    i+=1



cv2.imshow("There's federal agents outside my house", img)
cv2.waitKey()

print("Lookin good bossu!")