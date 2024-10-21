import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        text = 'I am glad this happened'
        self.assertEqual(emotion_detector(text)['dominant_emotion'], 'joy')

        text = 'I am really mad about this'
        self.assertEqual(emotion_detector(text)['dominant_emotion'], 'anger')

        text = 'I feel disgusted just hearing about this'
        self.assertEqual(emotion_detector(text)['dominant_emotion'], 'disgust')

        text = 'I am so sad about this'
        self.assertEqual(emotion_detector(text)['dominant_emotion'], 'sadness')

        text = 'I am really afraid that this will happen'
        self.assertEqual(emotion_detector(text)['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
