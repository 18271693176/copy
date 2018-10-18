# import numpy as np
#
# tmp = np.loadtxt('a.csv',dtype=np.str,delimiter=',')
#
# print tmp


import csv
import os
import shutil

train_path_prefix = '/home/newnfs/ljf/deeplsion/train/images'
train_label_prefix = '/home/newnfs/ljf/deeplsion/train/labels'
val_path_prefix = '/home/newnfs/ljf/deeplsion/val/images'
val_label_prefix = '/home/newnfs/ljf/deeplsion/val/labels'

dir_list = [train_path_prefix,train_label_prefix,val_path_prefix,val_label_prefix]

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

for path in dir_list:
    if not os.path.exists(path):
        os.makedirs(path)


with open('DL_info.csv','rb') as csv_file:
    tmp = csv.reader(csv_file)
    j = 0
    for i in tmp:
        if i[0] != 'File_name':
            old_pic_path = os.path.join('/home/newnfs/Dataset/deeplesion/Key_slices',i[0])
            # print '----',old_pic_path
            if os.path.exists(old_pic_path):
                train_pic_path = os.path.join(train_path_prefix,str(j)+'.png')
                val_pic_path = os.path.join(val_path_prefix,str(j)+'.png')
                val_label_path = os.path.join(val_label_prefix,str(j)+'.txt')
                # prefix = i[0].split('.')[0]
                train_label_path = os.path.join(train_label_prefix,str(j)+'.txt')
                label_class = class_transfer(int(i[9]))
                print label_class
                i_6_list = i[6].split(',')
                i_6 = '{} {} {} {}'.format(i_6_list[0].strip(),i_6_list[1].strip(),i_6_list[2].strip(),i_6_list[3].strip())
                i_8_list = i[8].split(',')
                i_8 = '{} {} {}'.format(i_8_list[0].strip(),i_8_list[1].strip(),i_8_list[2].strip())
                i_12_list = i[12].split(',')
                i_12 = '{} {} {}'.format(i_12_list[0].strip(),i_12_list[1].strip(),i_12_list[2].strip())
                i_13_list = i[13].split(',')
                # i_13 = '{} {}'.format(i_13_list[0].strip(), i_13_list[1].strip())
                if i_13_list[0].strip() == '512':
                    if i[-1] == '1':
                        print '1111'
                        shutil.copyfile(old_pic_path,train_pic_path)
                        with open(train_label_path,'w') as f:
                            f.write('{} 0 0 0 {} {} {} 0'.format(label_class,i_6,i_12,i_8))
                    elif i[-1] == '2':
                        print '2222'
                        shutil.copyfile(old_pic_path,val_pic_path)
                        with open(val_label_path,'w') as f:
                            f.write('{} 0 0 0 {} {} {} 0'.format(label_class,i_6,i_12,i_8))
                    j+=1
            else:
                print '{} file not found in folder'.format(old_pic_path)
        else:
            pass






