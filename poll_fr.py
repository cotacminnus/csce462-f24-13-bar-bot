import subprocess
import time
import os
from PIL import Image, ImageOps, ImageDraw
import numpy as np

class FacialRecognition:
    @staticmethod
    def capture_image(save_path="captured_image.jpg"):
        """
        Captures an image using `fswebcam` and saves it to the specified path.
        Returns the path to the captured image.
        """
        try:
            print("Capturing image...")
            # Ensure the directory exists
            save_dir = os.path.dirname(save_path)
            if save_dir and not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # Use fswebcam to capture the image
            subprocess.run(
                ["fswebcam", "-r", "640x480", "--no-banner", save_path],
                check=True
            )
            if os.path.exists(save_path):
                print(f"Image successfully saved to {save_path}")
                return save_path
            else:
                raise Exception("Image capture failed, file not saved.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error capturing image: {e}")

    @staticmethod
    def detect_face(image_path):
        """
        Detects a face-like structure in the image using stricter heuristics.
        Returns True if a face-like structure is detected, False otherwise.
        """
        try:
            # Open the image and convert to grayscale
            image = Image.open(image_path).convert("L")
            image_array = np.array(image)

            # Threshold for pixel intensity
            mean_intensity = np.mean(image_array)
            high_intensity_region = image_array > mean_intensity * 1.2  # Brighter regions
            low_intensity_region = image_array < mean_intensity * 0.8  # Darker regions

            # Count bright and dark pixels
            bright_pixels = np.sum(high_intensity_region)
            dark_pixels = np.sum(low_intensity_region)

            print(f"Bright pixels: {bright_pixels}, Dark pixels: {dark_pixels}")

            # Strict heuristic: Ensure bright and dark regions are in proportion
            if 1500 < bright_pixels < 5000 and 1500 < dark_pixels < 5000:
                print("Face-like structure detected!")
                return True
            else:
                print("No face detected.")
                return False
        except Exception as e:
            print(f"Error detecting face: {str(e)}")
            return False

    @staticmethod
    def poll_webcam(interval=2, save_path="captured_image.jpg"):
        """
        Continuously polls the webcam for face detection.
        """
        try:
            while True:
                print("Polling for faces...")
                # Capture an image
                image_path = FacialRecognition.capture_image(save_path)
                # Detect face directly from the image
                if FacialRecognition.detect_face(image_path):
                    print("Face detected!")
                else:
                    print("No face detected.")
                # Wait before the next poll
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nPolling stopped by user.")
        finally:
            # Cleanup
            if os.path.exists(save_path):
                os.remove(save_path)

if __name__ == "__main__":
    try:
        FacialRecognition.poll_webcam(save_path="output/captured_image.jpg")
    except Exception as e:
        print(f"An error occurred: {e}")


