import csv
from xml.dom.minidom import Document
import os
import os.path

images_path = '/home/newnfs/ljf/CHESTXRAY/images_a'
xml_path = '/home/newnfs/ljf/CHESTXRAY/xmls'

if not os.path.exists(xml_path):
    os.makedirs(xml_path)




def process_x_y(x,y,w,h):
    xmin = x
    xmax = x + w
    ymin = y - h
    ymax = y
    return str(xmin),str(xmax),str(ymin),str(ymax)


def writeXml(class_name,pic_name,xml_name,xmin_n,ymin_n,xmax_n,ymax_n):
    doc = Document()
    # owner
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)
    # owner
    folder = doc.createElement('folder')
    annotation.appendChild(folder)
    folder_txt = doc.createTextNode("CHESTXRAY")
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
    width_txt = doc.createTextNode('1024')
    width.appendChild(width_txt)

    height = doc.createElement('height')
    size.appendChild(height)
    height_txt = doc.createTextNode('1024')
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



with open('BBox_List_2017.csv') as csv_file:
    tmp = csv.reader(csv_file)
    for i in tmp:
        if i[0] != 'Image Index':
            png_name = i[0]
            name = i[0].split('.')[0]
            xml_file_path = os.path.join(xml_path,name+'xml')
            if os.path.exists(os.path.join(images_path,png_name)):
                class_name = i[1]
                xmin, xmax, ymin, ymax = process_x_y(int(i[2]),int(i[3]),int(i[4]),int(i[5]))
                writeXml(class_name,png_name,xml_path,xmin,ymin,xmax,ymax)
            else:
                print 'No such file {}'.format(png_name)










