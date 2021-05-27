import os, math, urllib, urllib.request
from os.path import isfile
from io import BytesIO
from PIL import Image, ImageStat

def frame_test(file_path):
    """Converts provided GIF into individual frames and compares frames to see if it is flashing."""
    e = False
    t = 0
    last_stat = None
    x = 0
    i = 0
    assert(isgif(file_path)==True)
    if(isurl(file_path)):
        file_path = BytesIO(urllib.request.urlopen(file_path).read())
    im = Image.open(file_path)
    x = im.n_frames
    threshold = math.ceil(x / 3)
    if x == 1:
        return False
    for i in range(x):
        if e == True:
            return e
        im.seek(i)
        frames_obj = BytesIO()
        im.save(frames_obj, 'PNG')
        frame = Image.open(frames_obj)
        stat = ImageStat.Stat(frame)
        if last_stat:
            t = t_test(stat, last_stat)
            if(t >= (stat.count[0] * .000625)):
                i += 1
                if i >= threshold:
                    e = True
        last_stat = stat
    return e

def isurl(file_path):
    """Checks if the provided file path is a url."""
    try:
        req = urllib.request.urlopen(file_path)
        status = req.getcode()
        if status == 200:
            return True
        else:
            return False
    except:
        return False

def isgif(file_path):
    """Checks if file path directs to a gif or list of frames."""
    file_ext = ''
    if isfile(file_path):
        try:
            file_ext = os.path.splitext(file_path)[1]
        except:
            print("Unable to resolve file path.")
        if file_ext == '.gif':
            return True
        else:
            print('The provided file is not a suitable GIF image. \n Please ensure that you are using a GIF filetype image.')
            return False
    elif isurl(file_path):
        try:
            file_ext = os.path.splitext(file_path)[1]
        except:
            print("Unable to resolve URL path.")
        if file_ext == '.gif':
            return True
        else:
            print('The provided URL is not to a suitable GIF image. \n Please ensure that you are linking to the image itself and not a webpage displaying the image.')
            return False
    elif isinstance(file_path, BytesIO):
        try:
            Image.open(file_path)
            return True
        except:
            print("The provided BytesIO file is not a suitable image file.")
            return False
    elif isinstance(file_path, list):
        try:
            Image.open(file_path[0]) 
            return True
        except:
            print("The provided list is not made up of suitable images.")
            return False    
    else:
        print('The provided file path is not a file, url, BytesIO file or a list of images. \n Please ensure you are providing one of these data types.')
        return False

def t_test(image1, image2):
    """Performs a Student's t-test for the provided images."""
    num = image1.rms[0] - image2.rms[0]
    denom = math.sqrt((image1.stddev[0]**2/image1.count[0]) + (image2.stddev[0]**2/image2.count[0]))
    t = num / denom
    if t < 0:
        t *= -1
    return t
    