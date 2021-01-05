import numpy as np
import cv2

# starting the web cam
cam = cv2.VideoCapture(0)
bg = cv2.imread("ME.png")

while True:
    ret, frame = cam.read()
    # print(frame)

    frame = cv2.resize(frame, (640, 480))
    bg = cv2.resize(bg, (640, 480))

    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])
    mask = cv2.inRange(frame, l_black, u_black)
    
    res = cv2.bitwise_and(frame, frame, mask = mask)
    f = frame - res
    f = np.where(f == 0, bg, f)
    cv2.imshow("output", frame)
    cv2.imshow("output2", f)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()