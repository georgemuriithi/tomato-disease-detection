# Tomato Disease Detection

<a href="https://github.com/georgemuriithi/tomato-disease-detection/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/georgemuriithi/tomato-disease-detection.svg?color=blue&cachedrop">
</a>

This is an end to end project in the agricultural domain. A CNN model is trained to detect whether a tomato plant has a particular disease by using a picture of its leaf. The model can accessed from a mobile app or a web page.

## Mobile App
![Screenshot_20220530_213621(1)](https://user-images.githubusercontent.com/21691211/171020330-ee6b21ff-000a-40f8-a887-9a09cd913671.png)

## Web Page
![Screenshot 2022-05-30 220714(1)](https://user-images.githubusercontent.com/21691211/171020296-97dcc7c1-8f43-430a-b2ea-1ddd60622334.png)

## Problem Description
Farmers face economic losses for failing to detect diseases in their tomato plants or giving them wrong treatments after making incorrect assumptions. It is also an additional cost to hire experts to investigate tomato plants and identify diseases.

## Solution Approach
A mobile app is developed to help farmers identify tomato diseases by taking pictures of tomato leaves. This is simple and accurate. The app uses a CNN model trained for image classification to identify tomato diseases through tomato leaves.

- Data Collection: <a href="https://www.kaggle.com/datasets/mohitsingh1804/plantvillage">Kaggle PlantVillage Dataset</a>
- Model Building: Tensorflow, CNN, Data Augmentation
- MLOps: TensorFlow Serving, Docker
- Backend: FastAPI
- Frontend: React JS, React Native
- Deployment: GCP (Google Cloud Platform), GCF (Google Cloud Functions)
