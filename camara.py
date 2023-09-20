import cv2
print("Package imported")
# img = cv2.imread("resources/balloon.jpg")
# videoSource = "resources/example.mp4"
videoSource = 0
# videoSource = "http:192.168.0.124:8080/shot.jpg" # IP webcam Android
cap = cv2.VideoCapture(videoSource)

# _, img = cap.read()
# cv2.imshow("Image", img)

while True:
    cap.open(videoSource)  # necesario para apertura de cámara ip
    _, img = cap.read()
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:   # ESC ?
        break
