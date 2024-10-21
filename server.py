from flask import Flask, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector')
def detect_emotions():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    response = f"For the given statement, the system response is "
    for key, value in emotions:
        if key != 'dominant_emotion':
            response += f"'{key}': {value}, "
    response = response[:-2] + f". The dominant emotion is {emotions['dominant_emotion']}."
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)