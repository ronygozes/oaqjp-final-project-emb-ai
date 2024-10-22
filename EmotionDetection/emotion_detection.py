import json
import requests


def emotion_detector(text_to_analyse):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json =  { "raw_document": { "text": text_to_analyse } }
    # print('im here')
    response = requests.post(url, json = input_json, headers=headers, timeout=2.50)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }
    response = json.loads(response.text)
    emotions = response['emotionPredictions'][0]['emotion']
    max_value = max(emotions.values())
    for key, value in emotions.items():
        if value == max_value:
            emotions['dominant_emotion'] = key
            break
    return emotions
