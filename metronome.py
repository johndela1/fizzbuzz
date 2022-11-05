#!/usr/bin/env python3

import subprocess
import time
from itertools import count



def say(word):
    w = word if type(word) == str else str(word)
    subprocess.Popen(
        ["say", w],
        stderr=subprocess.DEVNULL,
    )

for i in count():
    print(i)
    time.sleep(2)
