#recognition step

import cv2
import face_recognition as fr
import pandas as pd
import numpy as np


vid = cv2.VideoCapture(0)
fd = cv2.CascadeClassifier(
    cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')

try:
    face_db = pd.read_csv('faces_data.tsv', index_col = 0, sep='\t')  #read file
    data = {'name':face_db['name'].values.tolist(),      #convert it back to dictionary
            'encoding':face_db['encoding'].values.tolist(),}

except Exception as e:
    print(e)  #print the error
    data={'name':[],'encoding':[]}  #if not present create a new csv file

while True:
    flag, img=vid.read()
    if flag:
        faces= fd.detectMultiScale(
            cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50,50)
        )
        if len(faces)==1:
            x,y,w,h =faces[0]
            img_face = img[y:y+h, x:x+w, :].copy()   #crop the image
            img_face=  cv2.resize(img_face, (400,400),
                                  interpolation= cv2.INTER_CUBIC)  #size remains same of cropped face
            
            face_encoding = fr.face_encodings(img_face)  #extract features

            if len(face_encoding)==1:
                # print('recognition will  starts')
                
                for ind,enc_value in enumerate (data['encoding']):
                    print(enc_value)
                    matched = fr.compare_faces(face_encoding[0],np.array(eval(enc_value)))

                    if matched == True:
                        # print(data['name'][ind])
                        cv2.putText(                                       #to print name on image
                            img, data['name'][ind],
                            (50,50), cv2.FONT_HERSHEY_COMPLEX,
                            (0,0,255),8)
                        break

            # cv2.imwrite(f'{name}_{frameCount}.png',img_face)  #save image
            # print(face_encoding)

            
        cv2.imshow('preview', img)
        key = cv2.waitKey(1)
        if key==ord('q'):
            break
cv2.destroyAllWindows()
vid.release()