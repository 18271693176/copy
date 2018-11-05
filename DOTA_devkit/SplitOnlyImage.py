# coding = utf-8
import copy
import os

import numpy as np

import cv2
import dota_utils as util


class splitbase():
    def __init__(self,
                 srcpath,
                 dstpath,
                 gap=100,
                 subsize=256,
                 ext='.png'):
        self.srcpath = srcpath
        self.outpath = dstpath
        self.gap = gap
        self.subsize = subsize
        self.slide = self.subsize - self.gap
        self.srcpath = srcpath
        self.dstpath = dstpath
        self.ext = ext

    def saveimagepatches(self, img, subimgname, left, up, ext='.png'):
        subimg = copy.deepcopy(img[up: (up + self.subsize), left: (left + self.subsize)])
        print subimg.shape
        # subimg.show()
        outdir = os.path.join(self.dstpath, subimgname + ext)
        print outdir
        cv2.imwrite(outdir, subimg)

    def SplitSingle(self, name, rate, extent):
        img = cv2.imread(os.path.join(self.srcpath, name + extent))
        assert np.shape(img) != ()

        if (rate != 1):
            resizeimg = cv2.resize(img, None, fx=rate, fy=rate, interpolation=cv2.INTER_CUBIC)
        else:
            resizeimg = img

        # the image after resize
        outbasename = name + '__' + str(rate) + '__'

        weight = np.shape(resizeimg)[1]
        height = np.shape(resizeimg)[0]
        print weight,height
        left, up = 0, 0
        while (left < weight):
            if (left + self.subsize >= weight):
                left = max(weight - self.subsize, 0)
            up = 0
            while (up < height):
                if (up + self.subsize >= height):
                    up = max(height - self.subsize, 0)
                print 'up={},left={}'.format(up,left)
                subimgname = outbasename + str(left) + '___' + str(up)
                print 'after save up={},left={}'.format(up,left)
                self.saveimagepatches(resizeimg, subimgname, left, up)
                if (up + self.subsize >= height):
                    break
                else:
                    up = up + self.slide #156
            if (left + self.subsize >= weight):
                break
            else:
                left = left + self.slide

    def splitdata(self, rate):

        imagelist = util.GetFileFromThisRootDir(self.srcpath)
        imagenames = [util.custombasename(x) for x in imagelist if (util.custombasename(x) != 'Thumbs')]
        for name in imagenames:
            self.SplitSingle(name, rate, self.ext)


if __name__ == '__main__':
    split = splitbase(r'example/images/',
                      r'example/examplesSplit/')
    split.splitdata(1)
