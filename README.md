# Disease-severity-prediction

It is a web application that is developed using django to predict the disease and severity (benign or malignant) based on the symptoms collected from the user.
This web app can be divided into two modules: **Disease prediction** and **Severity prediction**.

## Disease prediction

This module can be found in the folder disease-prediction. This module uses decision tree to predict the disease based on the five symptoms collected from the user.

Following diseases will be predicted:
* Cardio-disease
* Jaundice
* Allergy
* Common cold
* Diabetes
* Hepatitis C
* Hypothyroidism

## Disease severity

AutoML is used to train models for predicting the severity (benign or malignant). Datasets are collected for each of the seven diseases.
Severity feature is computed based on the feature importance. Separate model is trained for each of the seven diseases.

AutoMl library used - mljar-supervised

Link: https://mljar.com/automl/

## Datasets

Datasets can be found in the repository.

   

