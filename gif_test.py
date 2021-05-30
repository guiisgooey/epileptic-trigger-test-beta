import math, urllib.request
from io import BytesIO
from PIL import Image, ImageStat
from helper_methods import isurl, isgif, t_test

def frame_brightness_test(file_path):
    """Converts provided GIF into individual frames and compares frames to see if it is flashing."""
    e = False
    last_stat = None
    n = 0
    assert(isgif(file_path)==True)
    if(isurl(file_path)):
        file_path = BytesIO(urllib.request.urlopen(file_path).read())
    im = Image.open(file_path)
    x = im.n_frames
    threshold = math.ceil(x / 10)
    if x == 1:
        return e
    for i in range(x):
        if e == True:
            return e
        im.seek(i)
        frames_obj = BytesIO()
        im.save(frames_obj, 'PNG')
        frame = Image.open(frames_obj)
        stat = ImageStat.Stat(frame)
        if(last_stat):
            t = t_test(last_stat, stat)
            if(t >= (stat.count[0] * .000625)):
                i += 1
                if i >= threshold:
                    e = True
        last_stat = stat
    return e