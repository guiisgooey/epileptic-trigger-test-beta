import cv2, math, urllib.request
from io import BytesIO
from PIL import Image, ImageStat
from helper_methods import isurl, t_test, isvideo

def frame_brightness_test(file_path):
    """Converts provided GIF into individual frames and compares frames to see if it is flashing."""
    e = False
    last_stat = None
    i = 0
    if(isvideo(file_path)):
        pass
    if(isurl(file_path)):
        file_path = BytesIO(urllib.request.urlopen(file_path).read())
    cap = cv2.VideoCapture(file_path)
    x = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    threshold = math.ceil(x / 20)
    if x == 1:
        return e
    for _ in range(x):
        if e == True:
            return e
        _, image = cap.read()
        _, buf = cv2.imencode(".png", image)
        frame_obj = BytesIO(buf)        
        frame = Image.open(frame_obj)
        stat = ImageStat.Stat(frame)
        if last_stat:
            t = t_test(stat, last_stat)
            if (t >= (stat.count[0] * .000625)):
                i += 1
                if i >= threshold:
                    e = True
        last_stat = stat      
    return e