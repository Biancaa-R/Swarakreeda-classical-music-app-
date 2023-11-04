import requests
from flask import Flask,request,jsonify
URL="http://127.0.0.1:5000//predict"# The link provided, running in the local host
import sounddevice
from scipy.io.wavfile import write
fs= 44100
second =  int(input("Enter time duration in seconds: "))
# Temporary option
print("Recording.....n")
record_voice = sounddevice.rec( int ( second * fs ) , samplerate = fs , channels = 2 )
sounddevice.wait()
write("out.wav",fs,record_voice)
print("Finished.....Please check your output file")


#TEST_AUDIO_FILE_PATH="D://sound_recog//music//bhairavi//Bhairavi01.wav"
TEST_AUDIO_FILE_PATH="C:\\Users\\Biancaa. R\\flask app\\out.wav"
if __name__=="__main__":
    audio_file=open(TEST_AUDIO_FILE_PATH,"rb")
    values={"file":(TEST_AUDIO_FILE_PATH,audio_file,"audio/wav")}
    response=requests.post(URL,files=values)
    data=response.json()
    print(f"predicted category is: {data['prediction']}")
