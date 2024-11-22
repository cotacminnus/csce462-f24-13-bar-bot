import os
import numpy as np
from FRbasic import FacialRecognition

def test_capture_image():
    """
    Test the capture_image method to ensure it saves an image file.
    """
    test_image_path = "test_image.jpg"
    try:
        # Capture an image
        captured_path = FacialRecognition.capture_image(save_path=test_image_path)
        assert os.path.exists(captured_path), "Image file was not saved."
        print("test_capture_image passed!")
    except Exception as e:
        print(f"test_capture_image failed: {e}")
    finally:
        # Cleanup the test image
        if os.path.exists(test_image_path):
            os.remove(test_image_path)

def test_preprocess_image():
    """
    Test the preprocess_image method to ensure it processes the image correctly.
    """
    sample_image_path = "sample_face.jpg"

    # Ensure a sample image file exists
    if not os.path.exists(sample_image_path):
        print(f"Sample image '{sample_image_path}' not found. Please provide a valid image.")
        return

    try:
        # Preprocess the image
        processed_image = FacialRecognition.preprocess_image(sample_image_path)
        assert isinstance(processed_image, np.ndarray), "Preprocessed image is not a NumPy array."
        assert len(processed_image.shape) == 2, "Preprocessed image is not grayscale."
        print("test_preprocess_image passed!")
    except Exception as e:
        print(f"test_preprocess_image failed: {e}")

def test_detect_face():
    """
    Test the detect_face method with a preprocessed image.
    """
    sample_image_path = "sample_face.jpg"

    # Ensure a sample image file exists
    if not os.path.exists(sample_image_path):
        print(f"Sample image '{sample_image_path}' not found. Please provide a valid image.")
        return

    try:
        # Preprocess the image
        processed_image = FacialRecognition.preprocess_image(sample_image_path)
        # Detect a face-like structure
        result = FacialRecognition.detect_face(processed_image)
        assert isinstance(result, bool), "detect_face did not return a boolean value."
        print(f"test_detect_face passed! Face detected: {result}")
    except Exception as e:
        print(f"test_detect_face failed: {e}")

def test_detect_face_with_webcam():
    """
    Test the detect_face_with_webcam method end-to-end.
    """
    try:
        # Detect a face directly using the webcam
        result = FacialRecognition.detect_face_with_webcam()
        assert isinstance(result, bool), "detect_face_with_webcam did not return a boolean value."
        print(f"test_detect_face_with_webcam passed! Face detected: {result}")
    except Exception as e:
        print(f"test_detect_face_with_webcam failed: {e}")

if __name__ == "__main__":
    print("Running tests...")
    test_capture_image()
    test_preprocess_image()
    test_detect_face()
    test_detect_face_with_webcam()

