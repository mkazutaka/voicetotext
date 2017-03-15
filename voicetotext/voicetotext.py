import click
import argparse
import base64
import json
import time
import codecs
import sys
import glob

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials

from .transcribe import get_speech_text

@click.command()
@click.argument('target-directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--files-extension', '-f', default="flac")
@click.option('--encoding', '-e', default="FLAC")
@click.option('--sample_rate', '-s', default=48000)
@click.option('--language-code', '-l', default='en-US')
@click.option('--output-file', '-o', default='result.txt')
@click.option('--display/--no-display', default=True)
def cli(target_directory, files_extension, encoding, sample_rate, language_code, output_file, display):
    target_files = glob.glob(target_directory + '/*.' + files_extension)
    for f in target_files:
        text_list = get_speech_text(f,
                encoding=encoding,
                sample_rate=sample_rate,
                language_code=language_code)
        with open(output_file, 'a') as f:
            text = '\n'.join(text_list) + '\n'
            if display:
                print(text, end='')
            f.write('\n'.join(text_list) + '\n')
