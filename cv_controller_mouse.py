import cv2
import mediapipe as mp
import pyautogui
from math import dist

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
pyautogui.FAILSAFE = False  
prev_x, prev_y = 0, 0
prev_dx, prev_dy = 0, 0
screen_width, screen_height = pyautogui.size()

acc = 0.9 
accd = 0.4
close = 0.12
dragging = False

def is_hand_closed(hand_landmarks):
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    distance = dist((wrist.x, wrist.y), (middle_tip.x, middle_tip.y))
    return distance < close

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            cur_x, cur_y = wrist.x * frame_width, wrist.y * frame_height
            if prev_x != 0 and prev_y != 0:
                dx = cur_x - prev_x
                dy = cur_y - prev_y
                velocity_x = dx - prev_dx
                velocity_y = dy - prev_dy
                if dragging:
                    scaled_dx = dx * (1 + abs(velocity_x) * accd)
                    scaled_dy = dy * (1 + abs(velocity_y) * accd)
                else:
                    scaled_dx = dx * (1 + abs(velocity_x) * acc)
                    scaled_dy = dy * (1 + abs(velocity_y) * acc)
                pyautogui.moveRel(scaled_dx, scaled_dy)
                prev_dx, prev_dy = dx, dy
            prev_x, prev_y = cur_x, cur_y 
            if is_hand_closed(hand_landmarks):
                if not dragging:
                    pyautogui.mouseDown()
                    dragging = True
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging = False
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    else:
        prev_x, prev_y = 0, 0  
        prev_dx, prev_dy = 0, 0  

    cv2.imshow("Hand Mouse Control (Acceleration)", cv2.resize(frame,(1300,900)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
