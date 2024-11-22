import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import os

class FacialRecognition:
    @staticmethod
    def capture_image(save_path="captured_image.jpg"):
        """
        Captures an image using the Raspberry Pi camera module and saves it to the specified path.
        Returns the path to the captured image.
        """
        try:
            camera = PiCamera()
            raw_capture = PiRGBArray(camera)
            print("Capturing image...")
            camera.capture(raw_capture, format="bgr")
            camera.close()

            # Save the captured image
            image = raw_capture.array
            cv2.imwrite(save_path, image)
            print(f"Image saved to {save_path}")
            return save_path
        except Exception as e:
            raise Exception(f"Error capturing image: {str(e)}")

    @staticmethod
    def face_recog(image_path, cascade_path="haarcascade_frontalface_default.xml"):
        """
        Detects faces in the image using OpenCV's Haar cascade.
        Returns a boolean indicating whether a face is detected.
        """
        try:
            # Load the Haar cascade for face detection
            if not os.path.exists(cascade_path):
                raise FileNotFoundError("Haar cascade file not found. Please download it from OpenCV's GitHub.")

            face_cascade = cv2.CascadeClassifier(cascade_path)

            # Load the image
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if len(faces) == 0:
                print("No faces detected.")
                return False

            print(f"Detected {len(faces)} face(s).")
            return True
        except Exception as e:
            raise Exception(f"Error during facial recognition: {str(e)}")

    @staticmethod
    def detect_face_with_webcam(save_path="captured_image.jpg", cascade_path="haarcascade_frontalface_default.xml"):
        """
        Captures an image using the Raspberry Pi camera module and detects faces in it.
        Returns a boolean indicating whether a face is detected.
        """
        try:
            # Capture image from Raspberry Pi camera
            image_path = FacialRecognition.capture_image(save_path)
            # Detect faces in the captured image
            return FacialRecognition.face_recog(image_path, cascade_path)
        finally:
            # Clean up by removing the saved image
            if os.path.exists(save_path):
                os.remove(save_path)

if __name__ == "__main__":
    try:
        detected = FacialRecognition.detect_face_with_webcam()
        if detected:
            print("Face detected successfully!")
        else:
            print("No face detected.")
    except Exception as e:
        print(f"An error occurred: {e}")


'''
import boto3

# need to configure credentials
class Facial_Recognition:
    def face_recog(img_path):    #the relative path to the image will be passed in
        #passes in image, returns a bool, see if any faces are recognized
        client = boto3.client('rekognition')

        with open(img_path, 'rb') as image:
            response = client.detect_faces(
            Image={'Bytes': image.read()},
            Attributes=['DEFAULT']  # we don't need specific attributes as of now
        )

        if not response['FaceDetails']:
            print("No faces matched.")
            return False

        return True

    def test(img_path):
        client = boto3.client('rekognition')

        with open(img_path, 'rb') as image:
            response = client.detect_faces(
            Image={'Bytes': image.read()},
            Attributes=['DEFAULT']  # we don't need specific attributes as of now
        )
            
        if not response['FaceDetails']:
            print("No faces matched.")
            return False
        
        print(response)

        return True
'''
        
