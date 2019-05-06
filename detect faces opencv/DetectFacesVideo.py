import cv2

# Importa los datos de machine learning previamente entrenados https://github.com/opencv/opencv/tree/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capturar video de alguna fuente, https://www.youtube.com/watch?v=S9vBXV-tHEM 
# cap = cv2.VideoCapture('test.mp4')

while True:
    # Lee un cuadro de video
    _, img = cap.read()
    # Convierte a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detecta la cara
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Dibuja un rectangulo en la cara
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Muestra la imagen procesada
    cv2.imshow('img', img)
    # Se detiene si es precionada la tecla ESC
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Deja el tratamiento de datos sobre el video
cap.release()