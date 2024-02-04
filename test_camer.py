import cv2

cap = cv2.VideoCapture(0)
# cap.set(6, cv2.VideoWriter.fourcc("M", "J", "P", "G"))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# cap.set(cv2.CAP_PROP_FPS, 90)  # 设置帧率为30帧/秒


while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
