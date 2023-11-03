# Testing of model:

from tensorflow.keras.models import load_model

model=load_model('audio_classification.hdf5')
filename="D:\\sound_recog\\music\\bhairavi\\Bhairavi01.wav"
audio, sample_rate = librosa.load(file_name) 
mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
#Reshape MFCC feature to 2-D array
mfccs_scaled_features=mfccs_scaled_features.reshape(1,-1)

x_predict=model.predict(mfccs_scaled_features) 
predicted_label=np.argmax(x_predict,axis=1)
print(predicted_label)