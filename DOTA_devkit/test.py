# -*-coding:utf-8-*-
import time
import os
import re
from PIL import Image
import numpy as np
import cv2
import copy

path = "example/examplesSplit"

# xIndex = 0
# yIndex = 0
# cropSize = 256
# xNum = 0
# yNum = 0
#
# im = Image.open(IMAGE_PATH)  # 打开图片句柄
# pSize = im.size
#
# xNum = pSize[0] / cropSize
# yNum = pSize[1] / cropSize
#
# print "size  ", xNum, '  ', yNum
#
# for yIndex in range(yNum):
#     for xIndex in range(xNum):
#         print "pic : ", xIndex, "_", yIndex
#         box = (xIndex * cropSize, yIndex * cropSize, (xIndex + 1) * cropSize, (yIndex + 1) * cropSize)  # 设定裁剪区域
#         region = im.crop(box)  # 裁剪图片，并获取句柄region
#         name = "example/test/map%s_%s.png" % (xIndex, yNum - 1 - yIndex)
#         region.save(name)  # 保存图片
#         # xIndex = xIndex+1
#         # yIndex = yIndex+1
#         print int(time.time())


# box = (0, 156, 256, 412)  # 设定裁剪区域
# region = im.crop(box)
# name = 'b.png'
# region.save(name)

# size = 256
# gap = 100
# num = 156


def get_files(dir, ext=None):
    allfiles = []
    needExtFilter = (ext != None)
    for root, dirs, files in os.walk(dir):
        for filespath in files:  # 遍历文件夹中的原图片
            filepath = os.path.join(root, filespath)
            extension = os.path.splitext(filepath)[1][1:]
            if needExtFilter and extension in ext:
                allfiles.append(filepath)
            elif not needExtFilter:
                allfiles.append(filepath)
    return allfiles


all_pic = get_files(path)




def merge_pic(wight=1111,height=1182):
    c_img = Image.new('RGB', (wight, height))

    for pic in all_pic:
        pattern1 = re.compile(r'__\d+___\d+')
        # print('subname:', subname)
        x_y = re.findall(pattern1, pic)
        x_y_2 = re.findall(r'\d+', x_y[0])
        x, y = int(x_y_2[0]), int(x_y_2[1])
        tmp = Image.open(pic)
        c_img.paste(tmp, (x, y, x + 256, 256 + y))

    c_img.save('c.png')


# a_img = Image.open('a.png')
# b_img = Image.open('b.png')

#
# c_img.paste(a_img,(0,0,256,256))
# c_img.paste(b_img,(0,156,256,412))
#
# # c_img.show()
#
# c_img.save('c.png')





def split_single(pic_path='P0706.png', dstpath='test', subszie=256, gap=100):
    img = cv2.imread(pic_path)
    pic_name = pic_path.split('/')[-1].split('.')[0]
    weight = np.shape(img)[1]
    height = np.shape(img)[0]
    left, up = 0, 0
    slide = subszie - gap
    outbasename = pic_name + '__' + '1' + '__'
    while (left < weight):
        if (left + subszie >= weight):
            left = max(weight - subszie, 0)
        up = 0
        while (up < height):
            if (up + subszie >= height):
                up = max(height - subszie, 0)
            print 'up={},left={}'.format(up, left)
            subimgname = outbasename + str(left) + '___' + str(up)
            print 'after save up={},left={}'.format(up, left)
            subimg = copy.deepcopy(img[up: (up + subszie), left: (left + subszie)])
            outdir = os.path.join(dstpath, subimgname + '.png')
            cv2.imwrite(outdir, subimg)
            if (up + subszie >= height):
                break
            else:
                up = up + slide  # 156
        if (left + subszie >= weight):
            break
        else:
            left = left + slide


split_single()