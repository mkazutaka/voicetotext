# -*- coding: utf-8 -*-
import threading
from pydub.silence import split_on_silence

class SilenceSplitter(threading.Thread):
    def __init__(self, audio_segment,
            min_silence_len=1000,
            silence_thresh=-16,
            keep_silence=100):
        threading.Thread.__init__(self)
        self.audio_segment = audio_segment
        self.min_silence_len = min_silence_len
        self.silence_thresh = silence_thresh
        self.keep_silence = keep_silence
        self.chunks = None

    def run(self):
        self.chunks = split_on_silence(
                self.audio_segment,
                self.min_silence_len,
                self.silence_thresh,
                self.keep_silence,
                )
        print(len(self.chunks))

    def join(self):
        threading.Thread.join(self)
        return self.chunks
