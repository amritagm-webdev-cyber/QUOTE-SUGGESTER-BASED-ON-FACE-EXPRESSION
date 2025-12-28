from django.shortcuts import render
from django.http import StreamingHttpResponse
from deepface import DeepFace
import cv2
import random
from .quotes import quotes

camera = cv2.VideoCapture(0)

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def video_feed(request):
    return StreamingHttpResponse(
        gen_frames(),
        content_type='multipart/x-mixed-replace; boundary=frame'
    )

def index(request):
    emotion = None
    quote = None
    emotions = {}   # ✅ IMPORTANT: initialize

    if request.method == "POST":
        success, frame = camera.read()
        if success:
            cv2.imwrite("face.jpg", frame)

            result = DeepFace.analyze(
                img_path="face.jpg",
                actions=["emotion"],
                enforce_detection=False,
                detector_backend="opencv"
            )

            emotions = result[0]["emotion"]

            # Find emotion with highest confidence
            emotion = max(emotions, key=emotions.get)




            quote = random.choice(quotes.get(emotion, quotes["neutral"]))

    return render(request, "emotion/index.html", {
        "emotion": emotion,
        "quote": quote,
        "scores": emotions
    })
