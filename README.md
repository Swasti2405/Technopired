# 🧠🎮 Technopired  
## Gamified Multimodal Learning Platform for Dyslexic Children  

> “Making learning inclusive through gamification and multimodal interaction.”

---

## 📌 Overview  

Technopired is a **gamified, web-based assistive learning platform** designed specifically for **children with dyslexia**. The system integrates **speech interaction, gesture control, and eye tracking** to provide an accessible and engaging educational experience.  

By combining **multimodal interaction with game-based learning**, Technopired reduces reliance on traditional text-heavy methods and enables children to learn through **audio, visual, and interactive feedback loops**.  

---

## 🎯 Core Capabilities  

The platform provides three key learning pathways:

- 🎤 **Speech-Based Learning**  
  Listen → Repeat → Evaluate workflow using speech recognition and text-to-speech  

- ✋ **Gesture-Based Interaction**  
  Hand tracking using MediaPipe for non-traditional input  

- 👁️ **Eye & Blink-Based Control**  
  Gaze detection and blink selection using OpenCV + dlib  

These modalities allow children to interact with the system in ways that align with their cognitive strengths.  

---

## 🧠 Problem Statement  

Children with dyslexia often face challenges with:

- Reading fluency and comprehension  
- Text-heavy educational tools  
- Limited engagement with traditional methods  

Most existing tools are:

- Not adaptive to diverse learning styles  
- Not interactive or engaging  
- Not designed for assistive multimodal interaction  

Technopired addresses these gaps by:

- Reducing reliance on text-heavy learning  
- Providing audio-visual and interactive pathways  
- Introducing gamification to improve engagement and retention  

---

## 🎮 Key Features  

### 1. Gamified Learning Modules  
- Interactive activities  
- Encourages engagement through repetition and reward  

### 2. Speech Recognition & Feedback  
- Converts text to speech using gTTS  
- Captures user speech via microphone  
- Evaluates correctness using Google Speech Recognition  

### 3. Hand Gesture Control  
- Real-time hand tracking via MediaPipe  
- Enables interaction without keyboard/mouse  

### 4. Eye & Blink Tracking  
- Eye gaze detection using dlib landmark model  
- Blink-based selection system  

### 5. Web-Based Interface  
- Built with Flask  
- User authentication and session management  
- Interactive learning pages  

---

## 🏗️ System Overview  

The system consists of three major components:

### 1. Web Application (Flask)
Handles:
- Routing  
- User authentication  
- UI rendering  

### 2. Interaction Modules
- `NEW.py` → Gesture-based interaction  
- `gaze.py` / `gaze1.py` → Eye tracking modules  

### 3. Speech Engine
- gTTS for speech output  
- SpeechRecognition for input evaluation  

---

## 📊 Learning Flow  
User Input → Interaction Mode → Feedback → Reinforcement

---

## 📂 Repository Structure  
```bash
Technopired/
│
├── app.py # Main Flask application
├── NEW.py # Hand gesture module
├── gaze.py # Eye tracking module
├── gaze1.py # Alternate gaze implementation
├── databse.db # SQLite database
├── shape_predictor_68_face_landmarks.dat
│
├── templates/ # HTML templates
├── IMG/ # Images
├── CMake/ # Config files
│
├── input_audio.wav # Recorded audio
├── voice.mp3 # Generated audio
```

---

## ⚙️ Installation & Setup  

### 1. Clone Repository  
```bash
git clone https://github.com/Swasti2405/Technopired.git
cd Technopired
```

2. Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install flask opencv-python dlib mediapipe pygame gtts speechrecognition sounddevice numpy mutagen
```

4. Run Application
```bash
python app.py
```

Open browser:
```bash
http://127.0.0.1:5000
```

## 🧪 Core Functionalities

1. Speech Learning Module
- System speaks a sentence
- User repeats it
- System evaluates correctness
2. Gesture Interaction Module
- Webcam-based hand tracking
- Enables gesture-controlled interaction
3. Eye Tracking Module
- Detects gaze direction
- Uses blinking for selection

---

## 📈 Project Highlights

- 🎯 Target Users: Dyslexic children
- 🧠 Learning Modes: 3 (Speech, Gesture, Eye Tracking)
- 🎮 Gamified Modules: Multiple interactive activities
- 🔬 Assistive Technologies: Integrated multimodal system

---

## ⚠️ Limitations

- Windows-dependent subprocess execution
- Requires webcam and microphone
- Passwords currently stored in plaintext
- Large model files included in repository

---

### 🚀 Future Improvements
- Secure authentication (password hashing)
- Cross-platform compatibility
- Unified interface without external scripts
- Cloud deployment support
- Improved accuracy of gesture and gaze detection
- Personalized learning adaptation

---

## 🧰 Technologies Used
- Python
- Flask
- OpenCV
- dlib
- MediaPipe
- Google Text-to-Speech (gTTS)
- SpeechRecognition
- SQLite
- Pygame

---

## 🤝 Contributors

- Swasti Sadanand
- Rubini Pramod Avalakki
- Sameeksha BH
- Sonia Puri

---

## 📜 License

This project is developed for academic and research purposes.

