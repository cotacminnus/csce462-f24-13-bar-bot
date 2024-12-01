import os
from local_facial_recognition import FacialRecognition

def test_capture_image():
    """
    Test the capture_image method to ensure it saves an image file.
    """
    test_image_path = "test_image.jpg"
    try:
        captured_path = FacialRecognition.capture_image(save_path=test_image_path)
        assert os.path.exists(captured_path), "Image was not saved correctly."
        print("test_capture_image passed!")
    except Exception as e:
        print(f"test_capture_image failed: {e}")
    finally:
        if os.path.exists(test_image_path):
            os.remove(test_image_path)

def test_face_recog():
    """
    Test the face_recog method with a valid image file.
    """
    sample_image_path = "sample_face.jpg"
    if not os.path.exists(sample_image_path):
        print(f"Sample image '{sample_image_path}' not found. Please provide a valid image.")
        return

    try:
        result = FacialRecognition.face_recog(image_path=sample_image_path)
        assert isinstance(result, bool), "face_recog did not return a boolean."
        print(f"test_face_recog passed! Face detected: {result}")
    except Exception as e:
        print(f"test_face_recog failed: {e}")

def test_detect_face_with_webcam():
    """
    Test the detect_face_with_webcam method.
    """
    try:
        result = FacialRecognition.detect_face_with_webcam()
        assert isinstance(result, bool), "detect_face_with_webcam did not return a boolean."
        print(f"test_detect_face_with_webcam passed! Face detected: {result}")
    except Exception as e:
        print(f"test_detect_face_with_webcam failed: {e}")

if __name__ == "__main__":
    print("Running tests...")
    test_capture_image()
    test_face_recog()
    test_detect_face_with_webcam()
