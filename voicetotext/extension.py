# -*- coding: utf-8 -*-
import os.path

support_extensions = ['.mp4']

def is_support_extension(file_name):
    _, file_extension = os.path.splitext(file_name)
    print(file_extension)
    return True if file_extension in support_extensions else False
