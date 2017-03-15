# -*- coding: utf-8 -*-

import click
import os
import subprocess
import threading
import time
import sys
import math
from pydub.silence import split_on_silence

from .factory import audio_segment_factory
from .animation import WaitingAnimation
from .splitter import SilenceSplitter
from .prompt import query_yes_no, query_integer

@click.command()
@click.argument('media_file', type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.option('--silence-longer', '-l', default=1000)
@click.option('--silence-regard', '-r', default=-15)
@click.option('--silence-trailing', '-t', default=500)
@click.option('--relative/--no-relative', default=False)
@click.option('--output-directory', '-o', default='./results')
@click.option('--yes', is_flag=True)
def cli(media_file, silence_longer, silence_regard, relative, silence_trailing, output_directory, yes):
    # Output Directory Check
    if(not os.path.isdir(output_directory)):
        if(query_yes_no('Output Directory not found, Can I make output directory', assumed=yes)):
            os.makedirs(output_directory)
            sys.stdout.write('Make Output Directory..Done!\n')
        else:
            sys.stdout.write('You must choose output directory. bye')
            sys.exit(1)

    sound = audio_segment_factory(media_file)
    while True:
        thresh = sound.dBFS + silence_regard if relative else silence_regard
        th_splitter = SilenceSplitter(
                sound,
                silence_longer,
                thresh,
                silence_trailing,
                )
        th_animation = WaitingAnimation()
        
        th_splitter.start()
        th_animation.start()
        chunks = th_splitter.join()
        th_animation.stop()

        sys.stdout.write('File was separete {0} files'.format(len(chunks)))
        if(query_yes_no('Output Separeted files?', assumed=yes)):
            for i, chunk in enumerate(chunks):
                chunk.export(output_directory + "/{0:03d}.flac".format(i), format="flac")
            sys.stdout.write('separeted done! Have a nice Day!')
            sys.exit(1)
        else:
            if(query_yes_no('Retry?')):
                silence_longer = query_integer('silence_longer?', 1000)
                silence_longer = query_integer('silence_regard?', -15)
                silence_longer = query_integer('silence_trailing?', 500)
            else:
                sys.stdout.write('ok! Thank you! good bye')
                sys.exit(1)
