import boto3
import cv2
import os

class FacialRecognition:
    @staticmethod
    def capture_image(save_path="captured_image.jpg"):
        """
        Captures an image from the webcam and saves it to the specified path.
        Returns the path to the captured image.
        """
        # Open the webcam
        cam = cv2.VideoCapture(0)  # Use 0 for default webcam
        if not cam.isOpened():
            raise Exception("Could not open webcam.")
        
        print("Capturing image...")
        ret, frame = cam.read()
        if not ret:
            raise Exception("Failed to capture image.")
        
        # Save the captured frame
        cv2.imwrite(save_path, frame)
        cam.release()
        print(f"Image saved to {save_path}")
        return save_path

    @staticmethod
    def face_recog(image_path):
        """
        Detects faces in the image using AWS Rekognition.
        Returns a boolean indicating whether a face is detected.
        """
        client = boto3.client('rekognition')

        with open(image_path, 'rb') as image:
            response = client.detect_faces(
                Image={'Bytes': image.read()},
                Attributes=['DEFAULT']
            )

        if not response['FaceDetails']:
            print("No faces detected.")
            return False

        print("Face detected!")
        return True

    @staticmethod
    def detect_face_with_webcam(save_path="captured_image.jpg"):
        """
        Captures an image using the webcam and detects faces in it.
        Returns a boolean indicating whether a face is detected.
        """
        try:
            # Capture image from webcam
            image_path = FacialRecognition.capture_image(save_path)
            # Detect faces in the captured image
            return FacialRecognition.face_recog(image_path)
        finally:
            # Clean up by removing the saved image
            if os.path.exists(save_path):
                os.remove(save_path)



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
        
