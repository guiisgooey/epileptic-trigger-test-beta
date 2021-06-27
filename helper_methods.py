import os, urllib, urllib.request, math
from io import BytesIO
from PIL import Image

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
    if os.path.isfile(file_path):
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

def isvideo(file_path):
    pass

def t_test(image1, image2):
    """Performs a Student's t-test for the provided images."""
    num = image1.rms[0] - image2.rms[0]
    denom = math.sqrt(((image1.stddev[0]**2)/image1.count[0]) + ((image2.stddev[0]**2)/image2.count[0]))
    if denom == 0:
        return 0
    t = num / denom
    if t < 0:
        t *= -1
    return t