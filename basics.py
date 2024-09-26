# import numpy as np
import cv2
import face_recognition

imgMarnus = face_recognition.load_image_file('ImagesBasic/Marnus.png')
imgMarnus = cv2.cvtColor(imgMarnus, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('ImagesBasic/Marnus Test.png')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgMarnus)[0]
encodeMarnus = face_recognition.face_encodings(imgMarnus)[0]
cv2.rectangle(imgMarnus, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

# comparing the faces and finding the distance between faces
results = face_recognition.compare_faces([encodeMarnus], encodeTest)
faceDis = face_recognition.face_distance([encodeMarnus], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Marnus', imgMarnus)
cv2.imshow('Marnus Test', imgTest)
cv2.waitKey(0)
