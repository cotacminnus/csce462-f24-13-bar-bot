import subprocess
import time
import os
from PIL import Image, ImageFilter, ImageOps
import numpy as np

class FacialRecognition:
    @staticmethod
    def capture_image(save_path="captured_image.jpg"):
        """
        Captures an image using `libcamera-still` and saves it to the specified path.
        Returns the path to the captured image.
        """
        try:
            print("Capturing image...")
            # Ensure the directory exists
            save_dir = os.path.dirname(save_path)
            if save_dir and not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # Use libcamera-still to capture the image
            subprocess.run(
                ["libcamera-still", "-o", save_path, "--width", "640", "--height", "480", "--nopreview"],
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
    def detect_edges(image_path):
        """
        Applies edge detection to the image using Sobel or Canny-like filters.
        Returns the processed image as a NumPy array.
        """
        try:
            # Open the image and convert to grayscale
            image = Image.open(image_path).convert("L")
            # Apply edge detection
            edges = image.filter(ImageFilter.FIND_EDGES)
            # Enhance edges
            edges = ImageOps.autocontrast(edges)
            return np.array(edges)
        except Exception as e:
            raise Exception(f"Error during edge detection: {str(e)}")

    @staticmethod
    def detect_face(image_path):
        """
        Detects a face-like structure in the image using edge and geometry analysis.
        Returns True if a face-like structure is detected, False otherwise.
        """
        try:
            # Apply edge detection
            edge_array = FacialRecognition.detect_edges(image_path)

            # Analyze geometry: Detect circular or oval shapes
            # Define a bounding box in the center of the image
            height, width = edge_array.shape
            center_x, center_y = width // 2, height // 2
            box_size = min(width, height) // 4
            roi = edge_array[center_y - box_size:center_y + box_size, center_x - box_size:center_x + box_size]

            # Count edge intensity within the ROI
            edge_intensity = np.sum(roi > 128)  # Count pixels with high edge intensity

            print(f"Edge intensity in ROI: {edge_intensity}")

            # Thresholds for detection
            if edge_intensity > 500:  # Adjust threshold based on testing
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


'''
import subprocess
import time
import os
from PIL import Image, ImageFilter, ImageOps, ImageDraw
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
    def detect_edges(image_path):
        """
        Applies edge detection to the image using Sobel or Canny-like filters.
        Returns the processed image as a NumPy array.
        """
        try:
            # Open the image and convert to grayscale
            image = Image.open(image_path).convert("L")
            # Apply edge detection
            edges = image.filter(ImageFilter.FIND_EDGES)
            # Enhance edges
            edges = ImageOps.autocontrast(edges)
            return np.array(edges)
        except Exception as e:
            raise Exception(f"Error during edge detection: {str(e)}")

    @staticmethod
    def detect_face(image_path):
        """
        Detects a face-like structure in the image using edge and geometry analysis.
        Returns True if a face-like structure is detected, False otherwise.
        """
        try:
            # Apply edge detection
            edge_array = FacialRecognition.detect_edges(image_path)

            # Analyze geometry: Detect circular or oval shapes
            # Define a bounding box in the center of the image
            height, width = edge_array.shape
            center_x, center_y = width // 2, height // 2
            box_size = min(width, height) // 4
            roi = edge_array[center_y - box_size:center_y + box_size, center_x - box_size:center_x + box_size]

            # Count edge intensity within the ROI
            edge_intensity = np.sum(roi > 128)  # Count pixels with high edge intensity

            print(f"Edge intensity in ROI: {edge_intensity}")

            # Thresholds for detection
            if edge_intensity > 750:  
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

'''



