from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import sqlite3
import speech_recognition as sr
import sounddevice as sd
import wave
import numpy as np
import subprocess
import pygame
import time
from gtts import gTTS
from mutagen.mp3 import MP3
import time


def Play(text1):
    print('\n------------Entered text--------------\n')
    print(text1)
    myobj = gTTS(text=text1, lang='en-us', tld='com', slow=False)
    myobj.save("voice.mp3")
    print('\n------------Playing--------------\n')
    song = MP3("voice.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load('voice.mp3')
    pygame.mixer.music.play()
    time.sleep(song.info.length)
    pygame.quit()


app = Flask(__name__)
app.secret_key = "your_secret_key"

def create_database():
    conn = sqlite3.connect("databse.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

create_database()  

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("userlog.html")

@app.route('/seasaw')
def seasaw():
    return render_template("home.html")

@app.route('/dice')
def dice():
    return render_template("dice.html")

@app.route('/texttospeech')
def texttospeech():
    return render_template("texttospeech.html")

@app.route('/gesture')
def gesture():
    subprocess.Popen(['start', 'cmd', '/k', 'python NEW.py'], shell=True)
    return redirect(url_for('seasaw'))

@app.route('/eyeblink')
def eyeblink():
    subprocess.Popen(['start', 'cmd', '/k', 'python gaze1.py'], shell=True)
    return redirect(url_for('seasaw'))

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        conn = sqlite3.connect("databse.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (username, email, phone, password) VALUES (?, ?, ?, ?)", 
                        (username, email, phone, password))
        conn.commit()
        return render_template("index.html", msg = "Signup successful! Please log in.")
    return render_template('index.html')

@app.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect("databse.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=? and password = ?", (email,password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(url_for('home'))
        else:
            return render_template("index.html", msg = "Entered wrong email or password")
    return render_template("index.html")

@app.route('/textspeech', methods=['POST', 'GET'])
def textspeech():
    check = request.args.get("text").lower()
    Play(check)
    while True:
        Play('Speak')
        duration = 5
        fs = 44100
        channels=2
        filename="input_audio.wav"
        print("Recording...")
        audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype=np.int16)
        sd.wait()
        print("Recording complete.")

        # Save the recorded audio to a WAV file
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(2)
            wf.setframerate(fs)
            wf.writeframes(audio_data.tobytes())

        # Perform speech recognition
        recognizer = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data).lower()
                print("Recognized text:", text)
                break
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
    if text == check:
        Play("correct. moving to the next sentence")
        return jsonify(True)
    else:
        Play("Incorrect. Try again.")
        return jsonify(False)

if __name__ == "__main__":
    print("http://127.0.0.1:5000/")
    app.run(debug=True, use_reloader=False)
