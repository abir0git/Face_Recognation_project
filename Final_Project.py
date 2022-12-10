import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade_side = cv2.CascadeClassifier('haarcascade_profileface.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

while (True):
    try:
        # Read the frame
        success , img = cap.read()
        # To resize the camera window and to use maximize button
        cv2.namedWindow("FACE DETECTION SOFTWARE", cv2.WINDOW_NORMAL)
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        faces_side = face_cascade_side.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        flag = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            flag = 1
        # if no front face then check for side face
        if(flag == 0):
            for (x, y, w, h) in faces_side:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # Display
        cv2.imshow('FACE DETECTION SOFTWARE', img)
    except:
        pass
    # Stop if escape key is pressed
    k = cv2.waitKey(1) & 0xff
    if k==27:
        break
    # When cross button is clicked the window closed.
    # That is its a alternate quit button
    try:
        if(cv2.getWindowProperty('FACE DETECTION SOFTWARE', 0) < 0):
            break
    except:
        break

# Release the VideoCapture object
cap.release()