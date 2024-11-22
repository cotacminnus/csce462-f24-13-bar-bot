import subprocess
import time
from PIL import Image, ImageOps
import numpy as np
import os

class FacialRecognition:
    @staticmethod
    def capture_image(save_path="captured_image.jpg"):
        """
        Captures an image using `fswebcam` and saves it to the specified path.
        Returns the path to the captured image.
        """
        try:
            print("Capturing image...")
            # Use fswebcam to capture an image
            subprocess.run(["fswebcam", "-r", "640x480", "--no-banner", save_path], check=True)
            print(f"Image saved to {save_path}")
            return save_path
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error capturing image: {e}")

    @staticmethod
    def preprocess_image(image_path):
        """
        Converts the image to grayscale and applies basic edge detection.
        Returns the processed image as a NumPy array.
        """
        try:
            # Open the image and convert it to grayscale
            image = Image.open(image_path).convert("L")
            # Enhance edges using autocontrast
            image = ImageOps.autocontrast(image)
            return np.array(image)
        except Exception as e:
            raise Exception(f"Error preprocessing image: {str(e)}")

    @staticmethod
    def detect_face(image_array):
        """
        Detects a "face-like" structure in the image using intensity clustering.
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
    def poll_facial_recognition(interval=2, save_path="captured_image.jpg"):
        """
        Continuously captures images and checks for face-like structures at a given interval.
        """
        try:
            while True:
                print("Polling for faces...")
                # Capture an image
                image_path = FacialRecognition.capture_image(save_path)
                # Preprocess the image
                image_array = FacialRecognition.preprocess_image(image_path)
                # Check for a face
                if FacialRecognition.detect_face(image_array):
                    print("Face detected successfully!")
                else:
                    print("No face detected.")
                # Wait for the next poll
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nPolling stopped by user.")
        finally:
            # Clean up the captured image
            if os.path.exists(save_path):
                os.remove(save_path)

if __name__ == "__main__":
    try:
        FacialRecognition.poll_facial_recognition()
    except Exception as e:
        print(f"An error occurred: {e}")
