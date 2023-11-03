import requests
from flask import Flask,request,jsonify
URL="http://127.0.0.1:5000//predict"# The link provided, running in the local host
TEST_AUDIO_FILE_PATH="D://sound_recog//music//bhairavi//Bhairavi01.wav"

if __name__=="__main__":
    audio_file=open(TEST_AUDIO_FILE_PATH,"rb")
    values={"file":(TEST_AUDIO_FILE_PATH,audio_file,"audio/wav")}
    response=requests.post(URL,files=values)
    data=response.json()
    print(f"predicted keyword is: {data['keyword']}")
