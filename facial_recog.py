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

        