# Video to GIF Converter

## function
- clip
- crop
- rotate
- resize
- fps

## enviroment
```
Windows 10
Python 3.9.2
MoviePy 1.0.3
```
## .env settings
default value(.env)
```
filename_in='input.mp4'
filename_out='output.gif'
t_start=0.0
t_end=5.0
x_center=-1
y_center=-1
width=800
height=800
rotate_degree=0
size_rate=0.5
program='ffmpeg'
fps=15
```
var(type): description
- filename_in(str): input file name(video such as .mp4)
- filename_out(str): output file name(.gif)
- t_start(float): clip start time(seconds)
- t_end(float): clip end time(seconds)
- x_center(int): crop center position x(-1: video center)
- y_center(int): crop center position y(-1: video center)
- width(int): crop width(-1: clip size)
- height(int): crop height(-1: clip size)
- rotate_degree(float): degree of rotation
- size_rate(float): the adjustment rate after cropping
- program(str): 'ffmpeg' or 'imageio'
- fps(int): frames per second
