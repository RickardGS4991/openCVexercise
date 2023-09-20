"""
Ejercicio 03. Modificación de imágenes
- Redimensionamiento
- Inversión horizontal
- Inversión vertical
- Rotación
- Recorte
Versión de Python: 3.8.6
Versión de OpenCV: 4.2.0.32
Versión de numpy: 1.21.3
"""
import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)

img = cv2.imread("resources/balloon.jpg") #You must have a photo with this same name in the same directory
imgSmall = cv2.resize(img, (500, 350))
imgV = cv2.flip(imgSmall, 0)
imgH = cv2.flip(imgSmall, 1)
imgR = cv2.flip(imgSmall, -1)
imgC = img[120:490, 288:630]

while True:
    cv2.imshow("Original", img)
    cv2.imshow("Small", imgSmall)
    cv2.imshow("Vertical", imgV)
    cv2.imshow("Horizontal", imgH)
    cv2.imshow("Rotated", imgR)
    cv2.imshow("Cropped", imgC)

    if cv2.waitKey(1) & 0xFF == 27:
        break