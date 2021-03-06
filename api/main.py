# importing packages
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
# import tensorflow as tf
from PIL import Image
from io import BytesIO
import numpy as np
import requests
import uvicorn

app = FastAPI()  # creating FastAPI instance

# allowing requests from port 3000 for React UI
origins = [
    'http://localhost',
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# using version name
endpoint = 'http://localhost:8605/v1/models/tomato_disease_detection_model/labels/production:predict'
# using version number (trial)
# endpoint = 'http://localhost:8605/v1/models/tomato_disease_detection_model/labels/1:predict'
# using latest model
# endpoint = 'http://localhost:8605/v1/models/tomato_disease_detection_model:predict'

# model = tf.keras.models.load_model('../models/2')  # loading model

# declaring class names
class_names = ['Bacterial-spot', 'Early-blight', 'Healthy', 'Late-blight',
               'Leaf-mold', 'Mosaic-virus', 'Septoria-leaf-spot', 'Yellow-leaf-curl-virus']


# testing connection
@app.get('/ping')
async def ping():  # asynchronous and non-blocking
    return 'Hello!'


# predicting image
@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    file_bytes = await file.read()  # preventing blocking
    img = Image.open(BytesIO(file_bytes))  # converting bytes to image
    img_array = np.array(img)  # converting image to numpy array
    img_batch = np.expand_dims(img_array, axis=0)  # creating image batch for prediction

    # image prediction
    # pred = model.predict(img_batch)[0]
    json_data = {
        'instances': img_batch.tolist()
    }
    response = requests.post(endpoint, json=json_data)
    pred = response.json()['predictions'][0]

    pred_class = class_names[np.argmax(pred)]  # getting predicted class
    pred_conf = np.max(pred)  # getting prediction confidence
    return {
        'predClass': pred_class,
        'predConf': float(pred_conf)
    }


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
