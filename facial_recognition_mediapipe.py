import mediapipe as mp
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np
import os
from PIL import Image

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
            camera.capture(raw_capture, format="rgb")
            camera.close()
            image = raw_capture.array

            # Save the image
            Image.fromarray(image).save(save_path)
            print(f"Image saved to {save_path}")
            return save_path
        except Exception as e:
            raise Exception(f"Error capturing image: {str(e)}")

    @staticmethod
    def face_recog(image_path):
        """
        Detects faces in the image using MediaPipe.
        Returns a boolean indicating whether a face is detected.
        """
        try:
            # Load the image
            image = Image.open(image_path).convert("RGB")
            image_array = np.array(image)

            # Initialize MediaPipe Face Detection
            mp_face_detection = mp.solutions.face_detection
            face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

            # Perform face detection
            results = face_detection.process(image_array)

            # Check if faces are detected
            if not results.detections:
                print("No faces detected.")
                return False

            print(f"Detected {len(results.detections)} face(s).")
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
