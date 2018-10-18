from xml.dom.minidom import Document
import os
import os.path
from PIL import Image
#
# ann_path = "E:\\voc_year\\VOCdevkit\\VOC2005\\Annotations_txt\\"
# img_path = "E:\\voc_year\\VOCdevkit\\VOC2005\\yolo_img\\"
# xml_path = "E:\\voc_year\\VOCdevkit\\VOC2005\\ssd_label\\"

# if not os.path.exists(xml_path):
#     os.mkdir(xml_path)


import csv
import shutil

def class_transfer(num):
    if num == 1:
        return 'bone'
    elif num == 2:
        return 'abdomen'
    elif num == 3:
        return 'mediastinum'
    elif num == 4:
        return 'liver'
    elif num == 5:
        return 'lung'
    elif num == 6:
        return 'kidney'
    elif num == 7:
        return 'softtissue'
    elif num == 8:
        return 'pelvi'
    else:
        return 'other'



def writeXml(class_name,pic_name,xml_name,xmin_n,ymin_n,xmax_n,ymax_n,size_n):
    doc = Document()
    # owner
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)
    # owner
    folder = doc.createElement('folder')
    annotation.appendChild(folder)
    folder_txt = doc.createTextNode("deeplsion")
    folder.appendChild(folder_txt)

    filename = doc.createElement('filename')
    annotation.appendChild(filename)
    filename_txt = doc.createTextNode(pic_name)
    filename.appendChild(filename_txt)
    # ones#
    source = doc.createElement('source')
    annotation.appendChild(source)

    database = doc.createElement('database')
    source.appendChild(database)
    database_txt = doc.createTextNode("The deeplsion Database")
    database.appendChild(database_txt)

    annotation_new = doc.createElement('annotation')
    source.appendChild(annotation_new)
    annotation_new_txt = doc.createTextNode("deeplsion")
    annotation_new.appendChild(annotation_new_txt)

    image = doc.createElement('image')
    source.appendChild(image)
    image_txt = doc.createTextNode("flickr")
    image.appendChild(image_txt)
    # onee#
    # twos#
    size = doc.createElement('size')
    annotation.appendChild(size)

    width = doc.createElement('width')
    size.appendChild(width)
    width_txt = doc.createTextNode(size_n)
    width.appendChild(width_txt)

    height = doc.createElement('height')
    size.appendChild(height)
    height_txt = doc.createTextNode(size_n)
    height.appendChild(height_txt)

    depth = doc.createElement('depth')
    size.appendChild(depth)
    depth_txt = doc.createTextNode("3")
    depth.appendChild(depth_txt)
    # twoe#
    segmented = doc.createElement('segmented')
    annotation.appendChild(segmented)
    segmented_txt = doc.createTextNode("0")
    segmented.appendChild(segmented_txt)


    object_new = doc.createElement("object")
    annotation.appendChild(object_new)

    name = doc.createElement('name')
    object_new.appendChild(name)
    name_txt = doc.createTextNode(class_name)
    name.appendChild(name_txt)

    pose = doc.createElement('pose')
    object_new.appendChild(pose)
    pose_txt = doc.createTextNode("Unspecified")
    pose.appendChild(pose_txt)

    truncated = doc.createElement('truncated')
    object_new.appendChild(truncated)
    truncated_txt = doc.createTextNode("0")
    truncated.appendChild(truncated_txt)

    difficult = doc.createElement('difficult')
    object_new.appendChild(difficult)
    difficult_txt = doc.createTextNode("0")
    difficult.appendChild(difficult_txt)
    # threes-1#
    bndbox = doc.createElement('bndbox')
    object_new.appendChild(bndbox)

    xmin = doc.createElement('xmin')
    bndbox.appendChild(xmin)
    xmin_txt = doc.createTextNode(xmin_n)
    xmin.appendChild(xmin_txt)

    ymin = doc.createElement('ymin')
    bndbox.appendChild(ymin)
    ymin_txt = doc.createTextNode(ymin_n)
    ymin.appendChild(ymin_txt)

    xmax = doc.createElement('xmax')
    bndbox.appendChild(xmax)
    xmax_txt = doc.createTextNode(xmax_n)
    xmax.appendChild(xmax_txt)

    ymax = doc.createElement('ymax')
    bndbox.appendChild(ymax)
    ymax_txt = doc.createTextNode(ymax_n)
    ymax.appendChild(ymax_txt)
    # threee-1#
    # threee#

    prefix = '/home/newnfs/Dataset/deeplesion/new_xml'
    tempfile = os.path.join(prefix,xml_name)
    print 'write start {}'.format(tempfile)
    with open(tempfile, "w") as f:
        f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
    print 'write end {}'.format(tempfile)

with open('DL_info.csv','rb') as csv_file:
    tmp = csv.reader(csv_file)
    j = 0
    for i in tmp:
        if i[0] != 'File_name':
            old_pic_path = os.path.join('/home/newnfs/Dataset/deeplesion/Key_slices',i[0])
            # print '----',old_pic_path
            if os.path.exists(old_pic_path):
                print old_pic_path
                file_name = old_pic_path.strip().split('.')[0].split('/')[-1]
                pic_name = file_name + '.png'
                xml_name = file_name + '.xml'
                class_name = class_transfer(int(i[9]))
                if int(i[9])!= -1:
                    i_13_list = i[13].split(',')
                # print label_class
                    i_6_list = i[6].split(',')
                    xmin_n = str(int(float(i_6_list[0].strip())))
                    ymin_n = str(int(float(i_6_list[1].strip())))
                    xmax_n = str(int(float(i_6_list[2].strip())))
                    ymax_n = str(int(float(i_6_list[3].strip())))
              #  ymin_n = int(i_6_list[1].strip())
              #  xmax_n = int(i_6_list[2].strip())
              #  ymax_n = int(i_6_list[3].strip())
                    size_n = i_13_list[0].strip()
                    writeXml(class_name,pic_name,xml_name,xmin_n,ymin_n,xmax_n,ymax_n,size_n)
                    j+=1
                # print j
            else:
                print '{} file not found in folder'.format(old_pic_path)
        else:
            pass







#     with open(path, 'r') as f:
#         file_name = path.split('.')[0]
#         pic_name = file_name + '.png'
#         xml_name = file_name + '.xml'
#         line = f.read()
#         line_list = line.split()
#         writeXml(line_list, pic_name, xml_name)
