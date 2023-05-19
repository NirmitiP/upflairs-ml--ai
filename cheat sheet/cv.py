import cv2
# Reading an image
img = cv2.imread('image.jpg')

# Displaying an image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# This code loads an image file named "image.jpg" and displays it in a window using the cv2.imshow function. 
# The cv2.waitKey(0) function waits for a key press, 
# cv2.destroyAllWindows closes the window when a key is pressed.

# Converting an image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blurring an image
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Thresholding an image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Detecting edges in an image
edges = cv2.Canny(gray, 100, 200)


# Loading the face detection classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detecting faces in an image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Drawing rectangles around detected faces
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
