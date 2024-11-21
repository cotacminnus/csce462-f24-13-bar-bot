from facial_recog import FacialRecognition

def test_webcam_facial_recognition():
    """
    Tests the webcam-based facial recognition functionality.
    Captures an image using the webcam and checks for face detection.
    """
    print("Starting webcam facial recognition test...")

    try:
        # Attempt to detect a face using the webcam
        face_detected = FacialRecognition.detect_face_with_webcam("test_image.jpg")
        if face_detected:
            print("Test Passed: Face detected successfully!")
        else:
            print("Test Failed: No face detected.")
    except Exception as e:
        print(f"Test Failed: An error occurred - {e}")

if __name__ == "__main__":
    test_webcam_facial_recognition()
