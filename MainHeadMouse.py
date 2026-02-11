import cv2
import numpy as np
import pyautogui

# Screen size
screen_w, screen_h = pyautogui.size()

# Sensitivity constant (PLAY WITH THIS)
k_head = 2.5

# Load face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

prev_nose = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Approximate nose position
        nose_x = x + w // 2
        nose_y = y + int(h * 0.6)

        cv2.circle(frame, (nose_x, nose_y), 5, (0, 0, 255), -1)

        if prev_nose is not None:

            # ---------------- MATHEMATICS START ----------------
            dx = nose_x - prev_nose[0]      # displacement in x
            dy = nose_y - prev_nose[1]      # displacement in y

            move_x = k_head * dx            # scaling by sensitivity constant
            move_y = k_head * dy            # scaling by sensitivity constant
            # ---------------- MATHEMATICS END ----------------

            current_mouse_x, current_mouse_y = pyautogui.position()

            new_mouse_x = current_mouse_x + move_x
            new_mouse_y = current_mouse_y + move_y

            pyautogui.moveTo(new_mouse_x, new_mouse_y)

            cv2.line(frame, prev_nose, (nose_x, nose_y), (255, 0, 0), 2)

        prev_nose = (nose_x, nose_y)

    # Resize webcam window
    small_frame = cv2.resize(frame, (320, 240))

    cv2.imshow("Percepta Head Tracking", small_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
