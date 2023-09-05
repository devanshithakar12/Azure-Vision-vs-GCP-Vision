import io
import os
import pandas as pd 
from google.cloud import vision

#Instantiates the client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client-file-visionai-demo.json'
client = vision.ImageAnnotatorClient()

# prepare the image (local source)
image_path = 'Images\imgdata.jpg'
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)

response = client.face_detection(image=image)
faces = response.face_annotations
print(faces)
