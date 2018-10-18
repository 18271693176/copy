import os
import csv
import shutil

train_path_prefix = '/home/newnfs/ljf/chestxray/train/images'
train_label_prefix = '/home/newnfs/ljf/chestxray/train/labels'
val_path_prefix = '/home/newnfs/ljf/chestxray/val/images'
val_label_prefix = '/home/newnfs/ljf/chestxray/val/labels'




dir_list = [train_path_prefix,train_label_prefix,val_path_prefix,val_label_prefix]
for path in dir_list:
    if not os.path.exists(path):
       os.makedirs(path)


def produce_train():
    with open('BBox_List_2017.csv') as csv_file:
        tmp = csv.reader(csv_file)
        j = 0
        for i in tmp:
            old_pic_path = os.path.join('/home/newnfs/ljf/CHESTXRAY/images_a', i[0])
            if i[0] != 'Image Index':
                if os.path.exists(old_pic_path):
                    train_pic_path = os.path.join(train_path_prefix, str(j) + '.png')
                    train_label_path = os.path.join(train_label_prefix, str(j) + '.txt')
                    shutil.copyfile(old_pic_path, train_pic_path)
                    with open(train_label_path, 'w') as f:
                        f.write('{} 0 0 0 {} {} {} {} 0 0 0 0 0 0 0'.format(i[1],i[2],i[3],i[4],i[5]))
                    j += 1
                else:
                    print '{} file not found in folder'.format(old_pic_path)




def produce_val():
    for i in range(400):
        old_pic_path = os.path.join(train_path_prefix,str(i)+'.png')
        old_txt_path = os.path.join(train_label_prefix,str(i)+'.txt')
        new_pic_path = os.path.join(val_path_prefix,str(i)+'.png')
        new_txt_path = os.path.join(val_label_prefix, str(i) +'.txt')
        if os.path.exists(old_pic_path) and os.path.exists(old_txt_path):
            shutil.copyfile(old_pic_path,new_pic_path)
            shutil.copyfile(old_txt_path,new_txt_path)
        else:
            print '{} not found'.format(old_pic_path)

if __name__ == '__main__':
    produce_train()
    produce_val()