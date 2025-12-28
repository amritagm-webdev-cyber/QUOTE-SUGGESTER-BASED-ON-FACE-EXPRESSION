# 😊 MoodSense – AI-Based Mood Detection & Quote Recommendation System

## 📌 Project Overview

**MoodSense** is an AI-powered web application that detects a user’s mood in real time using facial expression analysis and recommends personalized motivational quotes. The system combines **computer vision**, **deep learning**, and **web development** to create an interactive and emotionally aware user experience.

---

## 🎯 Problem Statement

Most motivational platforms provide generic content without understanding the user’s emotional state. Users often struggle to identify or express their emotions, leading to ineffective engagement.
MoodSense addresses this by **automatically analyzing facial expressions** and delivering **emotion-specific quotes**.

---

## 💡 Solution

The application captures live webcam input, analyzes facial expressions using a deep learning model, determines the most probable emotion, and displays a quote tailored to the detected mood. The system also visualizes emotion confidence levels to ensure transparency and trust.

---

## ✨ Key Features

* ✅ Real-time **live webcam preview** inside the browser
* ✅ AI-based **facial emotion detection** using DeepFace
* ✅ **Probability-based emotion selection** for improved accuracy
* ✅ Emotion confidence visualization using progress bars
* ✅ Personalized **motivational quotes** for each mood
* ✅ Clean, responsive, and modern UI using Bootstrap
* ✅ Graceful handling of AI uncertainty

---

## 🧠 Emotions Detected

* Happy
* Sad
* Angry
* Fear
* Surprise
* Neutral
* Disgust

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, Bootstrap 5
* **Backend:** Django (Python)
* **Computer Vision:** OpenCV
* **Deep Learning:** DeepFace (CNN-based models)
* **Streaming:** MJPEG video streaming via Django
* **Database:** SQLite (extendable to PostgreSQL / MySQL)

---

## ⚙️ System Workflow

* User opens the web application
* Live webcam stream is displayed in the browser
* User clicks **Analyze My Mood**
* A frame is captured from the webcam
* Facial expression is analyzed using DeepFace
* Emotion probabilities are computed
* The most confident emotion is selected
* A matching motivational quote is displayed

---

## 📊 Emotion Decision Logic

* Emotion prediction is based on **maximum probability**, not hard-coded rules
* Low-confidence predictions are safely mapped to **Neutral**
* Emotion confidence percentages are shown to the user

This approach improves reliability and user trust.

---

## 🖼️ User Interface Highlights

* Live camera preview
* One-click mood analysis
* Emotion confidence bars
* Clear mood label and quote display
* Mobile-friendly layout

---

## 🚀 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/moodsense.git

# Navigate to project folder
cd moodsense

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install django deepface opencv-python tensorflow tf-keras pillow

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

Open browser:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
