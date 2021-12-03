import cv2
from random import randrange

# Loading pre-trained data on frontal face

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Choosing a video (no webcam available)
# for webcam replace VideoCapture parameter with 0
vid = cv2.VideoCapture('video.mov')

# iterate over the frames
while True:
    # capture frame by frame
    video, frame = vid.read()

    # if frame is read correctly, video returns TRUE
    if not video:
        print("Can't receive frame. Exiting ...")
        break

    # convert frame to grayscale
    gray_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces using rectangles - x, y, width, height
    face_coordinates = face_cascade.detectMultiScale(gray_vid)

    for i in face_coordinates:
        (x, y, w, h) = i
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 5)

    # display resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break

# once finished, released capture
vid.release()
cv2.destroyAllWindows()

print("Lookin good bossu!")