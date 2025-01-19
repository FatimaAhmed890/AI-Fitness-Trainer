import streamlit as st
import cv2
import numpy as np
import PoseModule 
import time
from squat_angle import findAngle

st.title("Squats 🏋🏻 with AI")
st.write("(Please carefully read the entire instruction manual before performing exercise and perform all movements slowly and deliberately to maintain control.)")

frame_placeholder = st.empty()
stop_button_pressed = st.button("Stop")

cap = cv2.VideoCapture(0)

pTime = 0
detector = PoseModule.poseDetector()
count = 0
direction = 1

while cap.isOpened() and not stop_button_pressed:
    success, img = cap.read()
    if not success:
        st.write("Video capture has ended")
        break
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img = cv2.flip(img, 1)
    img = detector.findPose(img, False) 
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        left_angle1, left_angle2 = detector.findAngle(img, 11, 12, 23, 24, 25, 27) 
        right_angle1, right_angle2 = detector.findAngle(img, 12, 11, 24, 23, 26, 28) 
        
        l_percentage1 = np.interp(left_angle1, (250, 300), (0, 100))
        l_percentage2 = np.interp(left_angle2, (60, 160), (0, 100))

        r_percentage1 = np.interp(right_angle1, (250, 300), (0, 100))
        r_percentage2 = np.interp(right_angle2, (60, 160), (0, 100))
        
        l_bar = np.interp(left_angle1, (250, 300), (650, 100))
        r_bar = np.interp(right_angle1, (250, 300), (650, 100))
        
        # check for the curls
        color = (255, 0, 255)
        if l_percentage1 == 100:
            color = (0, 255, 255)
            if direction == 1:
                count += 0.5
                direction = 0
        if l_percentage1 == 0:
            color = (255, 0, 255)
            if direction == 0:
                count += 0.5
                direction = 1
        if r_percentage1 == 100:
            color = (0, 255, 255)
            if direction == 1:
                count += 0.5
                direction = 0
        if r_percentage1 == 0:
            color = (255, 0, 255)
            if direction == 0:
                count += 0.5
                direction = 1
        
        height, width = img.shape[:2]
        # print(height, width) # 480 640
        
        x, y = width -570, 70
        
        radius = 70
        circle_color = (0, 255, 255)
        
        # Draw count
        
        # cv.circle(img, center, radius, color, thickness)
        cv2.circle(img, (x, y), radius, circle_color, thickness=-1)
        cv2.putText(img, str(count), (x-30, y+10), cv2.FONT_HERSHEY_PLAIN, 2,
                    (255, 0, 255), 4)
        
        # Draw Bar
        
        # cv2.rectangle(img, top_left, bottom_right, color, thickness)
        cv2.rectangle(img, (580, 100), (620, 460), color, 3)
        if l_percentage1:
            cv2.rectangle(img, (580, int(l_bar)), (620, 460), color, cv2.FILLED)
            cv2.putText(img, f'{int(l_percentage1)} %', (555, 80), cv2.FONT_HERSHEY_PLAIN, 2,
                        color, 3)
        else:
            cv2.rectangle(img, (580, int(l_bar)), (620, 460), color, cv2.FILLED)
            cv2.putText(img, f'{int(l_percentage1)} %', (555, 80), cv2.FONT_HERSHEY_PLAIN, 2,
                        color, 3)
        if r_percentage1:
            cv2.rectangle(img, (580, int(r_bar)), (620, 460), color, cv2.FILLED)
            cv2.putText(img, f'{int(r_percentage1)} %', (555, 80), cv2.FONT_HERSHEY_PLAIN, 2,
                        color, 3)
        else:
            cv2.rectangle(img, (580, int(r_bar)), (620, 460), color, cv2.FILLED)
            cv2.putText(img, f'{int(r_percentage1)} %', (555, 80), cv2.FONT_HERSHEY_PLAIN, 2,
                        color, 3)
              
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    # cv2.putText(img, str(int(fps)) + " frames per second", (20, 50), cv2.FONT_HERSHEY_PLAIN, 2,
    #             (255, 0, 255), 1)
    
    frame_placeholder.image(img, channels="RGB")
    
    if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
        break
    
cap.release()
cv2.destroyAllWindows()