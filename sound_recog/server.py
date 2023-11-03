from flask import Flask,request,jsonify
from tensorflow.keras.models import load_model
import random
import librosa
from sklearn.preprocessing import LabelEncoder
import numpy as np
import os

app=Flask(__name__)
model=load_model('audio_classification.hdf5')
@app.route("/predict",methods=["POST"]) #we are allowing post 


def predict():
    #inputing the audio file
    audio_file=request.files["file"]# gives us access to this paricular file
    file_name=str(random.randint(0,100000)) #Random number
    audio_file.save(file_name)# file will be stored in the working directory
    #predictions=model.predict(file_name)

    #filename="D:\\sound_recog\\music\\bhairavi\\Bhairavi01.wav"

    #preprocess the audio file
    audio, sample_rate = librosa.load(file_name) 
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    #Reshape MFCC feature to 2-D array
    mfccs_scaled_features=mfccs_scaled_features.reshape(1,-1)
    #predicted_label=model.predict_classes(mfccs_scaled_features)

    ### Split the dataset into independent and dependent dataset
    #label=[]
    #y=np.array(label)
    ### Label Encoding -> Label Encoder
    #from tensorflow.keras.utils import to_categorical
    #from sklearn.preprocessing import LabelEncoder
    #labelencoder=LabelEncoder()
    #y=to_categorical(labelencoder.fit_transform(y))

    x_predict=model.predict(mfccs_scaled_features) 
    predicted_label=np.argmax(x_predict,axis=1)
    print(predicted_label)
    #prediction_class = labelencoder.inverse_transform(predicted_label) 
    print(prediction_class)
    os.remove(file_name)

    data={"prediction":predicted_label}
    return jsonify(data)

if __name__=="__main__":
    app.run(debug=False)
