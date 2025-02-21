import cv2

## Reading the image plaksha_Faculty.jpg

img = cv2.imread("data/Plaksha_Faculty.jpg")

## Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Loading the required haar-cascade xml classifier file
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Applying the face detection method on the grayscale image.
## Change the parameters for better detection of faces in your case.
faces_rect = face_cascade.detectMultiScale(
    gray_img, 1.05, 4, minSize=(25, 25), maxSize=(50, 50)
)

# Define the text and font parameters
text = "Face Detected"  ## The text you want to write
font = cv2.FONT_HERSHEY_SIMPLEX  ## Font type
font_scale = 1  ## Font scale factor
font_color = (0, 0, 255)  ## Text color in BGR format (here, it's red)
font_thickness = 2  ## Thickness of the text


# Iterating through rectangles of detected faces
for x, y, w, h in faces_rect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # Use cv2.putText to add the text to the image, Use text, font, font_scale, font_color, font_thickness here
    cv2.putText(img, text, (x, y - 10), font, font_scale, font_color, font_thickness)

## Display the image and window title should be "Total number of face detected are #"
cv2.imshow("Total number of face detected are {}".format(len(faces_rect)), img)
cv2.waitKey(0)
cv2.destroyAllWindows()
