from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 30
camera.brightness = 65
raw_capture = PiRGBArray(camera, size=(320,240))
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    img = frame.array
    cv2.imshow("Original Image", img)
    raw_capture.truncate(0)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

# Load the Haar Cascade file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not open video.")
    exit()

print("Starting webcam for face detection. Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
video_capture.release()
cv2.destroyAllWindows()
