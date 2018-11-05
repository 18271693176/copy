import cv2

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
im = cv2.imread('C:\Users\ljf\Desktop\copy\DOTA_devkit\example\images\8888.png')
with open('C:\Users\ljf\Desktop\copy\DOTA_devkit\example\images\\comp4_det_test_plane.txt','r') as f:
    for line in f.readlines():
        if line:
            content = line.split(' ')
            x1,y1,x2,y2 = float(content[2]),float(content[3]),float(content[4]),float(content[5])
            truth = float(content[1])
            if truth > 0.25:
                print truth,type(x1),y1,x2,y2
                txt = 'plane {}'.format(round(truth,2))
                cv2.rectangle(im, (int(x1), int(y2)), (int(x2),int(y1)), (0, 255, 0), 2)
                cv2.putText(im, txt, (int(x1), int(y1)-7), font, 0.8, (0, 0, 255), 1)
# # 756.923965 763.822113 841.512268 877.402313
# cv2.rectangle(im,(756,877),(841,763),(0,255,0),2)
# cv2.rectangle(im,(870,890),(977,761),(0,255,0),1)
# cv2.rectangle(im,(620,867),(720,771),(0,255,0),3)



cv2.imwrite('C:\Users\ljf\Desktop\copy\DOTA_devkit\example\images\\9999.png',im)


