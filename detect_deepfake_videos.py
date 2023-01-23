!pip install deepfake-detection-tool

from deepfake_detection.detector import Detector

detector = Detector()

def detect_deepfake(video_path):
    result = detector.detect(video_path)
    return result

