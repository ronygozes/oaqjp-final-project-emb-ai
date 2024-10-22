from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotions():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    emotions_list = list(emotions.items())
    for em in emotions_list:
        if em[0] == 'dominant_emotion':
            emotions_list.remove(em)
            break
    response = f"For the given statement, the system response is "
    for i in range(len(emotions_list)-1):
        response += f"'{emotions_list[i][0]}': {emotions_list[i][1]}, "
    response = response[:-2] + f" and '{emotions_list[-1][0]}': {emotions_list[-1][1]}."
    response += f" The dominant emotion is <b>{emotions['dominant_emotion']}</b>."
    return response

if __name__ == '__main__':
    app.run(debug=True)