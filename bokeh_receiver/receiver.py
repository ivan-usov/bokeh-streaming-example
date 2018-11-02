from collections import deque

import numpy as np
import zmq

buffer = deque(maxlen=100)

def stream_receive():
    zmq_context = zmq.Context()
    zmq_socket = zmq_context.socket(zmq.SUB)
    zmq_socket.setsockopt_string(zmq.SUBSCRIBE, "")
    zmq_socket.connect("tcp://127.0.0.1:9000")

    poller = zmq.Poller()
    poller.register(zmq_socket, zmq.POLLIN)

    while True:
        events = dict(poller.poll(1000))
        if zmq_socket in events:
            waveform = np.frombuffer(zmq_socket.recv())
            buffer.append(waveform)
