import os
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import crop
import time

start = time.time()
print('loadding... ', end='')
load_dotenv()
settings = {
    'filename_in': os.getenv('filename_in'),
    'filename_out': os.getenv('filename_out'),
    't_start': float(os.getenv('t_start')),
    't_end': float(os.getenv('t_end')),
    'x_center': int(os.getenv('x_center')),
    'y_center': int(os.getenv('y_center')),
    'width': int(os.getenv('width')),
    'height': int(os.getenv('height')),
    'rotate': float(os.getenv('rotate_degree')),
    'rate': float(os.getenv('size_rate')),
    'program': os.getenv('program'),
    'fps': int(os.getenv('fps'))
}
end = time.time()
print(f'{end - start}s done.\nclipping1... ', end='')
start = time.time()
clip = (VideoFileClip(settings['filename_in']))#fucking slow
end = time.time()
print(f'{end - start}s done.\nclipping2... ', end='')
start = time.time()
clip = clip.subclip(t_start=settings['t_start'], t_end=settings['t_end'])
end = time.time()
print(f'{end - start}s done.\ncropping... ', end='')
start = time.time()
(w, h) = clip.size
if settings['x_center'] < 0:
    settings['x_center'] = w/2
if settings['y_center'] < 0:
    settings['y_center'] = h/2
if settings['width'] < 0:
    settings['width'] = w
if settings['height'] < 0:
    settings['height'] = h
cropped_clip = crop(clip, x_center=settings['x_center'], y_center=settings['y_center'], width=settings['width'], height=settings['height'])
if settings['rotate'] != 0:
    cropped_clip = cropped_clip.rotate(settings['rotate'])
if settings['rate'] != 1.0:
    cropped_clip = cropped_clip.resize(settings['rate'])
end = time.time()
print(f'{end - start}s done.\noutput...')
start = time.time()
cropped_clip.write_gif(settings['filename_out'], program=settings['program'], fps=settings['fps'])
# cropped_clip.write_gif('output2.gif', program='imageio', fps=settings['fps'])
end = time.time()
print(f'{end - start}s done.')
