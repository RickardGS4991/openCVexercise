import cv2

videoSource = 0

cap = cv2.VideoCapture(videoSource)
img_counter = 0

while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    if k % 256 == 97:
        # img_name = "image_{}.png".format(img_counter)
        cv2.imwrite('C:Users/labra/Desktop/Robotics/rostro.jpg', frame)
        print("Photo written!")
        img_counter += 1

cap.release()
cv2.destroyAllWindows()
