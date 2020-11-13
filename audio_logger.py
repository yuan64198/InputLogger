import wave
import threading

import pyaudio

from utils import get_timestamp, print_message
from constants import (AUDIO_LOG_FILENAME,
                    AUDIO_LOG_INTERVAL, 
                    CHUNK, 
                    NUM_CHANNEL, 
                    FS,
                    AUDIO_DIR,)



class AudioLogger(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.frames = []
        self.stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                channels=NUM_CHANNEL,
                rate=FS,
                frames_per_buffer=CHUNK,
                input=True)
    

    def save_audio_every_timeframe(self):
        for _ in range(100000):
            self.read_audio()
            self.save_audio()
            self.clear_buffer()


    def read_audio(self):
        for _ in range(0, int(FS / CHUNK * AUDIO_LOG_INTERVAL)):
            data = self.stream.read(CHUNK)
            self.frames.append(data)


    def save_audio(self):
        filename = AUDIO_LOG_FILENAME + "_" + get_timestamp() + ".wav"
        wf = wave.open(AUDIO_DIR+filename, 'wb')
        wf.setnchannels(NUM_CHANNEL)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(FS)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print_message("Save audio file to " + AUDIO_DIR+filename)

    def clear_buffer(self):
        self.frames = []

    def run(self):
        print_message("===== Start Recording Audio =====")
        self.save_audio_every_timeframe()