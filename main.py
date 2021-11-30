from cv2 import cv2

cap = cv2.VideoCapture(0)

img_counter = 0

while True:
    ret, frame = cap.read()
    cv2.imshow('S&H camera', frame)
    if cv2.waitKey(50) == ord('q'):
        break
    elif cv2.waitKey(20) == ord(' '):
        img_name = 'captured_img_{}.png'.format(img_counter)
        cv2.imwrite(img_name, frame)
        img_counter += 1

cap.release()

