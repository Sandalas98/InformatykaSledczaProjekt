import os
from PIL import Image, ImageOps
import cv2


# Funkcja zwraca wycięte twarze ze zdjęcia i zapusje je jako face_x.jpg w analisys_dir/images
def face_detection(path):
    iterator = -1
    for img in os.listdir(path):
        if img.endswith('.jpg') or img.endswith('.png'):
            iterator += 1
            print(path+'/'+img)
            img = cv2.imread(path+'/'+img)
    
            # Convert into grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Load the cascade
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
            
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            # Draw rectangle around the faces and crop the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                faces = img[y:y + h, x:x + w]
                cv2.imshow("face",faces)
                cv2.imwrite('face.jpg', faces)
                
            # Display the output
            cv2.imwrite(path+f'/face_{iterator}', img)
