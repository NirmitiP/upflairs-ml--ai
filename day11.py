import cv2
import matplotlib.pyplot  as plt
fd= cv2.CascadeClassifier(                                                 #feature descriptor
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'  #github file
)
sd = cv2.CascadeClassifier(                                                 #feature descriptor
    cv2.data.haarcascades + 'haarcascade_smile.xml')

vid=cv2.VideoCapture(0)
vid.isOpened()
flag,img=vid.read()
from time import sleep
seq=0
captured = False
while not captured:
    flag,img=vid.read()
    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #to convert in gray

        th,img_binary=cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY) #to convert in binary

        # x1,y1,w,h = (200,400,300,400)
        faces= fd.detectMultiScale(img_gray,                           #face detection
                                   scaleFactor=1.1,                    #scaleFactor- face detection precision 1.1 times
                                   minNeighbors=5,                    #minNeighbours
                                   minSize= (180,180)                   #minSize- min value of width and height
                                    )                 
          
                                                                            
        for x1,y1,w,h in faces:
            # img_cropped = img[y1:y1+h, x1:x1+w , :] #crops the image
            face = img_gray[y1:y1+h, x1:x1+w].copy()
            smiles = sd.detectMultiScale(face,1.1,5) #smile detection
            print(len(smiles))

            if len(smiles)==1:
                seq += 1
                if seq ==5:       
                    captured=cv2.imwrite('smile.png',img)
                    break
                xs,ys,ws,hs = smiles[0]
                cv2.rectangle(
                            img,
                            pt1=[xs+x1,ys+y1], 
                            pt2=[xs+ws+x1,ys+hs+y1],
                            color=(0,255,0),
                            thickness=7)
                
            else:
                seq=0


            cv2.rectangle(
                        img, 
                        pt1=[x1,y1], pt2= [x1+w, y1+h], 
                        color=(0,0,255),
                        thickness=7)  #higlights the particular part
            
            
 
            cv2.imshow('Preview',img)
        key=cv2.waitKey(1)
        if key==ord(' '): #will close the window when pressed spacebar
            break
    else:
        break
    sleep(0.1) #for delay
vid.release() #turns off the camera
cv2.destroyAllWindows()
#cv2.waitKey(1)    # only for Mac Os ,not for windows.
