import io
import os
import pandas as pd 
from google.cloud import vision

#Instantiates the client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client-file-visionai-demo.json'
client = vision.ImageAnnotatorClient()

# prepare the image (local source)
image_path = 'Images\pic2.jpg'
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)

# # prepare the image (web source)
# image_url = ''
# image = vision.Image()
# image.source.image_uri - image_url

response = client.face_detection(image=image)
faces = response.face_annotations
print(faces)
# Names of likelihood from google.cloud.vision.enums
# likelihood_name = (
#     "UNKNOWN",
#     "VERY_UNLIKELY",
#     "UNLIKELY",
#     "POSSIBLE",
#     "LIKELY",
#     "VERY_LIKELY",
# )
# print("Faces:")

# for face in faces:
#     print(f"anger: {likelihood_name[face.anger_likelihood]}")
#     print(f"joy: {likelihood_name[face.joy_likelihood]}")
#     print(f"surprise: {likelihood_name[face.surprise_likelihood]}")

#     vertices = [
#         f"({vertex.x},{vertex.y})" for vertex in face.bounding_poly.vertices
#     ]

#     print("face bounds: {}".format(",".join(vertices)))

# if response.error.message:
#     raise Exception(
#         "{}\nFor more info on error messages, check: "
#         "https://cloud.google.com/apis/design/errors".format(response.error.message)
#     )