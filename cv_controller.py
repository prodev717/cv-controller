import cv2
from math import dist
import mediapipe as mp
import pydirectinput

camera = cv2.VideoCapture(0)
mp_pose = mp.solutions.pose.Pose()
mp_draw = mp.solutions.drawing_utils

prev = None
movement = "NONE"
thresh = 30  

while camera.isOpened():
    ret, frame = camera.read()
    if not ret:
        break

    height, width, _ = frame.shape
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_pose.process(rgb)
    if result.pose_landmarks:
        nodes = result.pose_landmarks.landmark
        current = (int(nodes[0].x * width), int(nodes[0].y * height))
        if prev is not None:
            dif = (current[0] - prev[0], current[1] - prev[1])
            dis = dist(current, prev)
            if abs(dif[1]) > thresh and dis > thresh:
                movement = "s" if dif[1] > 0 else "w"
            elif abs(dif[0]) > thresh and dis > thresh:
                movement = "d" if dif[0] > 0 else "a"
            else:
                movement = None
            if movement!= None:
                pydirectinput.keyDown(movement)
                print(movement)
                pydirectinput.keyUp(movement)
            cv2.putText(frame, f"dif : {dif[0]} , {dif[1]}", (30, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 255), 2)
            cv2.putText(frame, f"dis : {dis:.2f}", (30, 60), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 255), 2)
            cv2.putText(frame, f"mov : {movement}", (30, 90), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 255), 2)
        prev = current
        mp_draw.draw_landmarks(frame,result.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
    cv2.imshow("cv controller", frame)
    
    if cv2.waitKey(1) == ord("q"):
        break

mp_pose.close()
camera.release()
cv2.destroyAllWindows()
