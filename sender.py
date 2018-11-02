from itertools import cycle
from time import sleep

import numpy as np
import zmq


def waveform_gen(length=10):
    waveforms = []
    for _ in range(5):
        waveforms.append(np.random.uniform(-1, 9, size=(length, )))
    return cycle(waveforms)

if __name__ == "__main__":
    ctx = zmq.Context()
    skt = ctx.socket(zmq.PUB)
    skt.bind('tcp://127.0.0.1:9000')

    print('Start sending...')

    waveform_gen = waveform_gen()
    for n in range(100):
        # sending data rate ~2 Hz
        skt.send(next(waveform_gen))
        sleep(0.5)
