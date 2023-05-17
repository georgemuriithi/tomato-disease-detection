# Tomato Disease Detection

<a href="https://github.com/georgemuriithi/tomato-disease-detection/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/georgemuriithi/tomato-disease-detection.svg?color=blue&cachedrop">
</a>

This is an end-to-end project in the agricultural domain. A Convolutional Neural Network (CNN) model is trained to detect whether a tomato plant has a particular disease by using a picture of its leaf. The model can be accessed from a mobile application or a web page.

## Mobile App
<p align="center">
  <img src="https://user-images.githubusercontent.com/21691211/171020330-ee6b21ff-000a-40f8-a887-9a09cd913671.png">
</p>

## Web Page
<p align="center">
  <img src="https://user-images.githubusercontent.com/21691211/171020296-97dcc7c1-8f43-430a-b2ea-1ddd60622334.png">
</p>

## Problem Description
Farmers face economic losses for failing to detect diseases in their tomato plants or giving them wrong treatments after making incorrect assumptions. It is also an additional cost to hire experts to investigate tomato plants and identify diseases.

## Solution Approach
A mobile app is developed to help farmers identify tomato diseases by taking pictures of tomato leaves. This is simple and accurate. The app uses a CNN model trained for image classification to identify tomato diseases through tomato leaves.

- Data Collection: <a href="https://www.kaggle.com/datasets/mohitsingh1804/plantvillage">Kaggle PlantVillage Dataset</a>
- <a href="https://github.com/georgemuriithi/tomato-disease-detection/blob/main/Tomato-Disease-Detection-Model.ipynb">Model Building</a>: TensorFlow, CNN, Data Augmentation
- MLOps: TensorFlow Serving, Docker
- Backend: FastAPI
- Frontend: React Native, React JS
- Deployment: GCP (Google Cloud Platform), GCF (Google Cloud Functions)

### Model Building & Performance
<a href="https://colab.research.google.com/drive/1-4BZ6qLznewBHl65NsbmWRswJijglM5w?usp=sharing">
  <img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg">
</a>

<p align="center">
  <img src="https://user-images.githubusercontent.com/21691211/217465060-e69f8ffa-4027-4ad8-a5ae-f314599f193c.png">
</p>

## Running Project Locally
### Setting up Local API
- ```cd apis/local```
- ```pip install -r requirements.txt```
- <a href="https://docs.docker.com/get-docker/">Install Docker</a>
- Get docker image for <a href="https://www.tensorflow.org/tfx/serving/docker">TensorFlow Serving</a>
- Run tensorflow serving docker image
- Serve a model by running the following command. Change the file path accordingly and add the appropriate config file at the end of the command. To serve the latest model, add ```all-models.config```. To serve a target model, add ```target-models.config```.
```
docker run -t --rm -p 8605:8605 -v C:\Users\User\tomato-disease-detection:/tomato-disease-detection tensorflow/serving --rest_api_port=8605 --allow_version_labels_for_unavailable_models --model_config_file=/tomato-disease-detection/config-files/
```
- Change the endpoint in ```apis/local/main.py``` accordingly, then run the file using an IDE or the following command:
```
uvicorn main:app --reload --host 0.0.0.0
```

### Running Mobile App
- ```cd mobile-app```
- ```yarn install```
- For macOS users only:
```
cd ios
pod install
cd ../
```
- <a href="https://reactnative.dev/docs/environment-setup">Set up an Emulator</a>
- Run the app using ```npm run android``` or ```npm run ios```

### Running Web Page
```
cd web-page
npm install
npm start
```

## Running Project using GCP
### Setting up GCP
- Create <a href="https://console.cloud.google.com/">GCP account</a>
- Create <a href="https://cloud.google.com/appengine/docs/standard/nodejs/building-app/creating-project">GCP project</a>
- Create <a href="https://cloud.google.com/storage/docs/creating-buckets">GCP bucket</a>
- Create ```models``` folder in the GCP bucket
- Upload ```tomato-disease-detection-model.h5``` model from ```models``` folder in the repo to ```models``` folder in the GCP bucket

### Deploying GCF
- Rename GCP bucket name in ```apis/gcf/main.py``` accordingly
- <a href="https://cloud.google.com/sdk/docs/install-sdk">Install Google Cloud CLI</a>
- <a href="https://cloud.google.com/sdk/docs/initializing">Initialize Google Cloud CLI</a>
- Deploy ```predict``` GCF using Google Cloud SDK Shell by running the following commands. Change the Python version and Project ID accordingly.
```
cd apis/gcf
gcloud functions deploy predict --runtime python310 --trigger-http --memory 512 --project project-id
```
- Enable Google Cloud Build API if necessary
- Get ```httpsTrigger url``` after deployment

### Running Mobile App & Web Page
- Change the url in the ```.env``` files to ```httpsTrigger url```
- Run accordingly
- Alternatively, install ```app-debug.apk``` from ```mobile-app/android/app/build/outputs/apk/debug``` on an Android device and run the Android mobile app

## Credits
@codebasics
