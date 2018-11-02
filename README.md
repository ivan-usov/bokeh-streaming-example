# bokeh-streaming-example
A basic example of inter-process communication with a zmq sender (`sender.py`) and a zmq receiver integrated into a bokeh server application (`bokeh_receiver/`).

### Install dependencies
Depending on your package manager
```
$ conda install pyzmq bokeh
```
or
```
$ pip install pyzmq bokeh
```

### Run
Start the zmq sender and the bokeh receiver app as two separate processes
```
$ python sender.py
Start sending...
```

```
$ bokeh serve bokeh_receiver
2018-11-02 14:53:50,042 Starting Bokeh server version 1.0.1 (running on Tornado 5.1.1)
2018-11-02 14:53:50,044 Bokeh app running at: http://localhost:5006/bokeh_receiver
2018-11-02 14:53:50,044 Starting Bokeh server with process id: 8453
```
Navigate to `http://localhost:5006/bokeh_receiver` in your browser to see a dynamically updating plot.
