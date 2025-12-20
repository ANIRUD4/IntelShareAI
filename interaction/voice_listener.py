import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

class VoiceListener:
    """
    Offline voice listener for IntelShare.
    Listens ONLY when explicitly called by backend.
    """

    def __init__(self, model_path="models/vosk-model"):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.audio_queue = queue.Queue()

    def _callback(self, indata, frames, time, status):
        self.audio_queue.put(bytes(indata))

    def listen_once(self, duration=4):
        """
        Listen for a short duration and return recognized text.
        """
        with sd.RawInputStream(
            samplerate=16000,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=self._callback
        ):
            for _ in range(int(16000 / 8000 * duration)):
                data = self.audio_queue.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    return result.get("text", "")

        final = json.loads(self.recognizer.FinalResult())
        return final.get("text", "")
