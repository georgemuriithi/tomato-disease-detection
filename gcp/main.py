# importing packages
from google.cloud import storage
import tensorflow as tf
import numpy as np
from PIL import Image

model = None  # declaring model
BUCKET_NAME = 'tf-models-1'  # declaring gcp bucket name
# declaring class names
class_names = ['Bacterial-spot', 'Early-blight', 'Healthy', 'Late-blight',
               'Leaf-mold', 'Mosaic-virus', 'Septoria-leaf-spot', 'Yellow-leaf-curl-virus']


# downloading model from gcp
def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)


# predicting image
def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            'models/tomato-disease-detection-model.h5',
            '/tmp/tomato-disease-detection-model.h5'
        )
        model = tf.keras.models.load_model('/tmp/tomato-disease-detection-model.h5')

    img = request.files['file']
    img_array = np.array(Image.open(img).convert('RGB').resize((256, 256)))  # converting image to numpy array
    img_array = img_array / 255  # rescaling image
    img_batch = tf.expand_dims(img_array, axis=0)  # creating image batch for prediction

    # image prediction
    pred = model.predict(img_batch)
    pred_class = class_names[np.argmax(pred[0])]  # getting predicted class
    pred_conf = round(100 * np.max(pred[0]), 2)  # getting prediction confidence

    return {
        'predClass': pred_class,
        'predConf': pred_conf
    }
