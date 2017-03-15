# -*- coding: utf-8 -*-
import os.path
from pydub import AudioSegment

def audio_segment_factory(file_name):
    _, extension = os.path.splitext(file_name)
    extension = extension[1:]
    return AudioSegment.from_file(file_name, extension)
