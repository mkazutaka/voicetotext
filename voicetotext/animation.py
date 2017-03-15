# -*- coding: utf-8 -*-
import itertools
import time
import sys
import threading

class WaitingAnimation(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # Refer: http://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
        self.alive = True
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if not self.alive:
                break
            sys.stdout.write('\rspliting ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rspliting Done!\n')

    def stop(self):
        self.alive = False
        self.join()
