!pip install pydub
from pydub import AudioSegment

def detect_ai_audio(audio_path):
    sound = AudioSegment.from_file(audio_path)
    return sound.duration_seconds

