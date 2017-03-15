#!/usr/bin/env python
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# Edited by Kazutaka Matsumoto
# based file: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/speech/api-client/transcribe.py
# ChangeLog
# - Delete Comment
# - Delete __main__ function
# - change main funciton name and arugment
# - add return text

"""Google Cloud Speech API sample application using the REST API for batch
processing.

Example usage: python transcribe.py resources/audio.raw
"""

import argparse
import base64
import json

import googleapiclient.discovery

def get_speech_service():
    return googleapiclient.discovery.build('speech', 'v1beta1')


def get_speech_text(speech_file, encoding="FLAC", sample_rate=48000, language_code="en-US"):
    """Transcribe the given audio file.

    Args:
        speech_file: the name of the audio file.
        encoding: encode audio file
        sample_rate: bitrate
        language_code: return language
    """
    with open(speech_file, 'rb') as speech:
        # Base64 encode the binary audio file for inclusion in the JSON
        # request.
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                # There are a bunch of config options you can specify. See
                # https://goo.gl/KPZn97 for the full list.
                'encoding': encoding,
                'sampleRate': sample_rate,
                # See http://g.co/cloud/speech/docs/languages for a list of
                # supported languages.
                'languageCode': language_code,
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })
    response = service_request.execute()

    # First print the raw json response
    # print(json.dumps(response, indent=2))

    results = []
    for result in response.get('results', []):
        for alternative in result['alternatives']:
            results.append(alternative['transcript'])
    return results
