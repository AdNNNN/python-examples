import cv2

# Importa los datos de machine learning previamente entrenados https://github.com/opencv/opencv/tree/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Lee la imagen de entrada
img = cv2.imread('test.jpg')

# Convierte la imagen a escala de grises
gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecta la cara
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Dibuja un rectangulo alrrededor de la cara
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h),(255,0,0),2)

# Muestra la salida de datos

cv2.imshow('img', img)
cv2.waitKey()
