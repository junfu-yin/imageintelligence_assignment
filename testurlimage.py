from PIL import Image
import requests
from io import BytesIO
import sys

import urllib.request
import numpy as np

import cv2




def getimage(url = 'http://google.com.au'):
    print('get image from '+ url)
    try:
        response = requests.get(url)
    except:
        response = sys.exc_info()[0]
        pass
    # print('fefefefefe')
    response = str(response)
    # print('error type:\t'+str(response))

    img = None

    if ('MissingSchema' in response):
        return 'MissingSchema', img
    if ('ConnectionError' in response):
        return 'ConnectionError', img
    if ('404' in response):
        return 'NotFound', img

    if ('200' in response):
        try:
            req = urllib.request.urlopen(url)
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1)  # 'load it as it is'

            if img is not None:
                return 'Okay', img
            else:
                return 'ImageError', img
            # cv2.imshow('lalala', img)
            # if cv2.waitKey() & 0xff == 27: quit()
        except:
            imgerror = sys.exc_info()[0]
            print(imgerror)
            return 'ImageRetrieveError', img


    return 'UnknownError', img
    # assert 3 * 4 == 123
    # img = Image.open(BytesIO(response.content))

def main():
    status, img = getimage(url = 'www.google.com.au')
    assert status == 'MissingSchema'
    assert img == None

    status, img = getimage(url = 'http://www.google.com.au')
    assert status == 'ImageError'
    assert img == None

    status, img = getimage(url = 'http://www.googleeee.com.au')
    assert status == 'ConnectionError'
    assert img == None

    status, img = getimage(url = 'http://www.google.com.au/jfnakjsdfn')
    assert status == 'NotFound'
    assert img == None


    status, img = getimage(url = 'https://en.wikipedia.org/wiki/File:404_error_sample.png')
    assert status == 'ImageError'
    assert img == None

    status, img = getimage(url = 'http://opencv-python-tutroals.readthedocs.io/en/latest/_static/opencv-logo-white.png')
    assert status == 'Okay'
    assert img is not None
    cv2.imshow('readimg', img)
    cv2.waitKey()



    urls = [
            'http://webneel.com/daily/sites/default/files/images/daily/09-2013/4-amazing-photography-lake.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/6-amazing-photography-ship.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/7-amazing-photography-ship.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/25-amazing-photo-living-human-brain.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/11-amazing-photography-tracy-space-earch.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/10-amazing-photography-space-shuttle-moon.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/2-amazing-photography-clouds.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/1-amazing-photography-parachute-jump.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/3-amazing-photography-park.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/5-amazing-photography-sunrise.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/8-amazing-photography-train-snow.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/9-amazing-photography-hurricane-space.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/12-creative-photography-woman.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/14-creative-photography-woman.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/16-creative-photography-portrait.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/17-most-amazing-photo-hight-sea-tide.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/18-amazing-photos-sea-wave.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/19-amazing-photography-woman-hair-splashing.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/20-amazing-photography-woman-splashing-hair.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/21-most-amazing-photo-fishing-net.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/22-most-amazing-photos-sunrise.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/23-most-amazing-photo-tree.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/24-amazing-photography-naobab-tree.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/amazing-photo.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/27-amazing-photo-dew-drops-macro.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/28-amazing-photo-water.preview.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/29-amazing-photos-cat.jpg'
            , 'http://webneel.com/daily/sites/default/files/images/daily/09-2013/30-amazing-photos-motion-blur-night.preview.jpg']
    for urlimg in urls:
        status, img = getimage(url=urlimg)
        assert status == 'Okay'
        assert img is not None
        cv2.imshow('readimg', img)
        cv2.waitKey()


if __name__ == "__main__":
    main()

