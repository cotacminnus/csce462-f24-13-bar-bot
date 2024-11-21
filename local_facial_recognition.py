import face_recognition
from picamera import PiCamera
from PIL import Image
import numpy as np
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
            camera.start_preview()
            print("Capturing image...")
            camera.capture(save_path)
            camera.stop_preview()
            camera.close()
            print(f"Image saved to {save_path}")
            return save_path
        except Exception as e:
            raise Exception(f"Error capturing image: {str(e)}")

    @staticmethod
    def face_recog(image_path):
        """
        Detects faces in the image using the face_recognition library.
        Returns a boolean indicating whether a face is detected.
        """
        try:
            # Load the image file into a numpy array
            image = face_recognition.load_image_file(image_path)
            # Detect face locations
            face_locations = face_recognition.face_locations(image)

            if not face_locations:
                print("No faces detected.")
                return False

            print(f"Face(s) detected at locations: {face_locations}")
            return True
        except Exception as e:
            raise Exception(f"Error during facial recognition: {str(e)}")

    @staticmethod
    def detect_face_with_webcam(save_path="captured_image.jpg"):
        """
        Captures an image using the Raspberry Pi camera module and detects faces in it.
        Returns a boolean indicating whether a face is detected.
        """
        try:
            # Capture image from Raspberry Pi camera
            image_path = FacialRecognition.capture_image(save_path)
            # Detect faces in the captured image
            return FacialRecognition.face_recog(image_path)
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
