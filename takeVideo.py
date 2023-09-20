import cv2

videoSource = 0

cap = cv2.VideoCapture(videoSource)

codecs = cv2.VideoWriter_fourcc(*'MP4V')
salida = cv2.VideoWriter('videoSalida.mp4', codecs, 20.0, (640, 480))

while (cap.isOpened()):
    ret, img = cap.read()
    if ret == True:
        cv2.imshow('video', img)
        salida.write(img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
salida.release()
cv2.destroyAllWindows()
