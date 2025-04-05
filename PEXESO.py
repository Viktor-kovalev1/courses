import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from random import shuffle

# создаем черный прямоугольник, если пара угадана
# каккого не работает?????????????( не могу объединить с другими картинками)
def black_rectangle():
    img=np.zeros((100,1260,3))  
    return img


# делаем красоту 

def mouse_click(event,x,y,flags,params):
    global x0
    global y0
    global count
    global elem1
    global elem2
    global coord_list
    global img_list
    global pict_list
    global ind1
    global ind2
    global back_img
    global fontFace
    global number_of_turn
    if event==cv.EVENT_LBUTTONDOWN:
        if count==0:
            for elem in coord_list:
                if elem[0]<=x<=elem[0]+200 and elem[1]+100<=y<=elem[1]+200 and elem[2]=='close':
                    ind1=coord_list.index(elem)
                    elem[2]='open'
                    img_list[ind1]=pict_list[ind1]
                    elem1=pict_list[ind1]
                    img=big_picture(img_list)
                    img=cv.vconcat([black_rectangle(),img])
                    cv.putText(img, f"Number of terns: {number_of_turn}", org = (20, 50), fontFace = fontFace, fontScale = 2,thickness = 1, color = 1 )
                    cv.imshow( "Window",img)
                    count=1

        elif count==1:
            for elem in coord_list:
                if elem[0]<=x<=elem[0]+200 and elem[1]+100<=y<=elem[1]+200 and elem[2]=='close':
                    ind2=coord_list.index(elem)
                    elem[2]='open'
                    img_list[ind2]=pict_list[ind2]
                    elem2=pict_list[ind2]
                    img=big_picture(img_list)
                    img=cv.vconcat([black_rectangle(),img])
                    cv.putText(img, f"Number of terns: {number_of_turn}", org = (20, 50), fontFace = fontFace, fontScale = 2,thickness = 1, color = 1 )
                    cv.imshow( "Window",img)
                    count=2
        else:
            number_of_turn-=1
            if np.array_equal(elem1, elem2):
                elem=elem1.copy()
                img_list[ind1]=elem
                img_list[ind2]=elem
                coord_list[ind1][2]='open'
                coord_list[ind2][2]='open'
            else:
                img_list[ind1]= back_img
                img_list[ind2]=back_img
                img=big_picture(img_list)
                img=cv.vconcat([black_rectangle(),img])
                cv.putText(img, f"Number of terns: {number_of_turn}", org = (20, 50), fontFace = fontFace, fontScale = 2,thickness = 1, color = 1 )
                cv.imshow( "Window",img)
                coord_list[ind1][2]='close'
                coord_list[ind2][2]='close'
            if number_of_turn==0:
                img1 = np.zeros( (800, 2200) )
                fontFace = cv.FONT_HERSHEY_DUPLEX
                cv.putText( img1, "YOU LOOSE, triple press any key", org = (20, 200), fontFace = fontFace, fontScale = 2.5,thickness = 3, color = 1 )
                cv.imshow( "Window",img1)
                cv.waitKey(0)
            control_list=[elem[2]for elem in coord_list]

           # хз почему не работает
            if 'close' not in control_list:
                img1 = np.zeros( (800, 2200) )
                fontFace = cv.FONT_HERSHEY_DUPLEX
                cv.putText( img1, "YOU WIN, triple press any key", org = (20, 200), fontFace = fontFace, fontScale = 2.5,thickness = 3, color = 1 )
                cv.imshow( "Window",img1)
                cv.waitKey(0)
               # cv.destroyWindow("Window")
            count=0

# совмещаем все картинки в кучу
def big_picture(pict_list):
    new_list=[]
    num=0
    h_list=[]
    for elem in pict_list:
        num+=1
        size=5
        image = cv.copyMakeBorder(elem, size, size, size, size,cv.BORDER_CONSTANT, value=[0,0,0])
        new_list.append(image)
        if num==6:
            img=cv.hconcat(new_list)
            h_list.append(img)
            new_list=[]
            num=0
    core=cv.vconcat(h_list)
    return core

    

# создаем рубашку

back_img=cv.imread('Volga.jpg')
back_img=cv.resize(back_img,(200,100))/255


count=0# переменная, отвечающая за количество нажатий лкм

#загружаем изображения

n=15
pict_list=[]
for i in range(n):
    img=cv.imread(f"molecule{i+1}.png")
    img=cv.resize(img, (200,100))/255
    pict_list.append(img)
pict_list*=2
shuffle(pict_list)
# создаем саму игру

#Hellow geymer
img0=img = np.zeros( (800, 2000) )
fontFace = cv.FONT_HERSHEY_DUPLEX
cv.putText( img0, "LETS START press any key", org = (200, 200), fontFace = fontFace, fontScale = 3,thickness = 3, color = 1 )
cv.imshow( "Window",img0)
cv.waitKey(0)
cv.destroyWindow("Window")


img_list=[back_img]*2*n
coord_list=[]
for j in range(5):
    coord_list.extend([[5+210*i,5+110*j,'close']for i in range(6)])
number_of_turn=50
img=big_picture(img_list)
img=cv.vconcat([black_rectangle(),img])
cv.putText(img, f"Number of terns: {number_of_turn}", org = (20, 50), fontFace = fontFace, fontScale = 2,thickness = 1, color = 1 )
cv.imshow( "Window",img)
cv.setMouseCallback('Window',mouse_click)
cv.waitKey(0)
cv.destroyWindow("Window")
   

