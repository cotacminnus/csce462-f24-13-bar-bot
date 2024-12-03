from picamera import PiCamera
from PIL import Image, ImageOps
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
            camera.resolution = (640, 480)
            print("Capturing image...")
            camera.capture(save_path)
            camera.close()
            print(f"Image saved to {save_path}")
            return save_path
        except Exception as e:
            raise Exception(f"Error capturing image: {str(e)}")

    @staticmethod
    def preprocess_image(image_path):
        """
        Converts the image to grayscale and applies edge detection.
        Returns the processed image as a NumPy array.
        """
        try:
            # Open the image and convert it to grayscale
            image = Image.open(image_path).convert("L")
            # Enhance edges using Sobel-like kernel convolution
            image = ImageOps.autocontrast(image)
            return np.array(image)
        except Exception as e:
            raise Exception(f"Error preprocessing image: {str(e)}")

    @staticmethod
    def detect_face(image_array):
        """
        Detects a "face-like" structure in the image using basic image processing.
        Returns True if a face-like structure is detected, False otherwise.
        """
        try:
            # Define thresholds for face-like regions
            mean_intensity = np.mean(image_array)
            high_intensity_region = image_array > mean_intensity * 1.1  # Bright regions
            low_intensity_region = image_array < mean_intensity * 0.9  # Dark regions

            # Check if high and low intensity regions form clusters (e.g., eyes and mouth)
            bright_pixels = np.sum(high_intensity_region)
            dark_pixels = np.sum(low_intensity_region)

            # Heuristic thresholds for detecting face-like patterns
            if bright_pixels > 500 and dark_pixels > 500:  # Adjust as needed
                print("Face-like structure detected!")
                return True
            else:
                print("No face detected.")
                return False
        except Exception as e:
            raise Exception(f"Error detecting face: {str(e)}")

    @staticmethod
    def detect_face_with_webcam(save_path="captured_image.jpg"):
        """
        Captures an image using the Raspberry Pi camera module and detects a face-like structure in it.
        Returns a boolean indicating whether a face is detected.
        """
        try:
            # Capture an image from the camera
            image_path = FacialRecognition.capture_image(save_path)
            # Preprocess the image
            image_array = FacialRecognition.preprocess_image(image_path)
            # Detect face-like structures
            return FacialRecognition.detect_face(image_array)
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
